class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        # Find the lengths of the two strings
        len1 = len(str1)
        len2 = len(str2)
        
        # Calculate the greatest common divisor of the lengths
        while len2:
            len1, len2 = len2, len1 % len2
        
        # Check if the shorter string is a divisor of the longer string
        if str1 + str2 != str2 + str1:
            return ""
        
        # Return the greatest common divisor
        return str1[:len1]
