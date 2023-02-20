class Solution:
    def hasGroupsSizeX(self, deck):
        # Create a dictionary that stores the count of each unique card
        d = {}
        for x in deck:
            d[x] = d.get(x, 0) + 1
        
        # Compute the set of all card counts
        res = set(d.values())
        
        # If there is a group with only one card, it is impossible to divide the cards into groups of X
        if 1 in res:
            return False
        
        # If all groups have the same number of cards, it is possible to divide the cards into groups of X
        if len(res) == 1:
            return True
        
        # Use the Euclidean algorithm to compute the greatest common divisor of the card counts
        div = res.pop()
        for x in res:
            while x:
                div, x = x, div % x
        
            # If the GCD is 1, it is impossible to divide the cards into groups of X
            if div == 1:
                return False
        
        # If the GCD is not 1, it is possible to divide the cards into groups of X
        return div != 1
