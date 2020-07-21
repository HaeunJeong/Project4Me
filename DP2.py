def fib_tab(n):
    cache = {}
    for i in range(1,n+1):
        #print(i)
        if i<3:
            cache[i] = 1
        else:
            cache[i] = cache[i-1]+cache[i-2]
    
    return cache[n]

def fib_tab2(n):
    fib_table = [0,1,1] #0번쨰, 1번째, 2번째 값 저장
    for i in range(3,n+1):
        fib_table.append(fib_table[i-1]+fib_table[i-2])
    return fib_table[n]

def fib_optimized(n):
    c = 1
    p = 1
    for i in range(3,n+1):
        c,p = c+p, c
       # temp = c
       # c = c+p
       # p = temp
    return c

# 테스트
print(fib_optimized(10))
print(fib_optimized(56))
print(fib_optimized(132))