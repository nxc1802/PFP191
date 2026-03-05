# Biến và Kiểu Dữ Liệu trong Python

## 1. Biến (Variables)

Biến là nơi lưu trữ dữ liệu trong chương trình. Python là ngôn ngữ **dynamic typing**, nghĩa là bạn không cần khai báo kiểu dữ liệu trước.

```python
# Khai báo biến
name = "Nguyen Van A"
age = 20
height = 1.75
is_student = True
```

### Quy tắc đặt tên biến:
- Bắt đầu bằng chữ cái hoặc dấu `_`
- Không bắt đầu bằng số
- Chỉ chứa chữ cái, số và `_`
- Phân biệt chữ hoa/thường (`Name` ≠ `name`)
- Không dùng từ khóa Python (`if`, `for`, `while`...)

---

## 2. Kiểu Dữ Liệu Cơ Bản

| Kiểu | Mô tả | Ví dụ |
|------|-------|-------|
| `int` | Số nguyên | `10`, `-5`, `0` |
| `float` | Số thực | `3.14`, `-2.5` |
| `str` | Chuỗi ký tự | `"Hello"`, `'Python'` |
| `bool` | Logic | `True`, `False` |

### Kiểm tra kiểu dữ liệu:
```python
x = 10
print(type(x))  # <class 'int'>
```

---

## 3. Chuyển Đổi Kiểu (Type Casting)

```python
# String -> Integer
s = "123"
n = int(s)      # n = 123

# Integer -> String
n = 456
s = str(n)      # s = "456"

# Integer -> Float
n = 10
f = float(n)    # f = 10.0

# Float -> Integer (cắt phần thập phân)
f = 3.9
n = int(f)      # n = 3
```

---

## 4. Nhập/Xuất Dữ Liệu

### Nhập từ bàn phím:
```python
name = input("Nhập tên: ")           # Luôn trả về string
age = int(input("Nhập tuổi: "))      # Chuyển sang int
```

### Xuất ra màn hình:
```python
print("Hello, World!")
print("Tên:", name, "- Tuổi:", age)
print(f"Tên: {name} - Tuổi: {age}")  # f-string (Python 3.6+)
```

---

## Tổng Kết

- **Biến** lưu trữ dữ liệu và không cần khai báo kiểu
- **4 kiểu cơ bản**: `int`, `float`, `str`, `bool`
- Dùng `type()` để kiểm tra kiểu
- Dùng `int()`, `float()`, `str()` để chuyển đổi kiểu
- `input()` luôn trả về chuỗi, cần chuyển đổi nếu cần số
