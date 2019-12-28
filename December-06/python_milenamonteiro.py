import math

def prime_fibonnaci(n):
    def is_prime(n):
        n = abs(int(n))
        if n < 2: return False
        if n == 2: return True
        if n % 2 == 0: return False
        r = math.sqrt(n)
        x = 3 
        while x <= r:
            if n % x == 0: return False
            x += 2
        return True
    a = 0
    b = 1
    primes = []
    while len(primes) < n: 
        c = a + b 
        a = b 
        b = c 
        if is_prime(b):
            primes.append(b)
    return primes
    