def get_receiver_top_orders_stack(heights):
    #if heights  == heights.isEmpty() == while heights
    answer = [0] * len(heights)

    while heights:
        height = heights.pop()
        for i in range(len(heights)-1, 0, -1):
            if heights[i] >= height:
                answer[len(heights)] = i+1
                break

    return answer

print(get_receiver_top_orders_stack([6,9,5,7,4]))