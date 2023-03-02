from random import randint
with open("E:\Prima.txt","r") as file:
    edges = file.readlines()

N = int(edges[0])
del edges[0]
#создание массива из файла
edges = [[int(n) for n in x.split()] for x in edges]

summa = 0
k = 0 #для упрощения
maxim = [0]*N
minim = set()
used_ver = set()

x = randint(1, N)
used_ver.add(x)
print(x)

#поиск максимального числа в массиве
for i in range (N):
    #print(edges[i])
    maxim[i] = max(edges[i])

#исключение 0 из массива
for i in range (N):
    for j in range (N):
        if edges[i][j] == 0:
            edges[i][j] = max(maxim)

while k < N:
    minim.clear()
    for l in range (N):
        if l+1 in used_ver:
            minim.add(min(edges[l]))
    for i in range (N):
        for j in range (N):
            if i+1 in used_ver and edges[i][j] == min(minim) and not(j+1 in used_ver):
                summa += edges[i][j]
                edges[i][j] = max(maxim)
                edges[j][i] = max(maxim)
                used_ver.add(j+1)
                break
            elif i+1 in used_ver and edges[i][j] == min(minim) and j+1 in used_ver:
                edges[i][j] = max(maxim)
                edges[j][i] = max(maxim)
                break
    k += 1

print(summa)
