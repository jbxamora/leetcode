class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        # Create a frequency dictionary to store the count of each unique card
        freq = {}
        for x in deck:
            if x in freq:
                freq[x] += 1
            else:
                freq[x] = 1 
        
        # Get a list of the card counts, sorted in ascending order
        values = sorted(freq.values())
        
        # Check if the smallest count is less than or equal to 1
        smallest = values[0]
        if smallest <= 1:
            return False 
        
        # Use the square root of the smallest count as an upper bound for the possible values of X
        m = math.ceil(smallest**(1/2))

        # Check if the deck can be divided into groups of size X for X = 2, 3, ..., m+1
        for i in range(2, m+2):
            if smallest % i == 0:
                if all(x % i == 0 for x in values[1:]):
                    return True
        
        # Check if the deck can be divided into groups of size smallest.
        if all(x % smallest == 0 for x in values[1:]):
            return True
        
        # If the deck cannot be divided into groups of any size, return False.
        return False

