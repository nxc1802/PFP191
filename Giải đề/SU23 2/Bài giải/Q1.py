import sys

# Copy-paste from cheat_sheet.py
def min_of_three(a, b, c):
    return min(a, b, c)

def main():
    # Given statements to input data
    a = int(input())
    b = int(input())
    c = int(input())
    
    # Write your statements here
    result = min_of_three(a, b, c)
    print(result)

if __name__ == "__main__":
    main()
