class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Initialize the count array for characters in t
        count_t = [0] * 128
        for char in t:
            count_t[ord(char)] += 1

        # Initialize the left and right pointers, the required count, and the minimum window length and starting index
        left, right = 0, 0
        required_count = len(t)
        min_window_len, min_window_start = float('inf'), 0

        # Loop through s using the right pointer
        while right < len(s):
            # If the current character is required for t, decrement the required count
            if count_t[ord(s[right])] > 0:
                required_count -= 1
            count_t[ord(s[right])] -= 1

            # While the current window contains all the characters in t, move the left pointer to the right
            while required_count == 0:
                # Update the minimum window if the current window is smaller
                if right - left + 1 < min_window_len:
                    min_window_len = right - left + 1
                    min_window_start = left

                # If the character at the left pointer is required for t, increment the required count
                count_t[ord(s[left])] += 1
                if count_t[ord(s[left])] > 0:
                    required_count += 1

                # Move the left pointer to the right
                left += 1

            # Move the right pointer to the right
            right += 1

        # Create the minimum window using slicing
        min_window = s[min_window_start:min_window_start + min_window_len] if min_window_len != float('inf') else ''

        return min_window



