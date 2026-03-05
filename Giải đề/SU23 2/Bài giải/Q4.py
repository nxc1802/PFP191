import sys

# Copy-paste from cheat_sheet.py
def sum_digits_in_string(s):
    total = 0
    for char in s:
        if char.isdigit():
            total += int(char)
    return total

def main():
    # Given statements to input data
    s = input()
    
    # Write your statements here
    result = sum_digits_in_string(s)
    print(result)

if __name__ == "__main__":
    main()
