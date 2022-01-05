print("Welcome to the tip calculator.")
total_bill = input("What was the total bill? $")
bill_percent = input("What percentage tip would you like to give? 10,12, or 15? ")
people = input("How many people to splt the bill? ")

result = (float(total_bill) / int(people)) * (1.0 + (int(bill_percent)/100))

# result_round = round(result,2)

#result get 2 decimal point with 0
result_final = "{:.2f}".format(result)

print(f"Each person should pay: ${result_final}")