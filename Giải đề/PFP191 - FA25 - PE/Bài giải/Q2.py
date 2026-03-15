import os

def solve_case_1():
    filename = input().strip()
    if not os.path.exists(f"Giải đề/PFP191 - FA25 - PE/Bài giải/{filename}"):
        print("File not found")
        return
    
    with open(f"Giải đề/PFP191 - FA25 - PE/Bài giải/{filename}", "r") as f:
        content = f.read().split()
        print(content)


def is_amstrong(num):
    num_str = str(num)
    length = len(num_str)
    sum = 0
    for digit in num_str:
        sum += int(digit)**length
    return sum == num


def solve_case_2():
    filename = input().strip()
    if not os.path.exists(f"Giải đề/PFP191 - FA25 - PE/Bài giải/{filename}"):
        print("File not found")
        return
    
    with open(f"Giải đề/PFP191 - FA25 - PE/Bài giải/{filename}", "r") as f:
        content = f.read().split()
        armstrong_nums = []
        for num_str in content:
            num = int(num_str)
            if is_amstrong(num) and num not in armstrong_nums:
                armstrong_nums.append(num)
        print(sorted(armstrong_nums))

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