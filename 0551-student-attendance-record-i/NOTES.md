Problem Statement:
You are given a string representing an attendance record for a student. The record only contains the following three characters:
​
'A': Absent
'L': Late
'P': Present
A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).
​
Write a function called checkRecord that takes in a string s and returns a boolean value indicating if the record is eligible for a reward.
​
Approach:
We can use a simple iterative approach to count the number of 'A's and continuous 'L's in the string. We'll also keep a track of the count of continuous 'L's. We'll set the count of continuous 'L's to 0 when we encounter a 'P' (present) or 'A' (absent).
​
Steps:
Initialize the count of continuous 'L's to 0 and the count of 'A's to 0.
Loop through the string and:
a. If the current character is 'A', increment the count of 'A's.
b. If the current character is 'L', increment the count of continuous 'L's.
c. If the current character is 'P', reset the count of continuous 'L's to 0.
d. If the count of 'A's is greater than 1 or the count of continuous 'L's is greater than 2, return False.
If the loop completes, return True.
Complexity Analysis:
Time Complexity: O(n), where n is the length of the input string s.
Space Complexity: O(1), we only need to keep track of a few variables to solve the problem.