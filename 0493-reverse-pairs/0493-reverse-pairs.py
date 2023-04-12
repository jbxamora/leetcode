
from sortedcontainers import SortedList

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        sorted_nums = SortedList()
        count = 0

        for num in nums:
            count += len(sorted_nums) - sorted_nums.bisect_right(2 * num)
            sorted_nums.add(num)

        return count

