# 두 요소의 위치를 바꿔주는 helper function
def swap_elements(my_list, index1, index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp
    return my_list


# 퀵 정렬에서 사용되는 partition 함수
#my_list의 값들을 pivot 기준으로 재배치한 후, pivot의 최종 위치 인덱스를 리턴해야 합니다.
def partition(my_list, start, end):
    p = end
    b = start
    #range(n) 은 0~n-1 index까지 생성되므로, n-2 index까지 가려면, len()-1 만 하면됨.
    # 작은애들    큰애들    P
    #|-------|---------|-|  로 정렬이 되어야함.
    for i in range(len(my_list)-1):
        if my_list[i] < my_list[p]:
            swap_elements(my_list, b, i)
            b=b+1
    swap_elements(my_list,b,p)
    p=b
    return p


# 테스트 1
list1 = [4, 3, 6, 2, 7, 1, 5]
pivot_index1 = partition(list1, 0, len(list1) - 1)
print(list1)
print(pivot_index1)

# 테스트 2
list2 = [6, 1, 2, 6, 3, 5, 4]
pivot_index2 = partition(list2, 0, len(list2) - 1)
print(list2)
print(pivot_index2)
