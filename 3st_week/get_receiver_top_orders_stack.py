def get_receiver_top_orders_stack(heights):
    #if heights  == heights.isEmpty() == while heights
    answer = [0] * len(heights)

    while heights:
        height = heights.pop()
        #pop = 4
        #[6,9,5,7]
        n = len(heights)
        for i in range(n-1, -1, -1):
            print(i)
            if heights[i] >= height:
                answer[len(heights)] = i
                break

    return answer

print(get_receiver_top_orders_stack([6,9,5,7,4]))