The main idea of the solution is to divide the array into two parts: one with odd numbers and one with even numbers. We can then recursively apply the same approach to each part until we reach an array of length 1. This ensures that the resulting array is beautiful.
​
The implementation above does this in a slightly different way, by generating the array iteratively using a while loop. We start with a single element (1), and then at each iteration, we double the current elements in the array and add/subtract 1 to generate the next level of the array.
​
Finally, we return only the elements that are less than or equal to n. This ensures that we return an array of length n, even if the last level of the array has more elements.