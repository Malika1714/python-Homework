punctuations = '''!()-[]{}:;'"\,<>.?/@#$%^&*_~'''
str1 = input("Enter the string: ")
no_punct = ""
for char in str1:
    if char not in punctuations:
        no_punct = no_punct + char
print(no_punct)
