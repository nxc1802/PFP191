def input_positive_decimal():
    while True:
        try:
            n = int(input("Enter a positive decimal number: "))
            if n <= 0: print("Please input a positive decimal!")
            else: return n
        except:
            print("Please input a positive decimal!")

def pounds_to_kg(weight):
    return weight * 0.453592

def inches_to_meters(height):
    return height * 2.54 / 100

def calculate_BMI():
    n = input("You want to input yout weight and height in SI units or Imperial units:\n0. SI Units (default)\n1. Imperial Units\n")
    if n == "1":
        weight = int(input("Input your weight (lbs): "))
        height = int(input("Input your height (inches): "))
        weight = pounds_to_kg(weight)
        height = inches_to_meters(height)
    elif n == "0":
        weight = int(input("Input your weight (kg): "))
        height = int(input("Input your height (m): "))
    
    bmi = weight / (height ** 2)
    print(f"Your BMI is: {bmi}, ", end = ' ')


    if bmi < 16:
        print("your class is Severe Thinness")
    elif 16 <= bmi < 17:
        print("your class is Moderate Thinness")
    elif 17 <= bmi < 18.5:
        print("your class is Mild Thinness")
    elif 18.5 <= bmi < 25:
        print("your class is Normal weight")
    elif 25 <= bmi < 30:
        print("your class is Overweight")
    elif 30 <= bmi < 35:
        print("your class is Obesity Class I")
    elif 35 <= bmi < 40:
        print("your class is Obesity Class II")
    else:
        print("your class is Obesity Class III")

