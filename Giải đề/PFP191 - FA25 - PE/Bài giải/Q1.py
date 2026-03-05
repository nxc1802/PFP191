def solve_case_1():
    n = int(input("Enter the number of terms: "))
    # S = 1 - 1/2^2 + 1/3^3 - 1/4^4 + ... + ((-1)^(n+1))/n^n
    s = 0
    for i in range(1, n + 1):
        term = ((-1)**(i+1)) / (i**i)
        s += term
    print("OUTPUT")
    print(f"{s:.4f}")

def solve_case_2():
    s = input("Enter a string: ")
    words = s.split()
    # Sort alphabetically
    words.sort()
    print("OUTPUT")
    print(words)

def solve_case_3():
    rows = int(input("Enter the number of rows: "))
    # Fibonacci hollow triangle
    # First, get Fibonacci sequence
    fib = [0, 1]
    while len(fib) < rows:
        fib.append(fib[-1] + fib[-2])
    
    # We need the values: 1, 1, 2, 3, 5... (starting from fib[1])
    fib_vals = fib[1:] if rows > 0 else []
    if not fib_vals:
        return

    print("OUTPUT")
    for i in range(rows):
        val = fib_vals[i]
        if i == 0:
            print(val)
        elif i == rows - 1:
            # Bottom row is all asterisks
            print(f"{val}" + "*" * (i))
        else:
            # Hollow middle
            print(f"{val}" + " " * (i-1) + "*")

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
