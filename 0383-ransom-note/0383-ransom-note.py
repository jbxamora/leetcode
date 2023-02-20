class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_dict = {}
        for char in magazine:  # Create a dictionary with the counts of each character in the magazine
            mag_dict[char] = mag_dict.get(char, 0) + 1
        for char in ransomNote:  # Iterate through the ransom note and decrement the count of each character in the dictionary
            if mag_dict.get(char, 0) <= 0:
                return False
            mag_dict[char] -= 1
        return True
