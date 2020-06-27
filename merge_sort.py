def merge(list1, list2):
    #print(list1, list2)
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
        
    
# shift+ option + a : multiline comment
""" print(merge([1],[]))
print(merge([],[1]))
print(merge([2],[1]))
print(merge([1, 2, 3, 4],[5, 6, 7, 8]))
print(merge([5, 6, 7, 8],[1, 2, 3, 4]))
print(merge([4, 7, 8, 9],[1, 3, 6, 10])) """


# 합병 정렬
def merge_sort(my_list):
    if len(my_list)<=1:
        return my_list
    mid = len(my_list)//2
    return merge(merge_sort(my_list[:mid]),merge_sort(my_list[mid:]))
    

# 테스트
print(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))
print(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
print(merge_sort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))
