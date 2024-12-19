"""Check if given year is a leap year or not

In this post we will solve the problem "Check if given year is a leap year or not".

Problem Statement: Check if the given year is a leap year or not."""

def leap_year(year):
    if year < 0:
        return False
        
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True

def main():
    year = 2023
    if leap_year(year):
        print("Yes")
    else:
        print("No")



if __name__ == "__main__":
    main()