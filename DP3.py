#가능한 최대 수익을 리턴시켜 주는 함수 max_profit_memo를 Memoization 방식으로 작성해 보세요. 
# cache[count] : 새콤달콤이 count일 때 최대 수익
# print_list[count] : count개 살때 새콤달콤 판매가격

def max_profit_memo(price_list, count, cache):
    if count > len(price_list)-1:
        max = max_profit_memo(price_list,count-len(price_list)+1, cache) + max_profit_memo(price_list,len(price_list)-1, cache)
    else:
        max = price_list[count]

    if cache.get(count) is not None:
        #print(f"cache[{count}]: {cache[count]}")
        return cache[count]

    for i in range(1,count):
        if max < cache[i] + max_profit_memo(price_list, count-i,cache):
            max = cache[i] + cache[count-i]
    
    cache[count] = max
    #print(f"cache[{count}]: {cache[count]}")
    return cache[count]


    
def max_profit(price_list, count):
    max_profit_cache = {}
    max_profit_cache[0] = price_list[0]
    max_profit_cache[1] = price_list[1]

    return max_profit_memo(price_list, count, max_profit_cache)


# 테스트
print(max_profit([0, 100, 400, 800, 900, 1000], 5))
print(max_profit([0, 100, 400, 800, 900, 1000], 10))
print(max_profit([0, 100, 400, 800, 900, 1000, 1400, 1600, 2100, 2200], 9))
