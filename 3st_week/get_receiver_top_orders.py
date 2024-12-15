def get_receiver_top_orders(array):
    answer = [0] * len(array)
    n = len(array)

    for i in range(n-1, 0, -1):
        for j in range(i - 1, -1, -1):
            print(i, j)
            if array[i] <= array[j]:
                answer[i] = j+1
                break

#0 1 2 3 4
#0 1 2 3
#0 1 2
#0 1
#0

    return answer

print(get_receiver_top_orders([6,9,5,7,4]))