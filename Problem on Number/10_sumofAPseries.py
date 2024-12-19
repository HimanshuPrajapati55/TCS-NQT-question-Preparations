"""
Find Sum of AP Series

Example 1:
Input:
n=4
a=2
d=2
Output: 20
Explanation: 2+4+6+8 = 20

Input:
n=8
a=2
d=5
Output: 124
Explanation: -2 +3 + 8 + 13 + 18 + 23 + 28 + 33 = 124
"""
# a = first term of A.P.
# d= common Difference of A.P.
# n= Number of Terms in  A.P.

def aP_Series(a,d,n):
    sum_ap = (n/2)*(2*a+(n-1)*d)
    return int(sum_ap)

def aP1_Series(a, d, n):
    """
    Calculate the sum of the first n terms of an AP without using the formula.
    :param a: First term
    :param d: Common difference
    :param n: Number of terms
    :return: Sum of the series
    """
    sum_ap = 0
    current_term = a
    for _ in range(n):  # Loop n times
        sum_ap += current_term
        current_term += d  # Move to the next term
    return sum_ap

print(aP_Series(a=2,d=2,n=4))
print(aP1_Series(a=2,d=2,n=4))
print(aP_Series(a=-2,d=5,n=8))

