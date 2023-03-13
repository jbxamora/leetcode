```py
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
```
​
I use a dictionary `last_seen` to store the last seen index of each character because it allows me to quickly check whether a character is already in the current substring and find its last seen index.
I initialize the starting index of the current substring `(start)` to `0` and the maximum length of the substring `(max_len)` to `0` because the longest substring without repeating characters must start from some index and cannot be negative.
I use a for loop with enumerate to loop through each character in the string and its index, because I need to keep track of both the characters and their positions.
I check whether a character is already in the current substring and find its last seen index using if char in last_seen and `last_seen[char] >= start`, because if the character is not in the current substring, I don't need to update the starting index.
I update the last seen index of each character using `last_seen[char] = i`, so that I can find the last seen index of each character in the future.
I update the maximum length of the substring using `max_len = max(max_len, i - start + 1)`, because the length of the current substring is `i - start + 1`.
I return the maximum length of the substring at the end, because that is the length of the longest substring without repeating characters.