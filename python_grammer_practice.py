shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두", "없음."]

def is_exist_target_number_binary(order, menus):
    min_num = 0
    max_num = len(menus) -1
    target_num = (min_num + max_num)//2
    while min_num <= max_num:
        if order == menus[target_num]:
            return True
        elif order < menus[target_num]:
            max_num = target_num -1
        elif order > menus[target_num]:
            min_num = target_num + 1
        target_num = (min_num + max_num)//2

    return False


def is_available_to_order(menus, orders):
    # 이 부분을 채워보세요!
    menus.sort()
    for order in orders:
        if not is_exist_target_number_binary(order, menus):
            return False

    return True


result = is_available_to_order(shop_menus, shop_orders)
print(result)