# BMI Calculator Program

# Taking user input
name = input("Enter your name: ")
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

# Calculating BMI
bmi = weight / (height ** 2)

# Display BMI
print("\nHello", name)
print("Your BMI is:", round(bmi, 2))

# BMI Category
if bmi < 18.5:
    print("Category: Underweight")
elif 18.5 <= bmi < 24.9:
    print("Category: Normal weight")
elif 25 <= bmi < 29.9:
    print("Category: Overweight")
else:
    print("Category: Obese")
