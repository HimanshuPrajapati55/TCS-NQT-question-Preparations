def print_factore(x):
    print("The factors of",x,"are:")
    for i in range(1, x+1):
        if x%i == 0:
            print(i)

num = 10
print_factore(num)