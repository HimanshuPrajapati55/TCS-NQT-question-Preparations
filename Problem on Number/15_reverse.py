"roblem Statement: Given an integer. Write a program to reverse digits of a number."

def reverse(n):
    rev = 0
    
    while n > 0:
        digit = n % 10
        rev = (rev*10) + digit
        n = n//10
    
    return rev

print(reverse(123))