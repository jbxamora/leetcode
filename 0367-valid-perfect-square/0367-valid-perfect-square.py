# Problem statement: Given a positive integer num, determine if it is a perfect square.

# One approach to solve this problem is to use binary search to find the square root of num. We can start with the left boundary b = 1 and the right boundary e = (num >> 1) + 1 since the square root of num cannot be greater than num/2 + 1. Then, we repeatedly calculate the middle point mid and its square sq. If sq is equal to num, then num is a perfect square and we can return True. If sq is greater than num, then we need to search in the left half of the range, so we update the right boundary e = mid - 1. Otherwise, we need to search in the right half of the range, so we update the left boundary b = mid + 1. We repeat this process until we find the square root of num or the range becomes empty.

# The steps to get the solution of this problem are as follows:

# Define a function isPerfectSquare(num) that takes a positive integer num as input.

# Initialize the left boundary b to 1 and the right boundary e to (num >> 1) + 1.

# Use a while loop to perform binary search. In each iteration of the loop, calculate the middle point mid using mid = (b + e) >> 1 and its square sq using sq = mid * mid.

# If sq is equal to num, then num is a perfect square and we can return True.

# If sq is greater than num, then we need to search in the left half of the range, so we update the right boundary e = mid - 1.

# Otherwise, we need to search in the right half of the range, so we update the left boundary b = mid + 1.

# Repeat steps 3 to 6 until we find the square root of num or the range becomes empty.

# If the range becomes empty, then num is not a perfect square and we can return False.

# The time complexity of this approach is O(log n), where n is the value of num. The space complexity is O(1) since we are only using a constant amount of extra space to store the left and right boundaries and the middle point.

# Here are some additional notes on the approach:

# The >> operator is the bitwise right shift operator, which shifts the bits of a number to the right by a specified number of positions. In the provided solution, (num >> 1) + 1 is equivalent to int(num**0.5) + 1, which is an upper bound on the square root of num.

# The loop condition b <= e is used to ensure that the search range is not empty. If the left boundary b becomes greater than the right boundary e, then there are no more elements to search and we can exit the loop.

# The binary search algorithm is a divide and conquer algorithm that works by repeatedly dividing the search range in half until the target element is found or the range is empty. It has a time complexity of O(log n) and is useful for searching in sorted arrays or other sorted data structures.


class Solution(object):
    def isPerfectSquare(self, num):
        b, e = 1, (num >> 1) + 1
        while b <= e:
            mid = (b + e) >> 1
            sq = mid * mid
            if sq == num:
                return True
            if sq > num:
                e = mid - 1
            else:
                b = mid + 1
        return False