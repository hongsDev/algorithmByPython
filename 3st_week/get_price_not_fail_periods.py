from collections import deque
prices = [1, 2, 3, 2, 3]

def get_price_not_fall_periods(prices):
    # 이 부분을 채워주
    result = [0] * len(prices)
    n = len(prices)

    for i in range(0, n-1, 1):
        time = 0
        for j in range(i+1, n, 1):
            if prices[i] <= prices[j]:
                time += 1
            else:
                time += 1 #문제 요구상 가격이 떨어 졌을 때 까지도 1초로 계산을 해야함
                break
        result[i] = time

    return result

print(get_price_not_fall_periods(prices))
print("정답 = [4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods(prices))
print("정답 = [6, 2, 1, 3, 2, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods([3, 9, 9, 3, 5, 7, 2]))
print("정답 = [6, 1, 4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods([1, 5, 3, 6, 7, 6, 5]))