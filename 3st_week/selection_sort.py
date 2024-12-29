input = [4, 6, 2, 9, 1]
def selection_sort(array):

    n1 = len(array)
    print(n1)
    for i in range(n1-1):
        print(i)


    n = len(array)
    for i in range(n-1):
        min_idx = i
        for j in range(n-i):
            if array[min_idx] > array[j + i]:
                min_idx  =  j + i

        array[i], array[min_idx] = array[min_idx],array[i]
    return array

selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [1, 2, 4, 6, 9] / 현재 풀이 값 = ",selection_sort([4, 6, 2, 9, 1]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",selection_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",selection_sort([100,56,-3,32,44]))