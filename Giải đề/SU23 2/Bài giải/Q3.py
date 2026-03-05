import sys

# Copy-paste from cheat_sheet.py
def average_divisible_by(numbers, x):
    divisible = [n for n in numbers if n % x == 0]
    if not divisible:
        return 0
    return sum(divisible) / len(divisible)

def main():
    # Given statements to input data
    n = int(input()) # Number of elements (though we can just use the list)
    lst = []
    for _ in range(n):
        lst.append(int(input()))
    x = int(input())
    
    # Write your statements here
    res = average_divisible_by(lst, x)
    print(f"{res:.2f}")

if __name__ == "__main__":
    main()
