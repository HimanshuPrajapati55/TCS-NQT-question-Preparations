def prime_in_range(n,m):
    if n > m:
        print("Invalid range: n should be less than or equal to m.")
        return []

    primes = []
    for num in range(n, m+1):
        if num > 1:
            is_prime = True
            for i in range(2, int(num ** 0.5)+1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)
    return primes

n, m = 10, 50
result = prime_in_range(n, m)
if result:
    print(f"Prime numbers in the range [{n}, {m}]:", result)
else:
    print(f"No prime numbers found in the range [{n}, {m}].")
    