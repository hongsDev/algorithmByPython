def is_palindrome(string):

    start_num  = 0
    end_num = len(string)

    while start_num < end_num:
        print(string[start_num] )
        print(string[end_num-1])
        if string[start_num] == string[end_num-1]:
            start_num += 1
            end_num -= 1
        else:
            return False

    return True

input = "abcaa"
print(is_palindrome(input))

