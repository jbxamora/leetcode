This solution uses the `datetime` module to create a date object corresponding to the given day, month, and year. It then uses the `weekday()` method of the date object to get the weekday index (`0 for Monday, 1 for Tuesday`, etc.), and uses a list of weekday names to look up the corresponding weekday name. Finally, it returns the weekday name as a string.
​
Time complexity:
​
Creating the datetime object takes constant time, `O(1)`.
Accessing the `weekday()` method of the `datetime` object takes constant time, `O(1)`.
Looking up the corresponding weekday name in the list takes constant time, `O(1)`.
Therefore, the overall time complexity of the solution is `O(1`).
​
Space complexity:
​
The solution uses a constant amount of additional memory for the `datetime` object, the list of weekday names, and the weekday index variable.
Therefore, the overall space complexity of the solution is also `O(1)`