def celsius_to_fahrenheit(celsius):
    return(celsius* 9/5) + 32
def fahrenheit_to_celsius(fahrenheit):
    return(fahrenheit - 32)* 5/9
def main():
    print("Temperature conversion")
    print("1. Celsius to fahrenheit")
    print("2. fahrenheit to celsius")
    choice = input("Choose the conversion: ")
    if choice == '1':
        celsius = float(input("Enter temperature in celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(celsius,"C is",fahrenheit,"F")
    elif choice == '2':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(fahrenheit,"F is",celsius,"C")
    else:
        print("Invalid choice")
if __name__ == "__main__":
    main()
