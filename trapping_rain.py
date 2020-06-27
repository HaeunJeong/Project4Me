def trapping_rain(buildings):
    result=0
    for i in range(1,len(buildings)-1):
        left_highest_index = max([x for x in buildings[:i]] or [0])
        right_highest_index = max([x for x in buildings[i:]] or [0])
        #print(i, left_highest_index, right_highest_index)
        #print(min(left_highest_index, right_highest_index)-buildings[i])
        rain = min(left_highest_index, right_highest_index)-buildings[i]
        result +=  rain if rain>0 else 0
    return result

# 테스트
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))