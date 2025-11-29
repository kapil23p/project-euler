def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            n //= i
        else:
            i += 1
    return n  

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(largest_prime_factor(n))