str = input()

def sum_digits_in_string(s):
    """Tổng các ký tự là chữ số trong chuỗi"""
    return sum(int(char) for char in s if char.isdigit())

result = sum_digits_in_string(str)
print(result)