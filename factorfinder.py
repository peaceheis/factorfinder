import typing
import sys

def factorial(num): 
    if num <= 1: 
        return 1
    
    return num * factorial(num - 1)

def is_prime(num):
    """According to Wilson's Theorem, a number is prime if and only if (n-1)! + 1 is divisible by n."""
    if num > 1: 
        return ((factorial(num - 1) + 1) % num == 0)
    else: 
        return False

def get_possible_prime_factors(num): 
    """Simple generator comprehension to return all the possible prime factors up to a number - Generators provide a much smaller
        memory footprint than lists."""

    return (i for i in range(int(num/2)) if is_prime(i))

def flatten(to_be_flattened):
    if len(to_be_flattened) == 1:
            if type(to_be_flattened[0]) == list:
                    result = flatten(to_be_flattened[0])   
            else:
                    result = to_be_flattened
    elif type(to_be_flattened[0]) == list:
            result = flatten(to_be_flattened[0]) + flatten(to_be_flattened[1:])
    else:
            result = [to_be_flattened[0]] + flatten(to_be_flattened[1:])
    return result

def remove_duplicates(to_be_cleaned):
    returned_list = []
    for item in to_be_cleaned: 
        if item not in to_be_cleaned: 
            returned_list.append(item)
        
def find_factors(num, factors = []): 
    if is_prime(num): 
        factors.append(num)
        return remove_duplicates(factors)
    #time to connect everything
    primes = get_possible_prime_factors(num)
    for prime in primes: 
        if num % prime == 0: 
            non_prime_factor = num/prime
            factors.append([prime, non_prime_factor])
            print(factors)
            return remove_duplicates(factors + (flatten(find_factors(non_prime_factor, factors))))
        

print(find_factors(20))