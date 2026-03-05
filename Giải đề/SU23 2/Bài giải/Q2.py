import sys
import math

# Copy-paste from cheat_sheet.py
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def sum_primes_less_than(n):
    total = 0
    for i in range(2, n):
        if is_prime(i):
            total += i
    return total

def main():
    # Given statement to input data
    n = int(input())
    
    # Write your statements here
    result = sum_primes_less_than(n)
    print(result)

if __name__ == "__main__":
    main()
