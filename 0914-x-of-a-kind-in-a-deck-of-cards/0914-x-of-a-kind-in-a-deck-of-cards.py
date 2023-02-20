class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        # Use the Counter class to count the number of occurrences of each card in the deck
        ht = Counter(deck)
        
        # Compute the set of all counts
        counts_lst = set(ht.values())
        
        # Find the minimum count
        min_counts = min(counts_lst)

        # Check if the deck can be divided into groups of size i for i = 2, 3, ..., min_counts
        for i in range(2, min_counts+1):
            status = True
            for num in counts_lst:
                if num % i != 0:
                    # If any count is not divisible by i, it is impossible to divide the deck into groups of size i
                    status = False
                    break
            if status:
                # If all counts are divisible by i, the deck can be divided into groups of size i
                return True
        
        # If the deck cannot be divided into groups of any size, return False
        return False

