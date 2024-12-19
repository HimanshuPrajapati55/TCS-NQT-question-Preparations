"""
Problem Statement: Given a number N, print the smallest and largest digits present in the number.
Example 1:
Input: N = 2746
Output: Largest digit: 7
        Smallest digit: 2
Explanation: By simply going through the digits of 
the number, we figure out the largest and smallest 
digit in the number.

Example 2:
Input: N = 23004
Output: Largest digit : 4
        Smallest digit : 0
Explanation: By simply going through the digits of 
the number, we figure out the largest and smallest 
digit in the number.
"""

def min_max(num):
    mini = 9  
    maxi = 0
    while num != 0:
        d = num % 10  # Extract the last digit
        if d < mini:  # Compare manually
            mini = d 
        if d > maxi:
            maxi = d 
        num = num // 10  # Remove the last digit
    print("Minimum digit:", mini)
    print("maximum digit:", maxi)

min_max(4726)
