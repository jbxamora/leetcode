class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # Initialize the left and right indices
        l = 0
        h = len(nums) - 1
        # Loop until the left and right indices converge
        while l <= h:
            # Calculate the midpoint index
            m = (l + h) // 2
            # Check if the single element is at the end of the list
            if m == len(nums) - 1:
                return nums[m]
            # Check if the single element is to the right of the midpoint
            if (m % 2 == 1 and nums[m] == nums[m - 1]) or (m % 2 == 0 and nums[m] == nums[m + 1]):
                l = m + 1
            # Check if the single element is to the left of the midpoint
            else:
                if l == m == h or m % 2 == 1:
                    h = m - 1
                else:
                    h = m
        # Return the single element
        return nums[m]
    
# Here's how the solution works:

# The singleNonDuplicate method takes in a list of integers as input and returns the single element that appears only once in the list.
# The function uses binary search to find the single element in O(log n) time complexity.
# The l and h indices are initialized to the first and last indices of the list, respectively.
# In each iteration of the loop, the m index is set to the middle index between l and h.
# If m is at the end of the list, then it must be the single element, so we return it.
# If nums[m] is equal to the number before or after it, then the single element must be on the right side of m, so we set l = m + 1.
# Otherwise, the single element must be on the left side of m, so we update h based on whether m is even or odd.
# We continue this process until l and h converge, at which point we have found the single element.
# Finally, we return the single element.