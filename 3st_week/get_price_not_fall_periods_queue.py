from collections import deque
prices = [1, 2, 3, 2, 3]
def get_price_not_fall_periods_queue(prices):
    prices_queue = deque(prices)
    result = [0] * len(prices)
    idx = 0
    while prices_queue:
        price = prices_queue.popleft()
        time = 0
        for i in prices_queue:
            if price <= i:
                time += 1
            else:
                time += 1
                break

        result[idx] = time
        idx += 1

    return result

print(get_price_not_fall_periods_queue(prices))
print("정답 = [4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods_queue(prices))
print("정답 = [6, 2, 1, 3, 2, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods_queue([3, 9, 9, 3, 5, 7, 2]))
print("정답 = [6, 1, 4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods_queue([1, 5, 3, 6, 7, 6, 5]))