def main():
    month = int(input("Enter a month: "))
    if month >= 1 and month <= 4:
        print("SPRING")
    elif month >= 5 and month <= 8:
        print("SUMMER")
    elif month >= 9 and month <= 12:
        print("FALL")
    else:
        print("Error")

if __name__ == "__main__":
    main()