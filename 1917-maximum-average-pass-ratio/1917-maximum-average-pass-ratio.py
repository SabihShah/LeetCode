import heapq

class Solution(object):
    def maxAverageRatio(self, classes, extraStudents):
        """
        :type classes: List[List[int]]
        :type extraStudents: int
        :rtype: float
        """

        # function to calculate the gain of adding one student
        def gain(p, t):
            return (p + 1) / float(t + 1) - p / float(t)

        # build max heap with (-gain, p, t)
        heap = [(-gain(p, t), p, t) for p, t in classes]
        heapq.heapify(heap)

        # assign extra students one by one
        for _ in range(extraStudents):
            g, p, t = heapq.heappop(heap)   # class with max gain
            p, t = p + 1, t + 1
            heapq.heappush(heap, (-gain(p, t), p, t))

        # compute final average
        total = 0.0
        while heap:
            _, p, t = heapq.heappop(heap)
            total += p / float(t)

        return total / len(classes)
