def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def main():
    count = 0
    size = int(input("Please enter the size of the array:"))
    for i in range(size):
        num = int(input("Enter a number: "))
        if is_prime(num):
            count += 1

    print(count)

if __name__ == "__main__":
    main()