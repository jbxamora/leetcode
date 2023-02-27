class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Handle negative numbers
        if x < 0:
            return False
        
        # Convert the number to a string
        num_str = str(x)
        
        # Reverse the string and compare it to the original
        return num_str == num_str[::-1]
