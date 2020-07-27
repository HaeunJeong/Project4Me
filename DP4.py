#Tabulation 방식
#반복문을 사용하여, 아래서부터 계산해서 올라가는 방식. 필요없는 계산까지 할 수 있지만, previous, current 2개의 값을 사용하여 공간최적화 가능
'''
가능한 최대 수익을 리턴시켜 주는 함수 max_profit을 Tabulation 방식으로 작성해 보세요. max_profit은 파라미터 두 개를 받습니다.
price_list: 개수별 가격이 정리되어 있는 리스트
count: 판매할 새꼼달꼼 개수
'''

def max_profit(price_list, count):
    # 개수별로 가능한 최대 수익을 저장하는 리스트
    # 새꼼달꼼 0개면 0원
    profit_table = [0]

    # 개수 1부터 count까지 계산하기 위해 반복문
    for i in range(1, count + 1):
        # 새꼼달꼼 i개에 대한 최대 수익을 담는 변수 profit
        if i < len(price_list):
            # i개에 대한 가격이 price_list에 있으면,
            # profit에 price_list[i]값을 넣는다
            profit = price_list[i]
        else:
            # i개에 대한 가격이 price_list에 없으면,
            # profit에 0을 넣는다
            profit = 0

        # count개를 팔 수 있는 조합들을 비교해서, 가능한 최대 수익을 찾는다
        for j in range(1, i // 2 + 1):
            profit = max(profit, profit_table[j] + profit_table[i - j])

        profit_table.append(profit)

    return profit_table[count]

    
# 테스트
print(max_profit([0, 200, 600, 900, 1200, 2000], 5))
print(max_profit([0, 300, 600, 700, 1100, 1400], 8))
print(max_profit([0, 100, 200, 400, 600, 900, 1200, 1300, 1500, 1800], 9))
