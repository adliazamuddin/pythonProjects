height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

result = int(weight) / float(height) ** 2

result_int = int(result)

print(result_int)