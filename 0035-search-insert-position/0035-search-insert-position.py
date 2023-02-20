class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1  # Initialize the left and right pointers
        while left <= right:  # Perform binary search
            mid = (left + right) // 2  # Calculate the middle index
            if nums[mid] == target:  # If target is found, return the index
                return mid
            elif nums[mid] < target:  # If target is greater than the middle element, search the right half
                left = mid + 1
            else:  # If target is smaller than the middle element, search the left half
                right = mid - 1
        return left  # If target is not found, return the index where it should be inserted
