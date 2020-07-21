
#memoization
def fib_memo(n, cache):
    if cache.get(n) is not None:
        return cache.get(n)
    
    if n==1 or n==2:
        cache[n] = 1
        return cache[n]
    else:
        cache[n] = fib_memo(n-1, cache) + fib_memo(n-2, cache)
        return cache[n]
    
def fib(n):
    fib_cache = {}
    return fib_memo(n, fib_cache)

# 테스트
print(fib(10))
print(fib(50))
print(fib(100))