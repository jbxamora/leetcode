class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # Initialize the search range
        l, r = 1, num
        
        # Binary search
        while l + 1 < r:
            # Compute the middle element
            m = (l + r) // 2
            
            # Compute the square of the middle element
            sq = m * m
            
            # If the square matches the input, return True
            if sq == num:
                return True
            
            # If the square is greater than the input, search the left half
            elif sq > num:
                r = m
            
            # If the square is less than the input, search the right half
            else:
                l = m
        
        # Check if the left or right endpoint is a perfect square
        if l * l == num:
            return True
        if r * r == num:
            return True
        
        # If no perfect square is found, return False
        return False
