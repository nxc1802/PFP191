# Các Thuật Toán Cơ Bản trong Python

## 1. Kiểm Tra Số Nguyên Tố

Số nguyên tố là số lớn hơn 1 và chỉ chia hết cho 1 và chính nó.

```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

> **Tối ưu**: Chỉ cần kiểm tra đến √n vì nếu n = a × b thì một trong hai sẽ ≤ √n

---

## 2. Tìm Min/Max

### Tìm không dùng hàm có sẵn:
```python
def find_min(numbers):
    if len(numbers) == 0:
        return None
    min_val = numbers[0]
    for n in numbers:
        if n < min_val:
            min_val = n
    return min_val

def find_max(numbers):
    if len(numbers) == 0:
        return None
    max_val = numbers[0]
    for n in numbers:
        if n > max_val:
            max_val = n
    return max_val
```

### Tìm min của 3 số:
```python
def min_of_three(a, b, c):
    if a <= b and a <= c:
        return a
    elif b <= a and b <= c:
        return b
    else:
        return c
```

---

## 3. Tính Tổng

### Tổng các số trong danh sách:
```python
def sum_list(numbers):
    total = 0
    for n in numbers:
        total += n
    return total
```

### Tổng các số nguyên tố nhỏ hơn n:
```python
def sum_primes_less_than(n):
    total = 0
    for i in range(2, n):
        if is_prime(i):
            total += i
    return total
```

---

## 4. Tính Trung Bình

### Trung bình của danh sách:
```python
def average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)
```

### Trung bình các số chia hết cho x:
```python
def average_divisible_by(numbers, x):
    divisible = [n for n in numbers if n % x == 0]
    if len(divisible) == 0:
        return 0
    return sum(divisible) / len(divisible)
```

---

## 5. Đếm Phần Tử

### Đếm số chẵn/lẻ:
```python
def count_even(numbers):
    count = 0
    for n in numbers:
        if n % 2 == 0:
            count += 1
    return count
```

### Đếm số thỏa điều kiện:
```python
def count_divisible_by(numbers, x):
    count = 0
    for n in numbers:
        if n % x == 0:
            count += 1
    return count
```

---

## 6. Xử Lý Chuỗi

### Đếm chữ số trong chuỗi:
```python
def count_digits(s):
    count = 0
    for char in s:
        if char.isdigit():
            count += 1
    return count
```

### Tổng các chữ số trong chuỗi:
```python
def sum_digits_in_string(s):
    total = 0
    for char in s:
        if char.isdigit():
            total += int(char)
    return total
```

---

## 7. Giai Thừa và Dãy Fibonacci

### Giai thừa (n!):
```python
def factorial(n):
    if n <= 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Đệ quy
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)
```

### Fibonacci:
```python
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib
```

---

## 8. Sắp Xếp

### Bubble Sort:
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
```

### Selection Sort:
```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
```

---

## Tổng Kết

| Thuật toán | Mục đích | Độ phức tạp |
|------------|----------|-------------|
| is_prime | Kiểm tra số nguyên tố | O(√n) |
| find_min/max | Tìm giá trị nhỏ/lớn nhất | O(n) |
| sum_list | Tính tổng | O(n) |
| average | Tính trung bình | O(n) |
| count | Đếm phần tử | O(n) |
| factorial | Tính giai thừa | O(n) |
| bubble_sort | Sắp xếp | O(n²) |
