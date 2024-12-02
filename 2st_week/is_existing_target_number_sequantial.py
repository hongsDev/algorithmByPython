def is_exist_targer_number_binary(arr, target):
    min_number = 0
    max_number = len(arr) -1
    current_num = (min_number + max_number) // 2

    print(min_number , max_number)

    while min_number <= max_number:
        if arr[current_num] == target:
            return True
        elif arr[current_num] > target:
            max_number = current_num -1
        elif arr[current_num] < target:
            min_number = current_num + 1

        current_num = (min_number + max_number) // 2


print(is_exist_targer_number_binary([1,2,4,5,6,7,8,10,11,28, 50], 222))








