a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

def find_min_3(a, b, c):
    min_val = a
    if b < min_val: min_val = b
    if c < min_val: min_val = c
    return min_val

result = find_min_3(a, b, c)

print(result)