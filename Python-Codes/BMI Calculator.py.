# BMI Calculator - Height in feet only
# Input from user
weight = float(input("Enter your weight in kilograms (kg): "))
height_feet = float(input("Enter your height in feet (e.g., 5.5 for 5 feet 6 inches): "))
# Convert height to meters (1 foot = 0.3048 meters)
height_meters = height_feet * 0.3048
# BMI calculation
bmi = weight / (height_meters ** 2)
# Display BMI
print(f"\nYour BMI is: {bmi:.2f}")
# BMI categories
if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 24.9:
    print("You have a normal weight.")
elif 25 <= bmi < 29.9:
    print("You are overweight.")
else:
    print("You are obese.")
