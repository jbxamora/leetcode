from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Create a Counter object for t
        t_counter = Counter(t)

        # Initialize the left and right pointers, the required count, and the min window and its length
        left, right = 0, 0
        required_count = len(t_counter)
        min_window, min_window_len = '', float('inf')

        # Loop through s using the right pointer
        while right < len(s):
            # If the current character is required for t, decrement the required count
            if s[right] in t_counter:
                t_counter[s[right]] -= 1
                if t_counter[s[right]] == 0:
                    required_count -= 1

            # While the current window contains all the characters in t, move the left pointer to the right
            while required_count == 0:
                # Update the min window if the current window is smaller
                if right - left + 1 < min_window_len:
                    min_window = s[left:right+1]
                    min_window_len = right - left + 1

                # If the character at the left pointer is required for t, increment the required count
                if s[left] in t_counter:
                    t_counter[s[left]] += 1
                    if t_counter[s[left]] > 0:
                        required_count += 1

                # Move the left pointer to the right
                left += 1

            # Move the right pointer to the right
            right += 1

        return min_window
