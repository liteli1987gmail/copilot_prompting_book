# 创建一个函数用来找出一定范围内的质数
def find_primes(n):
    primes = []
    for num in range(2, n + 1):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            primes.append(num)
    return primes

# 创建一个函数用来找出一定范围内的质数
# 函数接受两个参数， \
# 函数返回一个列表，列表中包含所有找到的质数。 
# 确保函数处理边缘情况。

def find_primes(n):
    if n < 2:
        return []
    primes = []
    for num in range(2, n + 1):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            primes.append(num)
    return primes