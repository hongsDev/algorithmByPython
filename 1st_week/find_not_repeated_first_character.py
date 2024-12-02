def find_not_repeated_first_character(arr):

    for char in arr:
        is_repeated = False
        for compareChar in arr:
            if(char == compareChar):
                is_repeated = True

        if(is_repeated == False):
            return char

    return "-"


result = find_not_repeated_first_character
print(result("asdfa"))

