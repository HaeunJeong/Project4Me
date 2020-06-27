def merge(list1, list2):
    result = []
    if len(list1)==0 or len(list2)==0:
        return list1 if len(list1)>0 else list2

    while len(list1)>0 or len(list2)>0:
        value1 = list1[0] if len(list1)>0 else 100
        value2 = list2[0] if len(list2)>0 else 100
        result.append(min(value1, value2))
        if len(list1)>0 and min(value1, value2)==value1:
            del list1[0]
        elif len(list2)>0 and min(value1, value2)==value2:
            del list2[0]
        
    
    return result
        
    
# 테스트
print(merge([1],[]))
print(merge([],[1]))
print(merge([2],[1]))
print(merge([1, 2, 3, 4],[5, 6, 7, 8]))
print(merge([5, 6, 7, 8],[1, 2, 3, 4]))
print(merge([4, 7, 8, 9],[1, 3, 6, 10]))