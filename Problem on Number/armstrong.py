def isArmstrong(num):
    # Calculate the number of
    # digits in the given number
    k = len(str(num))
    # Initialize the sum of digits
    # raised to the power of k to 0
    sum = 0
    n = num
    # Iterate through each
    # digit of the number
    while n > 0:
        # Extract the last
        # digit of the number
        ld = n % 10
        # Add the digit raised to
        # the power of k to the sum
        sum += ld ** k
        # Remove the last digit
        # from the number
        n = n // 10
    # Check if the sum of digits raised to
    # the power of k equals the original number
    return sum == num



if __name__ == "__main__":
    N = 153
    print("N:", N)
    digits = isArmstrong(N)
    print("Number of Digits in N:", digits)