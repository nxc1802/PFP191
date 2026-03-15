def main():
    string_input = input("Enter a string: ")
    list_input = string_input.split()
    list_input.reverse()
    print(" ".join(list_input))

if __name__ == "__main__":
    main()