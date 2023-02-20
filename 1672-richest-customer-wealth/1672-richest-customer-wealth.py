class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # Initialize the maximum wealth to be zero
        max_wealth = 0
        
        # Loop over the rows in the accounts matrix
        for row in accounts:
            # Calculate the sum of the elements in the row
            row_sum = sum(row)
            
            # Update the maximum wealth if necessary
            if row_sum > max_wealth:
                max_wealth = row_sum
        
        # Return the maximum wealth
        return max_wealth
