from math import gcd
from collections import Counter

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = Counter(deck)
        values = list(count.values())
        gcd_val = values.pop()

        # Compute the GCD of all the counts in the deck
        for val in values:
            gcd_val = gcd(gcd_val, val)
            if gcd_val == 1:
                return False

        return gcd_val >= 2
