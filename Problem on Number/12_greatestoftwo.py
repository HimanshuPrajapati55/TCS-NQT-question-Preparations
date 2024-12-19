"""Greatest of two numbers


10

0
Problem Statement: Given two numbers. Find the greatest of two numbers.

Examples:

Example 1:
Input: 1 3
Output: 3
Explanation: Answer is 3,since 3 is greater than 1.

Input: 1.123  1.124
Output: 1.124
Explanation: Answer is 1.124,since 1.124 is greater than 1.123."""

def Greatest_of_two(m,n):
    if m < n:
        print(n,"is the greatest Number")
    else:
        print(m,"is the greatest number")
    
Greatest_of_two(m=1,n=3)
Greatest_of_two(1.112,1.908)