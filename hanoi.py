def move_disk(disk_num, start_peg, end_peg):
    print("%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동" % (disk_num, start_peg, end_peg))

def hanoi(num_disks, start_peg, end_peg):
    if num_disks == 0:
        return
    else:
        other_peg = 6 - start_peg - end_peg
        
        # 1. 가장 큰 원판을 제외하고 나머지 원판들을 start_peg에서 other_peg로 이동
        hanoi(num_disks - 1, start_peg, other_peg)
        
        # 2. 가장 큰 원판을 start_peg에서 end_peg로 이동
        move_disk(num_disks, start_peg, end_peg)
        
        # 3. 나머지 원판들을 other_peg에서 end_peg로 이동
        hanoi(num_disks - 1, other_peg, end_peg)
    

# 테스트 코드 (포함하여 제출해주세요)
#hanoi(1, 1, 3)
hanoi(2, 1, 3)
#hanoi(3, 1, 3)