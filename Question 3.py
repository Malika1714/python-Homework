factorial = 1
num = int(input("Enter number: "))
if num<0 :
    print("Factorail not possible")
elif num == 0:
    print("Factorial is one")
else:
    for i in range(1,num+1):
        factorial = factorial*i
    print("The factorail of",num,"is",factorial)