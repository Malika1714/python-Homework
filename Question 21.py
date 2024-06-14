def count_occurence(list1,num):
    count = 0
    for ele in list1:
        if ele == num:
            count += 1
    return count
numbers_list = [1,2,3,2,5,3,2,2,2]
element_count = 2
count = count_occurence(numbers_list,element_count)
print("The element",element_count,"occurs",count,"times in list.")