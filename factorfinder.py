import math
import sys
import matplotlib.pyplot as plt


# factor finder

def is_prime(num):
    """According to Wilson's Theorem, a number is prime if and only if (n-1)! + 1 is divisible by n."""
    if num > 1:
        return ((math.factorial(num - 1) + 1) % num == 0)
    else:
        return False

def get_possible_prime_factors(num):
    """Simple generator comprehension to return all the possible prime factors up to a number - Generators provide a much smaller
        memory footprint than lists."""
    return (i for i in range(num + 1) if is_prime(i))


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


def find_prime_factors(num, factors=[]):
    global primes #terrible form, I know.
    if num == 1:
        return flatten([1, *factors])

    # time to connect everything
    primes = get_possible_prime_factors(num)
    for prime in primes:
        if num % prime == 0:
            other_factor = int(num / prime)
            factors.append(prime)
            return flatten([find_prime_factors(other_factor, factors)])

def analysis():
    x = int(input("To what number would you like to analyze? "))
    primes = get_possible_prime_factors(x)
    sys.setrecursionlimit(x)
    y = [0]
    for i in range(1, x+1):
        thing = len(find_prime_factors(i, factors=[]))
        y.append(thing)
        print(f"{i}. {thing}")


    plt.plot(y, "ro")
    plt.axis([0, 1000, 0, 30])
    plt.show()

analysis()
