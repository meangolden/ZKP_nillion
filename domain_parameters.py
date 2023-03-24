# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 18:42:40 2023

@author: cp17593
"""

import random

def read_large_domain():
    filename = 'large_primes.txt'

    try:
        with open(filename, 'r') as f:
            large_domain = []
            for line in f:
                line = line.strip()  # Remove leading/trailing whitespace
                if line:  # Skip empty lines
                    num = int(line)
                    large_append(num)
        p, q, g, h = large_domain
        sizes = [ count_digits(num) for num in large_domain]
        if max(sizes) < 1e2:
            print(f'\nAgreed primes:\nq = {q}p = {p}')
            print(f'Agreed bases:g = {g}\nh = {h}')
            print()            
        print(f'Successfully read {len(large_domain)} integers from {filename}')
        print(f'The size of the four integers are {sizes}.')
    except FileNotFoundError:
        print(f'Could not find file {filename}')
        print()
    return large_domain


def check_parameters(q,p,g,h, display="on"):
       #See:https://en.wikipedia.org/wiki/Safe_and_Sophie_Germain_primes 
    assert_message = (
        "The prime order of 'g' and 'h' must be q. Use command line "
        "'os.startfile('prime_numbers.xlsx')' to open a list "
        "of valid domain parameters.\n\n"
        ) 
    assert is_prime(q), f'{q} is not a prime'
    assert is_prime(p), 'p is nota prime'
    if display == "on":
        print(f"Primality Test: Clear")
        print()
    
    if p < 1e8:  
        assert is_q_generator(g,q,p) and is_q_generator(h,q,p), assert_message
        if display == "on":
            print(f"\nPrime-Order Test: Clear")

    elif p >= 1e6 and p == 2*q + 1 :
        print("Some assertions have been deactivated due to the size of primes")
        print("provided. The method needs to be revised for increased efficieny")
        print("However, you provided a safe prime, which indicates that it was")
        print("acquired from a reliable source.")
        print()
    else:
        print("Prime number p is larger than 1e6. Some assertions have been ")
        print("deactivated. The method needs to be revised for increased efficiency")
        print()     

     
def is_q_generator(g,q,p):
    s = set([pow(g,i,p) for i in range(1,q)])
    if len(s) == q-1:
        return True
    else:
        return False
    
def is_prime(n, k=3):
    """
    Miller-Rabin primality test.
    Returns True if n is probably prime, False if n is composite.
    k is the number of iterations. Higher k means higher accuracy.\n\n
    """
    # Handle some small prime numbers separately
    if n in [2, 3]:
        return True
    if n == 1 or n % 2 == 0:
        return False

    # Write n-1 as 2^r*d
    r = 0
    d = n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Perform k iterations
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True
    
    
def find_primitives(q,p):
    """
    function generates two generators g and h of a cyclic group Z_q*, where \
    q and p are prime numbers. It uses the primitive root property of the\
    generators to ensure that g and h are unique and not equal to each other.\n\n"""
    assert p > 7
    for i in range(1000):  # Try up to 1000 times to find distinct a and b
        a = random.randint(2, p-2)
        b = random.randint(2, p-2)
        if a != b and a + b != p:
            break
    else:
        raise ValueError("Could not find distinct a and b. Try larger primes\n\n")
            
    g = pow(a, int((p-1)/q), p)
    h = pow(b, int((p-1)/q), p)
        
    assert g != h
    assert is_q_generator(g,q,p)
    assert is_q_generator(h,q,p)
        
    return g, h


def count_digits(n, base = 10):
    count = 0
    while n != 0:
        n //= base
        count += 1
    return count




