def find_max_num2(arr):
    for num in arr:
        is_max = True
        for compare_num in arr:
            if num < compare_num:
                is_max = False
        if is_max:
            return num


        #hongs

print(find_max_num2([1, 0, 32, 56, 6, 7, 123123, 78, 2, 2, 324, 2, 34, 12, 31, 23, 12, 4124]))












