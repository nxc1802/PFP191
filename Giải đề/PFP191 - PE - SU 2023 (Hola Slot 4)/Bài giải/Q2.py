n = int(input())

def is_prime(n):
    """Kiểm tra số nguyên tố"""
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

result = 0
for i in range(n):
    if is_prime(i): result += i

print(result)