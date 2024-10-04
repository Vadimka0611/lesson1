num1 = int(input("Enter your first number: "))

while True:
    num2 = int(input("Enter your second number: "))
    if num2 == 0:
        print("You can't divide by 0! Try again.")
    else: break

result1 = num1 + num2
result2 = num1 - num2
result3 = num1 * num2
result4 = num1 / num2

print(f"{num1} + {num2} = {result1}")
print(f"{num1} - {num2} = {result2}")
print(f"{num1} * {num2} = {result3}")
print(f"{num1} / {num2} = {result4}")