def highestPowerOf2(n):
    return (n & ( ~(n-1)))
n=24
print(highestPowerOf2(n))
