def highestPowerOf2(n):
    return (n & ( ~(n-1)))
n=int(input())
print(highestPowerOf2(n))
