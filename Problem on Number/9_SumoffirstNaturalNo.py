"""
Example 1:
Input: N=5
Output: 15
Explanation: 1+2+3+4+5=15

Example 2:
Input: N=6
Output: 21
Explanation: 1+2+3+4+5+6=15
"""

def sum_of_Natural(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum

print(sum_of_Natural(5))