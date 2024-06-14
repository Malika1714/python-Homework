def sum_of_digits(number):
    number_str= str(number)
    total = 0
    for digit in number_str:
        total+= int(digit)
    return total
number = int(input("Enter a number: "))
sum_digits = sum_of_digits(number)
print("The sum of digits of",number,"is",sum_digits)


