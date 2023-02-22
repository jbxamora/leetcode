class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Use binary search to find the single element
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            # Check if mid is the single element
            if mid % 2 == 0 and nums[mid] == nums[mid + 1]:
                left = mid + 2
            elif mid % 2 == 1 and nums[mid] == nums[mid - 1]:
                left = mid + 1
            else:
                right = mid
        # Return the single element
        return nums[left]
    
# Here's how the solution works:

# The singleNonDuplicate function takes in a sorted list of integers as input and returns the single element that appears only once in the list.
# The function uses binary search to find the single element in O(log n) time complexity.
# The left and right pointers are initialized to the first and last indices of the list, respectively.
# In each iteration of the loop, the mid pointer is set to the middle index between left and right.
# If mid is even and nums[mid] == nums[mid+1], then the single element must be on the right side of mid. So, we set left = mid + 2.
# If mid is odd and nums[mid] == nums[mid-1], then the single element must be on the right side of mid. So, we set left = mid + 1.
# Otherwise, the single element must be on the left side of mid. So, we set right = mid.
# The loop continues until left == right, at which point we have found the single element.
# Finally, the function returns the single element.