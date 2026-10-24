number = int(input("Enter a number: "))

if number < 0:
    print("Factorial is not defined for negative numbers")
else:
    factorial = 1
    counter = 1
    while counter <= number:
        factorial *= counter
        counter += 1
    print(f"Factorial of {number} = {factorial}")
