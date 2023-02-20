class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # key: num
        # value: index of num
        # Space: O(N)
        # Time: O(N)
        
        # create a dictionary to store the difference between target and the current num as key
        # and the index of the current num as value
        num_to_id = {}
        
        # iterate over the nums list using enumerate to keep track of the index
        for i, num in enumerate(nums):
            # check if the difference between the target and the current num is in the dictionary
            if target - num in num_to_id:
                # if it is, return the current index i and the value of the difference in the dictionary
                return [i, num_to_id[target - num]]
            else:
                # otherwise, add the current num to the dictionary with its index as value
                num_to_id[num] = i
