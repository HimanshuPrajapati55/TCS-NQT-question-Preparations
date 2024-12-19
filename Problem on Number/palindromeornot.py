def is_palindrome(num):
    """
    Check if a single integer is a palindrome.
    """
    rev_num = 0
    original = num
    while num > 0:
        digit = num % 10
        rev_num = (rev_num * 10) + digit
        num = num // 10
    return original == rev_num

def input_space_separated():
    """
    Accept space-separated integers from the user.
    """
    arr = list(map(int, input("Enter space-separated integers: ").split()))
    return arr

def main():
    """
    Main function to check for palindromes in a list of numbers.
    """
    arr = input_space_separated()
    for num in arr:
        if is_palindrome(num):
            print(f"{num} is a palindrome")
        else:
            print(f"{num} is not a palindrome")

if __name__ == "__main__":
    main()
