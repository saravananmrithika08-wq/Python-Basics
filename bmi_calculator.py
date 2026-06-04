# BMI Calculator 
# Mrithika - Biomedical Engineering Student 
# BMI is widely used in clinincal settings to assess bodu weight status 

def calculate_bmi(weight_kg, height_m):
  bmi = weight_kg / (height_m ** 2)
  return round(bmi, 2)

def interpret_bmi(bmi):
  if bmi < 18.5:
    return "Underweight"
  elif 18.5 <= bmi < 24.9:
    return "Normal weight"
  elif 25 <= bmi < 29.9:
    return "Overweight"
  else:
    return "Obese"

# --- Main Progress ---
print("=== Clinical BMI Calculator ===")
weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

bmi = calculate_bmi(weight, height)
category = interpret_bmi(bmi)

print(f"\nYour BMI: {bmi}")
print(f"Category: {category}")
