# Toán Tử trong Python

## 1. Toán Tử Số Học (Arithmetic Operators)

| Toán tử | Mô tả | Ví dụ |
|---------|-------|-------|
| `+` | Cộng | `5 + 3 = 8` |
| `-` | Trừ | `5 - 3 = 2` |
| `*` | Nhân | `5 * 3 = 15` |
| `/` | Chia (trả về float) | `5 / 3 = 1.667` |
| `//` | Chia lấy phần nguyên | `5 // 3 = 1` |
| `%` | Chia lấy dư (modulo) | `5 % 3 = 2` |
| `**` | Lũy thừa | `5 ** 3 = 125` |

```python
a = 10
b = 3
print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333...
print(a // b)  # 3
print(a % b)   # 1
print(a ** b)  # 1000
```

---

## 2. Toán Tử So Sánh (Comparison Operators)

Trả về `True` hoặc `False`

| Toán tử | Mô tả | Ví dụ |
|---------|-------|-------|
| `==` | Bằng | `5 == 5` → `True` |
| `!=` | Khác | `5 != 3` → `True` |
| `>` | Lớn hơn | `5 > 3` → `True` |
| `<` | Nhỏ hơn | `5 < 3` → `False` |
| `>=` | Lớn hơn hoặc bằng | `5 >= 5` → `True` |
| `<=` | Nhỏ hơn hoặc bằng | `5 <= 3` → `False` |

```python
x = 10
y = 5
print(x == y)   # False
print(x != y)   # True
print(x > y)    # True
print(x < y)    # False
```

---

## 3. Toán Tử Logic (Logical Operators)

| Toán tử | Mô tả | Ví dụ |
|---------|-------|-------|
| `and` | VÀ (cả hai True) | `True and False` → `False` |
| `or` | HOẶC (ít nhất một True) | `True or False` → `True` |
| `not` | PHỦ ĐỊNH | `not True` → `False` |

```python
a = True
b = False
print(a and b)  # False
print(a or b)   # True
print(not a)    # False

# Ứng dụng
age = 20
has_id = True
can_enter = age >= 18 and has_id  # True
```

---

## 4. Toán Tử Gán (Assignment Operators)

| Toán tử | Tương đương | Ví dụ |
|---------|-------------|-------|
| `=` | Gán | `x = 5` |
| `+=` | `x = x + n` | `x += 3` |
| `-=` | `x = x - n` | `x -= 3` |
| `*=` | `x = x * n` | `x *= 3` |
| `/=` | `x = x / n` | `x /= 3` |
| `//=` | `x = x // n` | `x //= 3` |
| `%=` | `x = x % n` | `x %= 3` |

```python
x = 10
x += 5   # x = 15
x -= 3   # x = 12
x *= 2   # x = 24
```

---

## 5. Độ Ưu Tiên Toán Tử

Từ cao đến thấp:
1. `**` (lũy thừa)
2. `*`, `/`, `//`, `%`
3. `+`, `-`
4. `==`, `!=`, `<`, `>`, `<=`, `>=`
5. `not`
6. `and`
7. `or`

```python
# Ví dụ về độ ưu tiên
result = 2 + 3 * 4      # = 2 + 12 = 14 (nhân trước)
result = (2 + 3) * 4    # = 5 * 4 = 20 (ngoặc trước)
```

---

## Tổng Kết

- **Số học**: `+`, `-`, `*`, `/`, `//`, `%`, `**`
- **So sánh**: `==`, `!=`, `>`, `<`, `>=`, `<=`
- **Logic**: `and`, `or`, `not`
- **Gán**: `=`, `+=`, `-=`, `*=`, `/=`
- Dùng `()` để thay đổi độ ưu tiên
