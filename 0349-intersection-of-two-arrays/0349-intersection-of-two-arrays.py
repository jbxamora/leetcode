# Problem statement: Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and appear as many times as it shows in both arrays.

# Another approach to solve this problem is to use sets. We can convert both arrays nums1 and nums2 to sets, and then use the set intersection operator & to find the common elements between the two sets. Finally, we convert the resulting set back to a list and return it.

# The steps to get the solution of this problem are as follows:

# Define a function intersection(nums1, nums2) that takes two integer arrays nums1 and nums2 as input.

# Convert nums1 and nums2 to sets using the set() function.

# Find the intersection of the two sets using the set intersection operator &.

# Convert the resulting set back to a list using the list() function.

# Return the list of common elements.

# The time complexity of this approach is O(n), where n is the total number of elements in both input arrays. The space complexity is also O(n) to store the sets.

# Here are some additional notes on the approach:

# The set() function creates a set from a given iterable (such as a list or a tuple). Sets are unordered collections of unique elements.

# The set intersection operator & returns a set containing the common elements between two sets.

# The list() function creates a list from a given iterable. In the provided solution, we use this function to convert the resulting set back to a list.

# Using sets is a useful approach when we need to find the intersection or union of two lists and we do not care about the order of the elements. However, sets are not useful when we need to preserve the order of the elements or when we need to access elements by index.

class Solution(object):
    def intersection(self, nums1, nums2):
        return list(set(nums1) & set(nums2))
        