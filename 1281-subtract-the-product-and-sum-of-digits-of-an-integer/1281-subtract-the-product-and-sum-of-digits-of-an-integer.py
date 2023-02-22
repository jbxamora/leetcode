class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        # Initialize the product and sum of digits to 1 and 0, respectively
        product, sum = 1, 0
        # Iterate over each digit in the number
        while n:
            # Extract the last digit and update the product and sum
            digit = n % 10
            product *= digit
            sum += digit
            # Right shift the number to remove the last digit
            n //= 10
        # Return the difference between the product and sum of digits
        return product - sum
    
# Here's how the solution works:

# The subtractProductAndSum function takes in an integer n as input and returns the difference between the product and sum of its digits.
# We initialize two variables product and sum to 1 and 0, respectively, to keep track of the product and sum of digits.
# We then iterate over each digit in n using a while loop that continues as long as n is not 0.
# In each iteration of the loop, we extract the last digit of n using the modulus operator %, and update the product and sum variables accordingly.
# We then right shift n by 1 digit using the floor division operator // to remove the last digit and continue the loop.
# Once the loop has completed, we return the difference between the product and sum of digits.