from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Create a Counter object for s1
        s1_counter = Counter(s1)

        # Initialize the window size, a Counter object for the current window, and the left and right pointers
        window_size = len(s1)
        window_counter = Counter(s2[:window_size])
        left, right = 0, window_size

        # Loop through each window in s2
        while right <= len(s2):
            # Check if the current window is a permutation of s1
            if s1_counter == window_counter:
                return True

            # Move the window to the right
            window_counter[s2[left]] -= 1
            if window_counter[s2[left]] == 0:
                del window_counter[s2[left]]
            if right < len(s2):
                window_counter[s2[right]] += 1

            left += 1
            right += 1

        return False
