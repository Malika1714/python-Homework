total = 0
list1 = []
n= int(input("Enter number of elements: "))
for i in range(0,n):
    ele = int(input("Enter the numbers: "))
    list1.append(ele)
print(list1)
for ele in range(0,len(list1)):
    total = total + list1[ele]
print("sum of all elements is: ", total)
