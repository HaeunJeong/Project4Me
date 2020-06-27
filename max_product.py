def max_product(left_cards, right_cards):
    max_value = 0
    for l in left_cards:
        for r in right_cards:
            if max_value < l*r:
                max_value = (l*r) 
    return max_value
    
# 테스트
print(max_product([1, 6, 5], [4, 2, 3]))
print(max_product([1, -9, 3, 4], [2, 8, 3, 1]))
print(max_product([-1, -7, 3], [-4, 3, 6]))