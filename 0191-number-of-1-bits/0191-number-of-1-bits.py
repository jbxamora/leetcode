class Solution:
    def hammingWeight(self, n: int) -> int:
        # Initialize the count of 1 bits to 0
        count = 0
        # Iterate over each bit in the number
        while n:
            # Check if the last bit is a 1
            if n & 1 == 1:
                count += 1
            # Right shift the number to remove the last bit
            n >>= 1
        # Return the count of 1 bits
        return count
