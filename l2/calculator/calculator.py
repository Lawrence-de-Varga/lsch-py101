print("Welcome to Calculator.")

not_numbers = True

while not_numbers:
    number1 = input("Please enter the first number: ")
    number2 = input("Please enter the second number: ")

    try:
        int(number1)
        int(number2)

    except ValueError:
        print("Please enter two valid integers.")
        print()
    else:
        number1 = int(number1)
        number2 = int(number2)
        not_numbers = False

possible_operation = False

while not possible_operation:
    print("Which operation would you like to perform? ")
    print("1: Addition, 2: Subtraction, 3: Multiplication, 4: Division.")

    operation = input("Please enter the number corresponding to the desired operation: ")

    if operation not in ['1', '2', '3', '4']:
        print()
        print("Please enter one of these digits corresponding to the desired operation.")
        print("1, 2, 3, 4")
        print()
        continue
    else:
        possible_operation = True


match operation:
    case '1':
        print(f"Adding {number1} and {number2}.")
        print(f"{number1 + number2}")
    case '2':
        print(f"Subtracting {number2} from {number1}.")
        print(f"{number1 - number2}")
    case '3':
        print(f"Multiplying {number1} by {number2}.")
        print(f"{number1 * number2}")
    case '4':
        print(f"Dividing {number1} by {number2}.")
        print(f"{number1 / number2}")
