# Nhập n phần tử, mỗi phần tử cách nhau bởi khoảng trắng
n = int(input('Enter the number of elements: '))
lst = list(map(int, input('List: ').split()))

x = int(input('Enter x = '))

def is_divisible(a, b):
    """Kiểm tra a có chia hết cho b không"""
    if b == 0: return False
    return a % b == 0
result = 0
count = 0
for i in lst:
    if is_divisible(i, x): 
        result += i
        count += 1
    
print(result / count)