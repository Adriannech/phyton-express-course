print("Description: This program will divide 2 numbers")

stop_word = "stop"


while True:
    num1 = input("Enter first number:")
    if num1 == stop_word:
        exit(0)
    num2 = input("Enter second number:")
    if num2 == stop_word:
        exit(0)

    try:
        try:
            num1 = float(num1)
        except ValueError as e:
            raise ValueError("Error: First number is not valid a number")
        try:
            num2 = float(num2)
        except ValueError as e:
            raise ValueError("Error: Second number is not a valid number")
        print("Result :" + str(num1 / num2))
    except ValueError as e:
        print (str(e))
    except ZeroDivisionError as e:
        print("Error: division by zero")
