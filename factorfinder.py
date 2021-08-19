import math

def factorial(num): 
    if num <= 1: 
        return 1
    
    return num * factorial(num - 1)

def is_prime(num):
    """According to Wilson's Theorem, a number is prime if and only if (n-1)! + 1 is divisible by n."""
    return ((factorial(num - 1) + 1) % num == 0)

def get_possible_prime_factors(num): 
    """Simple generator comprehension to return all the possible prime factors up to a number - Generators provide a much smaller
        memory footprint than lists."""
    return (i for i in range(int(num/2)) if is_prime(i))

def find_factors(num): 
    if is_prime(num): 
        return num

    #time to connect everything
    primes = get_possible_prime_factors(num)
    print(primes)
    print(next(primes))
    for prime in primes: 
        if num % prime == 0: 
            return set(prime, find_factors(num/prime))
        
