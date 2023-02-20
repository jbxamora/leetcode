class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # Base case: num is 1, which is a perfect square
        if num < 2:
            return True
        
        # Initialize the search range
        left, right = 2, num // 2
        
        # Binary search
        while left <= right:
            # Compute the middle element using integer division
            mid = (left + right) // 2
            
            # Compute the square of the middle element
            square = mid * mid
            
            # If the square matches the input, return True
            if square == num:
                return True
            
            # If the square is greater than the input, search the left half
            elif square > num:
                right = mid - 1
            
            # If the square is less than the input, search the right half
            else:
                left = mid + 1
        
        # If the loop terminates without finding a perfect square, return False
        return False
