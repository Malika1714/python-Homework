def calculator(num1,num2):
    print("Calculator: ")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice = input("Enter your choice: ")
    if choice == '1':
        sum = num1+num2
        print("Addition of two numbers is: ",sum)
    elif choice == '2':
        diff = num1-num2
        print("Subtraction of two numbers is: ",diff)
    elif choice == '3':
        multiply = num1*num2
        print("Multiplication of the two numbers is: ",multiply)
    elif choice == '4':
        div = num1 / num2
        print("Division of two numbers is: ",div)
    else:
        print("Invalid choice")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter secomd number: "))
calculator(num1,num2)