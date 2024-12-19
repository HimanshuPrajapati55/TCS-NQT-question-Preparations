"""Problem Statement: Given three numbers. Find the greatest of three numbers.

Examples:

Example 1:
Input: 1 3 5
Output: 5
Explanation: Answer is 5.Since 5 is greater than 1 and 3.

Example 2:
Input: 1.123  1.124 1.125
Output: 1.125
Explanation: Answer is 1.125. Since 1.125 is greater than 1.123 and 1.124"""

def three_greatest(a,b,c):
    if a > b and a>c:
        print(a,"is the greatest")
    elif b>a and b>c:
        print(b,"is the greatest")
    else:
        print(c,"is the greatest")
        


three_greatest(1,2,3)
three_greatest(1.67,1.78,1.01)
three_greatest(1000,2,1)