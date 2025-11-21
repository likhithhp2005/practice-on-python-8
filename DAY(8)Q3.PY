# Python Program to Print all Prime Factors of a given Number
# Using Sieve of Eratosthenes
n = 315
spf = [0 for _ in range(n + 1)]  # Smallest Prime Factor array
spf[1] = 1

for i in range(2, n + 1):
    spf[i] = i

for i in range(4, n + 1, 2):
    spf[i] = 2

for i in range(3, int(n ** 0.5) + 1, 2):
    if spf[i] == i:
        for j in range(i * i, n + 1, i):
            if spf[j] == j:
                spf[j] = i

while n != 1:
    print (spf[n])
    n //= spf[n]