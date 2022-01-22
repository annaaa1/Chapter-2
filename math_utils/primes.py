def isprime(n):
    from math import sqrt
    index = int(sqrt(n))
    if n == 1:
        return False
    if n==2:
        return True
    for i in range(2, index+1):
        if n % i == 0:
            return False
    return True
    
