"""
Program to find Sum of GP Series

Problem Statement: Given a geometric Progression (G.P) sequence with some inputs as:-

a, first term
r, common ratio
n, number of terms
 Write a program to find the sum of the geometric Progression Series.
"""
"""
Example 1:
Input: a=1 , r=0.5 , n=3
Output: 1.75
Explanation: The sum of given GP Series is 1.75

Example 2:
Input: a=3 , r=5 , n=2
Output: 18
Explanation: The sum of the given GP Series is 18
"""
def SumofGP(a,r,n):
    sum = 0
    for i in range(n):
        sum = sum+a
        a=a*r
    return sum

def main():
    a = 2
    r = 1.5
    n = 4
    print("Sum of GP series is",SumofGP(a,r,n))

if __name__ == "__main__":
    main()