# Chuỗi (Strings) trong Python

## 1. Tạo Chuỗi

```python
# Dấu nháy đơn hoặc kép
s1 = 'Hello'
s2 = "World"

# Chuỗi nhiều dòng
s3 = """Đây là
chuỗi nhiều
dòng"""

# Chuỗi rỗng
empty = ""
```

---

## 2. Truy Cập Ký Tự

Giống như list, string dùng **index** và **slicing**.

```python
s = "Python"
#    0 1 2 3 4 5    (index dương)
#   -6-5-4-3-2-1    (index âm)

print(s[0])      # "P"
print(s[-1])     # "n"
print(s[0:3])    # "Pyt"
print(s[::-1])   # "nohtyP" (đảo ngược)
```

> ⚠️ **Lưu ý**: String là **immutable** (không thể thay đổi từng ký tự)

---

## 3. Các Phương Thức Thường Dùng

### Thay đổi case:
```python
s = "Hello World"
s.upper()      # "HELLO WORLD"
s.lower()      # "hello world"
s.title()      # "Hello World"
s.capitalize() # "Hello world"
s.swapcase()   # "hELLO wORLD"
```

### Tìm kiếm:
```python
s = "Hello World"
s.find("o")      # 4 (index đầu tiên, -1 nếu không có)
s.index("o")     # 4 (như find nhưng lỗi nếu không có)
s.count("o")     # 2 (đếm số lần xuất hiện)
s.startswith("He")  # True
s.endswith("ld")    # True
"o" in s         # True (kiểm tra có chứa)
```

### Xử lý khoảng trắng:
```python
s = "  Hello World  "
s.strip()    # "Hello World" (xóa 2 đầu)
s.lstrip()   # "Hello World  " (xóa đầu trái)
s.rstrip()   # "  Hello World" (xóa đầu phải)
```

### Thay thế và tách:
```python
s = "Hello World"
s.replace("World", "Python")  # "Hello Python"

s = "apple,banana,cherry"
s.split(",")   # ["apple", "banana", "cherry"]

# Nối list thành string
fruits = ["apple", "banana", "cherry"]
",".join(fruits)  # "apple,banana,cherry"
```

### Kiểm tra:
```python
"123".isdigit()     # True (chỉ chứa số)
"abc".isalpha()     # True (chỉ chứa chữ)
"abc123".isalnum()  # True (chữ hoặc số)
"   ".isspace()     # True (chỉ chứa khoảng trắng)
```

---

## 4. Định Dạng Chuỗi

### f-string (Python 3.6+):
```python
name = "Hải"
age = 20
print(f"Tên: {name}, Tuổi: {age}")
print(f"Năm sau: {age + 1}")
print(f"Pi: {3.14159:.2f}")  # Làm tròn 2 chữ số
```

### format():
```python
print("Tên: {}, Tuổi: {}".format(name, age))
print("Tên: {0}, Tuổi: {1}".format(name, age))
```

### % operator:
```python
print("Tên: %s, Tuổi: %d" % (name, age))
```

---

## 5. Các Pattern Thường Gặp

### Đếm ký tự:
```python
def count_char(s, char):
    count = 0
    for c in s:
        if c == char:
            count += 1
    return count
```

### Đảo ngược chuỗi:
```python
def reverse_string(s):
    return s[::-1]
```

### Kiểm tra palindrome:
```python
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]
```

### Đếm từ:
```python
def count_words(s):
    return len(s.split())
```

### Tổng các số trong chuỗi:
```python
def sum_digits(s):
    total = 0
    for char in s:
        if char.isdigit():
            total += int(char)
    return total
```

---

## 6. Escape Characters

| Ký tự | Ý nghĩa |
|-------|---------|
| `\n` | Xuống dòng |
| `\t` | Tab |
| `\\` | Dấu \ |
| `\'` | Dấu ' |
| `\"` | Dấu " |

```python
print("Hello\nWorld")  # Xuống dòng
print("Tab\there")     # Tab
```

---

## Tổng Kết

- String là **immutable** (không thể thay đổi)
- Truy cập bằng **index** và **slicing**
- Các phương thức: `upper()`, `lower()`, `find()`, `replace()`, `split()`, `join()`
- Dùng **f-string** để định dạng
- Dùng `in` để kiểm tra chứa chuỗi con
