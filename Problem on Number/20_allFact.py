                                
def get_prime_factors(n):
    
    prime_factors = []
    
    
    for i in range(2, n + 1):
        if n % i == 0:
            
            prime_factors.append(i)
        
        while n % i == 0:
            n = n // i
            
    
    return prime_factors


if __name__ == "__main__":
    n = 60
    ans = get_prime_factors(n)
    print("Prime Factors for", n, ":", end=" ")
    for factor in ans:
        print(factor, end=" ")
    print()

                                
                            