# Problem statement: Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and appear as many times as it shows in both arrays.

# One approach to solve this problem is to sort both arrays nums1 and nums2, and then use two pointers to traverse them. We can use i to traverse nums1 and j to traverse nums2. If nums1[i] is greater than nums2[j], we increment j. If nums1[i] is less than nums2[j], we increment i. If nums1[i] is equal to nums2[j], then we add nums1[i] to the result array res if it is not already present in res, and we increment both i and j. We repeat this process until one of the arrays is fully traversed.

# The steps to get the solution of this problem are as follows:

# Define a function intersection(nums1, nums2) that takes two integer arrays nums1 and nums2 as input.

# Sort both arrays nums1 and nums2 using the sort() method.

# Initialize two pointers i and j to 0.

# Use a while loop to traverse both arrays. In each iteration of the loop, check if nums1[i] is greater than nums2[j]. If it is, increment j. If nums1[i] is less than nums2[j], increment i. If nums1[i] is equal to nums2[j], add nums1[i] to the result array res if it is not already present in res, and increment both i and j.

# Repeat steps 4 until one of the arrays is fully traversed.

# Return the result array res.

# The time complexity of this approach is O(n log n), where n is the length of the longer input array after sorting. The space complexity is O(n) to store the result array.

# Here are some additional notes on the approach:

# The sort() method sorts an array in ascending order. In the provided solution, we sort both nums1 and nums2 in ascending order before traversing them.

# The result array res is initialized as an empty list at the beginning of the function.

# The check if nums1[i] not in res: is used to ensure that each element in the result is unique. If nums1[i] is already present in res, we do not add it again.

# Using two pointers to traverse two arrays is a common approach to solving array problems. It has a time complexity of O(n) and is useful for finding patterns in two sorted arrays or searching for elements in unsorted arrays.

class Solution(object):
    def intersection(self, nums1, nums2):
        res = []
        nums1.sort()
        nums2.sort()
        i = j = 0
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                if nums1[i] not in res:
                    res.append(nums1[i])
                i += 1
                j += 1
        
        return res