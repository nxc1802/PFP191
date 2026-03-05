class Teacher:
    def __init__(self, name, age, class_info):
        self.name = name
        self.age = int(age)
        self.class_info = class_info
    
    def __str__(self):
        return f"{self.name}\n{self.age}\n{self.class_info}"

class Professor(Teacher):
    def __init__(self, name, age, class_info, address):
        super().__init__(name, age, class_info)
        self.__address = address
    
    def get_address(self):
        return self.__address
    
    def set_address(self, address):
        self.__address = address
        
    def display_info(self):
        print("OUTPUT")
        print(f"Age: {self.age}")
        print(f"Class: {self.class_info}")
        print(f"Name: {self.name}")
        print(f"Address: {self.__address}")

def input_teachers():
    n = int(input("Enter the number of teachers: "))
    teachers = []
    for i in range(1, n + 1):
        print(f"Enter teacher {i}")
        name = input("Enter name: ")
        age = input("Enter age: ")
        c_info = input("Enter class: ")
        teachers.append(Teacher(name, age, c_info))
    return teachers

def main():
    teachers = []
    while True:
        try:
            print("Your selection (1 -> 4): ", end="")
            line = input().strip()
            if not line: break
            choice = line
            
            if choice == "1":
                teachers = input_teachers()
                print("OUTPUT")
                for i, t in enumerate(teachers, 1):
                    print(f"Teacher {i}")
                    print(t)
            
            elif choice == "2":
                # Sort by decreasing age
                teachers.sort(key=lambda x: x.age, reverse=True)
                print("OUTPUT")
                for i, t in enumerate(teachers, 1):
                    print(f"Teacher {i}")
                    print(t)
                    
            elif choice == "3":
                # Filter class starts with SE and sort by name
                filtered = [t for t in teachers if t.class_info.startswith("SE")]
                filtered.sort(key=lambda x: x.name)
                print("OUTPUT")
                for i, t in enumerate(filtered, 1):
                    print(f"Teacher {i}")
                    print(t)
            
            elif choice == "4":
                name = input("Enter name: ")
                age = input("Enter age: ")
                c_info = input("Enter class: ")
                address = input("Enter address : ")
                prof = Professor(name, age, c_info, address)
                prof.display_info()
                
            print("FINISH")
        except EOFError:
            break

if __name__ == "__main__":
    main()
