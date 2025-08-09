n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

while True:
    option = input("Select Operation (1.Add, 2.Subtract, 3.Multiply, 4.Divide): ")

    if option == "1":
        print("Answer:", n1 + n2)
        break
    elif option == "2":
        print("Answer:", n1 - n2)
        break
    elif option == "3":
        print("Answer:", n1 * n2)
        break
    elif option == "4":
        if n2 != 0:
            print("Answer:", n1 / n2)
        else:
            print("Error: Division by zero not allowed.")
        break
    else:
        print("Invalid option, please try again.")
