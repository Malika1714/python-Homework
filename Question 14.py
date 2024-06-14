lines = []
while True:
    line = input("Enter a line: ")
    if line == "":
        break
    lines.append(line)
print("All lines are: ")
for line in lines:
    print(line)
