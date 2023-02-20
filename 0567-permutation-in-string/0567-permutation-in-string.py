class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Compute the length of s1
        L = len(s1)
        
        # Initialize dictionaries for character counts
        dic_s2 = {}
        dic_s1 = {}
        
        # Initialize a variable for the left endpoint of the sliding window
        l = 0
        
        # Loop over all unique characters in s1 and s2 and initialize their counts to zero
        for char in set(s1 + s2):
            dic_s2[char] = 0
            dic_s1[char] = 0
        
        # Count the occurrences of each character in s1
        for char in s1:
            dic_s1[char] += 1
        
        # If s2 is shorter than s1, it cannot contain a permutation of s1
        if len(s2) < L:
            return False
        
        # Initialize the character counts for the first L characters of s2
        for i in range(L):
            dic_s2[s2[i]] += 1
        
        # Check if the first L characters of s2 form a permutation of s1
        if dic_s2 == dic_s1:
            return True
        
        # Slide the window one character to the right at a time
        for i in range(L, len(s2)):
            # Decrement the count of the character that is being removed from the window
            dic_s2[s2[l]] -= 1
            l += 1
            
            # Increment the count of the character that is being added to the window
            dic_s2[s2[i]] += 1
            
            # Check if the current window forms a permutation of s1
            if dic_s2 == dic_s1:
                return True
        
        # If no permutation of s1 is found, return False
        return False
