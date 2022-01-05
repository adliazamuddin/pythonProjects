#Formula:
#   days = years × 365.2425 
#   weeks = years × 52.1775
#   months = years × 12 

age =int(input("Enter your current age: "))

expected_to_live = 90
days_formula = 365.2425
weeks_formula = 52.1775
months_formula = 12

age_days = (expected_to_live * days_formula) - (age * days_formula)
age_weeks = (expected_to_live * weeks_formula) - (age * weeks_formula)
age_months = (expected_to_live * months_formula) - (age * months_formula)

result_days = round(age_days)
result_weeks = round(age_weeks)
result_months = age_months

print(f"You have {result_days} days , {result_weeks} weeks and {result_months} months left.")

