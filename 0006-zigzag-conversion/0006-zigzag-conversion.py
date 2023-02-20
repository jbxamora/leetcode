class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # If numRows is 1 or the length of s is less than numRows, no conversion is necessary
        if numRows == 1 or len(s) < numRows:
            return s

        # Initialize the result list with empty strings for each row
        result = ['' for _ in range(numRows)]

        # Initialize the current row and direction
        row, direction = 0, 1

        # Loop through each character in s
        for char in s:
            # Add the character to the current row
            result[row] += char
            
            # If we're at the first row, change direction to downwards
            if row == 0:
                direction = 1
            # If we're at the last row, change direction to upwards
            elif row == numRows - 1:
                direction = -1
            
            # Move to the next row in the current direction
            row += direction

        # Combine the strings in the result list to form the converted string
        return ''.join(result)
