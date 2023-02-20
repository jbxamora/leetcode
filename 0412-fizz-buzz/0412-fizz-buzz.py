class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        # Create an empty list to store the output
        result = []
        
        # Loop from 1 to n
        for i in range(1, n+1):
            # If i is divisible by 3 and 5, append "FizzBuzz" to the result list
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
            # If i is divisible by 3, append "Fizz" to the result list
            elif i % 3 == 0:
                result.append("Fizz")
            # If i is divisible by 5, append "Buzz" to the result list
            elif i % 5 == 0:
                result.append("Buzz")
            # Otherwise, append the string representation of i to the result list
            else:
                result.append(str(i))
        
        # Return the result list
        return result
