import os

def is_armstrong(n):
    s = str(n)
    num_digits = len(s)
    total = sum(int(digit)**num_digits for digit in s)
    return total == n

def solve_case_1():
    filename = input().strip()
    if not os.path.exists(filename): return
    print("OUTPUT")
    with open(filename, 'r') as f:
        # Read all numbers separated by whitespace
        content = f.read().split()
        for num in content:
            print(num)

def solve_case_2():
    filename = input().strip()
    if not os.path.exists(filename): return
    print("OUTPUT")
    armstrong_nums = []
    with open(filename, 'r') as f:
        content = f.read().split()
        for num_str in content:
            try:
                num = int(num_str)
                if is_armstrong(num):
                    if num not in armstrong_nums:
                        armstrong_nums.append(num)
            except ValueError:
                continue
    # Sort and print
    armstrong_nums.sort()
    print(armstrong_nums)

def main():
    while True:
        try:
            print("Your selection (1 -> 2): ", end="")
            choice = input().strip()
            if not choice: break
            
            if choice == "1":
                solve_case_1()
            elif choice == "2":
                solve_case_2()
            
            print("FINISH")
        except EOFError:
            break

if __name__ == "__main__":
    main()
