# Урок № 8. Списки

# Задание № 1

"""
a = int(input("число строк: "))
b = []
for i in range(a):
    c = int(input("Введи число: "))
    if (c < 1) or (c > 10001):
        print("попробуй еще раз.")
    else:
        b.append(c)
if len(b) < 10e5:
    b.reverse()
    print(*b)
else:
    print("слишком длинный список!")
   """

# Задание № 2

"""
a = int(input("число от 1 до 100000: "))
b = []
if (a < 1) or (a > 100001):
    print("попробуй еще раз!")
b = list(map(int, input("числа через пробел: ").split()))
for i in b:
    if (i < 1) or (i>10e9):
        print("нормальное число введи в следующий раз")
while len(b) > a:
    b.pop()
b.insert(0, b[-1])
b.pop()
print(b)
"""

# Задание № 3

m = int(input("грузоподъемность лодки: "))            # 1 <= m <= 10e6
c = []
d = 0                                                 # колличество лодок
if 1 <= m <= 10e6:
    n = int(input("колличество рыбаков: "))           # 1 <= n <= 100
    if 1 <= n <= 100:
        for i in range(n):
            ai = int(input("вес каждого рыбака: "))   # 1 <= ai <= m
            if 1 <= ai <= m:
                c.append(ai)
            else:
                print("Задумайтесь о здоровье!")
        # print(c)
        for i in c:
            if min(c) + max(c) <= m:
                d += 1
                c.remove(min(c))
                c.remove(max(c))

            if (len(c) >= 2) and (c[0] + c[1] <= m):
                d += 1
                c.remove(c[0])
                c.remove(c[1])
        while len(c) >= 1:
            d += 1
            c.remove(c[0])
        # print(c)
        print("минимум лодок: ", d)
    else:
        print("не верное колличество рыбаков!")
else:
    print("не верная грузоподъемность!")