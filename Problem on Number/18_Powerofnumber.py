"""
xample 1:
Input:x = 2, n = 5
Output:32
Explanation: Calculate pow(2, 5) = 25 = 2*2*2*2*2 = 32
Example 2:
Input:x = 21, n = 2
Output: 441
Explanation:  Calculate pow(21, 2) = 212 = 21*21 = 441
"""

def main():
    x = 5
    n = 3
    ans = 1
    for i in range(n):
        ans *= x
    print(f"{x} raised to the power {n} is {ans}")


if __name__ == "__main__":
    main()