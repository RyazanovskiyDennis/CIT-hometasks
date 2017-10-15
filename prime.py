import math

n = int(input("Вывод простых чисел до числа (включительно): "))
a = [True] * n
for i in range(2,math.ceil(math.sqrt(n))+1):
    print('i = ', i)
    if a[i-1]:
        for j in range(i * 2, n+1, i):
            print('\tj = ', j)
            a[j-1] = False
b = [i for i in range(2, n+1) if a[i-1]]
print(b)
