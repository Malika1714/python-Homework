def string_to_char_list(string):
    """
    This function converts a string into a list of its characters.

    Parameters:
    string (str): The string to convert.

    Returns:
    list: A list of characters in the string.
    """
    return list(string)

# Example usage
string = "Hello, world!"

# Convert the string to a list of its characters
char_list = string_to_char_list(string)
print(f"The list of characters is: {char_list}")
