class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # Use a list comprehension to calculate the sum of each account
        account_sums = [sum(account) for account in accounts]
        
        # Return the maximum sum of the accounts
        return max(account_sums)
