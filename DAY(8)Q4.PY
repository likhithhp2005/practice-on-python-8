# Using Iterative Division

n = 45
i = 2
res = -1

while i * i <= n:
    while n % i == 0:
        res = i
        n //= i
    i += 1

if n > 1:
    res = n

print(res)