import math
import sys
#factor finder
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

    return (i for i in range(int(num/2)+1) if is_prime(i))

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
        if item not in returned_list: 
            returned_list.append(item)
    return returned_list

def find_factors(num, factors = []): 
    if num == 1: 
        return [1]
    if is_prime(num): 
        factors.append(num)
        return remove_duplicates([1, *factors, num])
    #time to connect everything
    primes = get_possible_prime_factors(num)
    for prime in primes: 
        if num % prime == 0: 
            other_factor = int(num/prime)
            factors.append([prime, other_factor])
            return remove_duplicates([1, *flatten(factors + (find_factors(other_factor, factors))), num])
    

#factor analyzing

last = int(input("To what number would you like to analyze factors? "))
sys.setrecursionlimit(last+1)

analyzed_list = []
for i in range(1, last+1): 
    factors = find_factors(i, factors = []) 
    analyzed_list.append((i, len(factors), round(len(factors)/i, ndigits=3))) #(number, number of factors, ratio of factors to all numbers below)

analyzed_list = sorted(analyzed_list, key=lambda tup: tup[2], reverse=True)[:10] #sort in decreasing order by ratio

print(f"Done! Here are the 10 numbers from 1 to {last} with the highest ratios of factors to numbers less than the number:")
for i, analyzed in enumerate(analyzed_list): 
    print(f"{i+1}: {analyzed[0]} with {analyzed[1]} factors, a ratio of {analyzed[2]}") #Ex: 1: 10 with 4 factors, a ratio of ...

