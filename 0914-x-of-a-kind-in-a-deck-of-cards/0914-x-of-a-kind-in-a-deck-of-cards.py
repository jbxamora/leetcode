import math

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        # Create a frequency dictionary to store the count of each unique card
        freq = {}
        for x in deck:
            freq[x] = freq.get(x, 0) + 1
        
        # Get a list of the card counts, sorted in ascending order
        values = sorted(freq.values())
        
        # Check if the smallest count is less than or equal to 1
        smallest = values[0]
        if smallest <= 1:
            return False 
        
        # Find the factors of the smallest count.
        factors = set()
        for i in range(2, int(smallest ** 0.5) + 1):
            if smallest % i == 0:
                factors.add(i)
                factors.add(smallest // i)
        factors.add(smallest)
        
        # Check if the deck can be divided into groups of size X for any factor of the smallest count
        for f in factors:
            if all(x % f == 0 for x in values):
                return True
        
        # If the deck cannot be divided into groups of any size, return False.
        return False

