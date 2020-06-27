# 제곱근 사용을 위한 sqrt 함수
from math import sqrt

# 두 매장의 직선 거리를 계산해 주는 함수
def distance(store1, store2):
    return sqrt((store1[0] - store2[0]) ** 2 + (store1[1] - store2[1]) ** 2)

# 가장 가까운 두 매장을 찾아주는 함수
def closest_pair(coordinates):
    min = 100000
    result = []
    for t1 in coordinates[:len(coordinates)-1]:
        #print(f't1 : {t1}')
        for t2 in coordinates[coordinates.index(t1)+1:len(coordinates)]:
            #print(f't2: {t2}')
            if min > distance(coordinates[coordinates.index(t1)],coordinates[coordinates.index(t2)]):
                min = distance(coordinates[coordinates.index(t1)],coordinates[coordinates.index(t2)])
                result = []
                result.append(t1)
                result.append(t2)
    
    return result
    

# 테스트
test_coordinates = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
print(closest_pair(test_coordinates))