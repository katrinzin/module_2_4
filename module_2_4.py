numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
a = len(numbers)

for i in range(a):
    delit = 0
    if numbers[i] <= 1:
        continue

    for j in range(1, i):
        if numbers[i] % j == 0:
            delit +=1
    if delit > 1:
        not_primes.append(numbers[i])
    else:
        primes.append(numbers[i])

print('primes', primes)
print('not primes', not_primes)