def get_receiver_top_orders(heights):
    answer = [0] * len(heights)
    n = len(heights)

    for i in range(n-1, 0, -1):
        for j in range(i-1, -1, -1):
           if heights[i] <= heights[j]:
                answer[i] = j+1
                break

    return answer

print(get_receiver_top_orders([6,9,5,7,4]))