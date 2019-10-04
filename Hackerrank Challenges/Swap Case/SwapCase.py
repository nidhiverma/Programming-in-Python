def swap_case(s):
    new_string = ""
    for char in s:
        if char.isupper():
             new_string += char.lower()
        elif char.islower():
            new_string += char.upper()
        else:
            new_string += char
    return new_string
