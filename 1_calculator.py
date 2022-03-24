str_first_number: str = input("Enter first number:")
first_number: float = float(str_first_number)

str_second_number: str = input("Enter second number:")
second_number: float = float(str_second_number)

operation: chr = input("Enter operation(/ + / - / * / / /):")

result: float
if operation == '+':
    result = first_number + second_number
elif operation == '-':
    result = first_number - second_number
elif operation == '*':
    result = first_number * second_number
elif operation == '/':
    result = first_number / second_number
else:
    print("Incorrect input")
    exit()

print(result)