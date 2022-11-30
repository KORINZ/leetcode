"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k,
return the k closest points to the origin (0, 0).
The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).
You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
"""
from typing import List
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        for x, y in points:
            distance = x ** 2 + y ** 2
            min_heap.append([distance, x, y])

        heapq.heapify(min_heap)
        res = [heapq.heappop(min_heap)[1:] for i in range(k)]

        return res


if __name__ == '__main__':
    print(Solution().kClosest([[1, 3], [-2, 2]], k=1))  # [[-2,2]]

# Time Complexity: O(k*log(n))
# Memory Complexity: O(n)
