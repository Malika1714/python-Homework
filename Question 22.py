list1=[]
n = int(input("Enter number of elements in the list: "))
for i in range(0,n):
    ele = int(input("Enter elements: "))
    list1.append(ele)
print(list1)
list_max = max(list1)
list_min = min(list1)
print("Maximum element is: ",list_max)
print("Minimum element is: ",list_min)