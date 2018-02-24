def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True



def primes_list(N):
    '''
    N: an integer
    Returns a list of prime numbers
    '''
    prime_list = []
    for i in range(2, N + 1):
        if isPrime(i):
            prime_list.append(i)
    return prime_list

print(primes_list(10))