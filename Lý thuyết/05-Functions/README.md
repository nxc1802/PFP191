# Hàm (Functions) trong Python

## 1. Định Nghĩa Hàm

Hàm là khối code có thể tái sử dụng, thực hiện một nhiệm vụ cụ thể.

### Cú pháp:
```python
def tên_hàm(tham_số):
    # code thực thi
    return giá_trị  # (tùy chọn)
```

### Ví dụ đơn giản:
```python
def greet(name):
    print(f"Xin chào, {name}!")

greet("Hải")  # Output: Xin chào, Hải!
```

---

## 2. Tham Số và Đối Số

### Tham số mặc định:
```python
def greet(name, greeting="Xin chào"):
    print(f"{greeting}, {name}!")

greet("Hải")               # Xin chào, Hải!
greet("Hải", "Hello")      # Hello, Hải!
```

### Nhiều tham số:
```python
def add(a, b):
    return a + b

result = add(3, 5)  # result = 8
```

### Đối số theo tên (keyword arguments):
```python
def info(name, age, city):
    print(f"{name}, {age} tuổi, ở {city}")

info(age=20, city="Hà Nội", name="Hải")
```

---

## 3. Return - Trả Về Giá Trị

### Trả về một giá trị:
```python
def square(n):
    return n ** 2

result = square(5)  # result = 25
```

### Trả về nhiều giá trị:
```python
def min_max(numbers):
    return min(numbers), max(numbers)

minimum, maximum = min_max([3, 1, 4, 1, 5])
print(f"Min: {minimum}, Max: {maximum}")
```

### Không có return:
```python
def say_hello():
    print("Hello!")
    # Không có return → trả về None

result = say_hello()  # result = None
```

---

## 4. Phạm Vi Biến (Variable Scope)

### Biến cục bộ (Local):
```python
def my_function():
    x = 10  # Biến cục bộ
    print(x)

my_function()
# print(x)  # LỖI! x không tồn tại bên ngoài hàm
```

### Biến toàn cục (Global):
```python
x = 10  # Biến toàn cục

def my_function():
    print(x)  # Có thể đọc

def modify():
    global x  # Khai báo dùng biến toàn cục
    x = 20

my_function()  # 10
modify()
print(x)       # 20
```

---

## 5. Các Pattern Hàm Thường Gặp

### Hàm kiểm tra:
```python
def is_even(n):
    return n % 2 == 0

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

### Hàm tính toán:
```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)  # Đệ quy

def sum_list(numbers):
    total = 0
    for n in numbers:
        total += n
    return total
```

### Hàm xử lý danh sách:
```python
def filter_even(numbers):
    result = []
    for n in numbers:
        if n % 2 == 0:
            result.append(n)
    return result
```

---

## 6. Lambda Functions

Hàm ẩn danh, viết trên một dòng.

```python
# Cú pháp: lambda tham_số: biểu_thức

square = lambda x: x ** 2
print(square(5))  # 25

add = lambda a, b: a + b
print(add(3, 4))  # 7

# Thường dùng với sorted, filter, map
numbers = [3, 1, 4, 1, 5]
sorted_nums = sorted(numbers, key=lambda x: -x)  # Sắp xếp giảm
print(sorted_nums)  # [5, 4, 3, 1, 1]
```

---

## Tổng Kết

- **def** để định nghĩa hàm
- **Tham số** có thể có giá trị mặc định
- **return** trả về giá trị (None nếu không có)
- **Biến cục bộ** chỉ tồn tại trong hàm
- Dùng **global** để dùng biến toàn cục
- **Lambda** cho hàm đơn giản một dòng
