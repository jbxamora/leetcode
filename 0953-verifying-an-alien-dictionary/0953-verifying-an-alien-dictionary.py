from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # Create a dictionary that maps each character to its order in the alien alphabet
        order_dict = {char: i for i, char in enumerate(order)}

        # Loop through the words pairwise
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
        
            # Loop through the characters in the words
            for j in range(min(len(word1), len(word2))):
                # If the characters are not the same, check their order in the alien alphabet
                if word1[j] != word2[j]:
                    if order_dict[word1[j]] > order_dict[word2[j]]:
                        # If the order is not correct, return False
                        return False
                    # If the order is correct, break out of the loop and check the next word pair
                    break
            else:
                # If the loop completes without finding a difference, check if the first word is longer than the second word
                if len(word1) > len(word2):
                    # If the first word is longer than the second word, return False
                    return False
            
        # If all word pairs are in the correct order, return True
        return True
