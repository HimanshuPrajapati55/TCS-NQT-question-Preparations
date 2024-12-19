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

def input_min_max():
    """
    Accept min and max values from the user.
    """
    min_val, max_val = map(int, input("Enter min and max values separated by a space: ").split())
    return min_val, max_val

def main():
    """
    Main function to find and print palindromic numbers between min and max.
    """
    min_val, max_val = input_min_max()
    print("Palindromic numbers between", min_val, "and", max_val, ":")
    for num in range(min_val, max_val + 1):
        if is_palindrome(num):
            print(num, end=" ")

if __name__ == "__main__":
    main()
