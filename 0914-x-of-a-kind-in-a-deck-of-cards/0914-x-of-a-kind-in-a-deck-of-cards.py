class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        counter = collections.Counter(deck)
        return math.gcd(*counter.values()) >= 2
