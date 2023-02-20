class Solution:
    def numberOfSteps (self, num: int) -> int:
        steps = 0  # Initialize the number of steps to 0
        while num:  # Continue as long as num is non-zero
            if num % 2 == 0:  # If num is even, divide by 2
                num //= 2
            else:  # If num is odd, subtract 1
                num -= 1
            steps += 1  # Increment the number of steps
        return steps  # Return the final number of steps
