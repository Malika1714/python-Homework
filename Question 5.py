str1 = input("Enter a string: ")
file_name = "string.txt"
with open(file_name, "w") as file:
    file.write(str1)
print("The string has been written to the file.")