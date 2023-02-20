import collections
import math

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        # Count the frequencies of each card using a Counter object
        counter = collections.Counter(deck)
        
        # Find the greatest common divisor of the counts
        gcd_val = counter.popitem()[1]
        for count in counter.values():
            gcd_val = math.gcd(gcd_val, count)
        
        # Return True if the GCD is greater than or equal to 2, else False
        return gcd_val >= 2
