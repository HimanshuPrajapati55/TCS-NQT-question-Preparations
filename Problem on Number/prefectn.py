def Prefectno(n):
    sum = 0
    for i in range(1,n-1):  
        if i%2 == 0:
            sum += i

    if sum == n:
        print("Prefect number")
    else:
        print("No prefect No")

if __name__ == "__main__":
    n = 6
    Prefectno(n)
        