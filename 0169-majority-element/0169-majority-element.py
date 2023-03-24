from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Initialize a dictionary to store the count of each element
        count_dict = {}
        
        # Iterate through the list of numbers
        for num in nums:
            # If the number is not already in the dictionary, add it with a count of 1
            if num not in count_dict:
                count_dict[num] = 1
            # If the number is already in the dictionary, increment its count
            else:
                count_dict[num] += 1
        
        # Find the number with the highest count
        majority = max(count_dict, key=count_dict.get)
        
        # Return the majority element
        return majority
