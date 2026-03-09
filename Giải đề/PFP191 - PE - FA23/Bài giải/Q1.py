# Q1 (4 marks): BMI Calculator with Unit Conversion

# 1. Input a positive decimal number
def input_positive_decimal():
    while True:
        try:
            n = float(input("Enter a positive decimal number: "))
            if n > 0:
                return n
            else:
                print("Invalid input. Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a positive number.")


# 2. Convert weight from pounds to kilograms
def pounds_to_kg(weight):
    return weight * 0.453592


# 3. Convert height from inches to meters
def inches_to_meters(height):
    return height * 2.54 / 100


# 4. BMI calculator
def bmi_calculator():
    unit = input("Enter unit system (SI for kg/m, imperial for lb/inches): ").strip().lower()

    if unit == "si":
        weight = input_positive_decimal()   # kg
        height = input_positive_decimal()   # m
    else:
        weight_lb = input_positive_decimal()
        height_in = input_positive_decimal()
        weight = pounds_to_kg(weight_lb)
        height = inches_to_meters(height_in)

    bmi = weight / (height ** 2)
    print(f"BMI = {bmi:.2f}")

    if bmi < 18.5:
        print("Classification: Underweight")
    elif bmi < 25.0:
        print("Classification: Normal weight")
    elif bmi < 30.0:
        print("Classification: Overweight")
    else:
        print("Classification: Obese")


bmi_calculator()
