"""
Problem Statement: Given an integer Print “YES” if it is a strong number else print “NO”.

Note : 

When the sum of factorial of individual digits of a number is equal to the original number the number is called a strong number. 
Strong number is also known as Krishnamurthi number/Peterson Number.
Examples:

Examples 1:
Input: N = 145
Output: Yes
Explanation: 1! + 4! + 5! = 145. Hence 145 is a strong number. 

Example 2:
Input:  26
Output: No
Explanation: 2! + 6! = 722. Hence 26 is not a strong number.
"""
def factorical_no(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return fact

def Strong_No(num):
    sum = 0
    while num > 0:
        digit = num % 10
        sum = sum + factorical_no(digit)
        num = num//10
    return sum

def main():
    number = 145
    answer = Strong_No(number)
    if answer == number and number !=0:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
