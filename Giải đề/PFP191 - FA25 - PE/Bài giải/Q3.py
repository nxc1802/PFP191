class Teacher:
    def __init__(self, name, age, class_info):
        self.name = name
        self.age = age
        self.class_info = class_info
    
    def __str__(self):
        return f"{self.name}\n{self.age}\n{self.class_info}"

class Professor(Teacher):
    def __init__(self, name, age, class_info, address):
        super().__init__(name, age, class_info)
        self.address = address
    
    def display_info(self):
        print(f"Age: {self.age}\nClass: {self.class_info}\nName: {self.name}\nAddress: {self.address}")
        
    def get_info(self):
        return f"Name: {self.name}\nAge: {self.age}\nClass: {self.class_info}\nAddress: {self.address}"
    
    def set_info(self, name, age, class_info, address):
        self.name = name
        self.age = age
        self.class_info = class_info
        self.address = address

def input_teachers():
    print("Enter the number of teachers: ")
    n = int(input())
    teachers = []
    for i in range(n):
        print("Enter teacher name: ")
        name = input()
        print("Enter teacher age: ")
        age = int(input())
        print("Enter teacher class info: ")
        class_info = input()
        teachers.append(Teacher(name, age, class_info))
    return teachers

def solve_case_3():
    pass


def main():
    while True:
        try:
            print("Your selection (1 -> 4): ", end="")
            choice = input().strip()
            if not choice: break
            
            if choice == "1":
                teachers = input_teachers()
                print("OUTPUT")
                for teacher in teachers:
                    print(teacher)
            elif choice == "2":
                teachers.sort(key=lambda x: x.age, reverse=True)
                print("OUTPUT")
                for teacher in teachers:
                    print(teacher)
            elif choice == "3":
                filtered = [t for t in teachers if t.class_info.startswith("SE")]
                filtered.sort(key=lambda x: x.name)
                print("OUTPUT")
                for teacher in filtered:
                    print(teacher)
            elif choice == "4":
                name = input("Enter name: ")
                age = int(input("Enter age: "))
                class_info = input("Enter class: ")
                address = input("Enter address: ")
                prof = Professor(name, age, class_info, address)
                print("OUTPUT")
                prof.display_info()
            
            print("FINISH")
        except EOFError:
            break

if __name__ == "__main__":
    main()