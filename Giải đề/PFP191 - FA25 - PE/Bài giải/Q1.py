def solve_case_1():
    n = int(input("Enter the number of terms: "))
    s = 0
    for i in range(1, n + 1):
        s += (-1)**(i+1) / i**i

    print("OUTPUT")
    print(f"{s:.4f}")

def solve_case_2():
    print("Enter a string: ", end="")
    s = input()
    words = s.split()
    words.sort()
    print("OUTPUT")
    print(words)

def solve_case_3():
    print("Enter a number of rows: ", end="")
    rows = int(input())
    fib = [0, 1]
    for i in range(rows-1):
        fib.append(fib[-1] + fib[-2])
    print(fib)
    
    fib_val = fib[1:] if rows > 0 else []
    if not fib_val:
        return

    print("OUTPUT")
    for i in range(rows):
        val = fib_val[i]
        if i == 0: print(val)
        elif i == rows - 1: print(f"{val}" + "*"*i)
        else: print(f"{val}" + " "*(i-1) + "*")

def main():
    while True:
        try:
            print("Your selection (1 -> 3): ", end="")
            choice = input().strip()
            if not choice: break
            
            if choice == "1":
                solve_case_1()
            elif choice == "2":
                solve_case_2()
            elif choice == "3":
                solve_case_3()
            
            print("FINISH")
        except EOFError:
            break

if __name__ == "__main__":
    main()