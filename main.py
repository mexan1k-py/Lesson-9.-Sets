#Homework 1
a = int(input('Введите количество элементов: '))

b = list(map(int, input().split()))[:a]

c = set(b)

print(len(c))

#Homework 2
a1 = set(input().split())

b1 = set(input().split())

print(len(a1.intersection(b1)))

#Homework 3
a2 = set()

for i in input().split():
    if i not in a2:
        a2.add(i)
        print('No')
    else:
        print('Yes')