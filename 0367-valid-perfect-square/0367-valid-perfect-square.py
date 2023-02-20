class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # Base case: if num is 1, it is a perfect square
        if num == 1:
            return True
        
        # Binary search the first half of the search space
        left, right = 1, num // 2 + 1
        while left <= right:
            mid = left + (right - left) // 2
            square = mid * mid
            if square == num:
                return True
            elif square < num:
                left = mid + 1
            else:
                right = mid - 1
        
        # If the loop terminates without finding a perfect square, num is not a perfect square
        return False