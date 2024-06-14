def check_prefix_suffix(string, prefix, suffix):
    """
    This function checks if the string starts with the given prefix or ends with the given suffix.

    Parameters:
    string (str): The string to check.
    prefix (str): The prefix to check for.
    suffix (str): The suffix to check for.

    Returns:
    bool: True if the string starts with the prefix or ends with the suffix, False otherwise.
    """
    return string.startswith(prefix) or string.endswith(suffix)


string = "Hello, world!"
prefix = "Hello"
suffix = "world!"


result = check_prefix_suffix(string, prefix, suffix)
print(f"Does the string start with '{prefix}' or end with '{suffix}'? {result}")
