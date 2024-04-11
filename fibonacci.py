# -*- coding: utf-8 -*-



import time


def fib1(n):
    """Fib with recursion."""

    # base case
    if n==0 or n==1:
        return 1
    # recurssive caae
    else:
        return fib1(n-1) + fib1(n-2)


def fib2(n):
    """Fib without recursion."""
    a, b = 0, 1
    for i in range(1, n+1):
        a, b = b, a+b
    return b


def fib3(n, cache = {0: 1, 1: 1}):
    """Fib with recursion and caching."""
    try:
        return cache[n]
    except KeyError:
        cache[n] = fib3(n-1) + fib3(n-2)
        return cache[n]



if __name__ == '__main__':
    test_n = 30
    
    start_time = time.time()
    print(fib1(test_n))
    exec_time = time.time() - start_time
    print("运行函数fib1耗时:%.4f秒！！！"%(exec_time))
    
    # 运行函数fib1耗时:0.3989秒！！！
            
    start_time = time.time()
    print(fib2(test_n))
    exec_time = time.time() - start_time
    print("运行函数fib2耗时:%.4f秒！！！"%(exec_time))    
    
    # 运行函数fib2耗时:0.0000秒！！！

    start_time = time.time()
    print(fib3(test_n))
    exec_time = time.time() - start_time
    print("运行函数fib3耗时:%.4f秒！！！"%(exec_time))
    
    # 运行函数fib2耗时:0.0000秒！！！




