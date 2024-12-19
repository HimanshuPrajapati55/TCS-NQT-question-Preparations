def even_Or_Odd(n):
    return (n&1)

n = 101
if(even_Or_Odd(n) == 0):
    print("Even")
else:
    print("Odd")