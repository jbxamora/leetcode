# The class Solution line defines a new class called Solution that is used to encapsulate the solution to the problem.

# The countOdds method takes in two integer arguments, low and high, and returns an integer. This method is used to count the number of odd integers between low and high.

# The if statement checks whether both low and high are even. If they are, then the number of odd integers in the range is (high - low) / 2. This is because if both low and high are even, then there are an equal number of even and odd integers in the range, and half of them are odd.

# The else statement is executed if either low or high is odd. In this case, the number of odd integers in the range is (high - low) / 2 + 1. This is because either the first or the last integer in the range is odd, so we need to add one to the number of odd integers in the range.

# The // operator is used for integer division, which means that the result is an integer and any remainder is discarded. This is used to count the number of odd integers in the range.

# First, we need to determine the number of odd integers in the range from low to high. One way to do this is to iterate through the range and count the odd integers. However, this approach would be slow for large ranges.

# Instead, we can use the fact that the difference between two consecutive odd integers is 2, and the difference between two consecutive even integers is also 2. This means that if both low and high are odd (or both are even), then there are (high - low) / 2 odd integers in the range. If one of low and high is odd and the other is even, then there are (high - low) / 2 + 1 odd integers in the range.

# We can use this knowledge to write a simple solution that checks whether both low and high are even, and calculates the number of odd integers accordingly. If one of low and high is odd, then we add one to the calculated number of odd integers to account for the odd number at either end of the range.

# Finally, we can encapsulate this solution in a class Solution and a countOdds method that takes in the low and high arguments and returns the number of odd integers in the range.

class Solution(object):
    def countOdds(self, low, high):
    
        if low % 2 == 0 and high % 2 == 0:
            return (high - low) // 2
        else:
            return (high - low) // 2 + 1
