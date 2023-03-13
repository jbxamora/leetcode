class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Create a dictionary to store the last seen index of each character
        last_seen = {}
        # Initialize the starting index of the current substring and the maximum length
        start = 0
        max_len = 0
        # Loop through each character in the string
        for i, char in enumerate(s):
            # If the character is already in the substring, update the starting index
            # to the last seen index of the character + 1
            if char in last_seen and last_seen[char] >= start:
                start = last_seen[char] + 1
            # Update the last seen index of the character
            last_seen[char] = i
            # Update the maximum length if the current substring is longer
            max_len = max(max_len, i - start + 1)
        # Return the maximum length
        return max_len
