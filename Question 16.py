def count_char(input_string):
    frequency_dict = {}
    for char in input_string:
        if char in frequency_dict:
            frequency_dict[char] += 1
        else:
            frequency_dict[char] = 1
    return frequency_dict
input_string = input("Enter your sentence: ")
frequency = count_char(input_string)
print(frequency)