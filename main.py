
import copy
from heapq import heappush, heappop

# Asumsi: susunan_akhir itu terurut
susunan_awal = [[1,3,4,15],[2,0,5,12],[7,6,11,14],[8,9,10,13]]
# Note: kalau target, 0 nya itu jadi 16
susunan_akhir = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

def find_X(susunan):
    for i in range(4):
        for j in range(4):
            if (susunan[i][j] == 0):
                if ((i%2==0 and j%2==1) or (i%2==1 and j%2==0)):
                    X = 1
                else:
                    X = 0
    return X

def posisi(x, susunan_awal):
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    for row in range(4):
        for col in range(4):
            if (susunan_awal[row][col] == x):
                posisi = matrix[row][col]
    return posisi

def kurang(i, susunan_awal):
    # Banyaknya ubin bernomor j sedemikian sehingga j < i dan POSISI(j) > POSISI(i)
    count = 0
    if (i != 16):
        for row in range(4):
            for col in range(4):
                j = susunan_awal[row][col]
                posisi_j = posisi(j,susunan_awal)
                posisi_i = posisi(i,susunan_awal)
                if (j < i) and (posisi_j > posisi_i) and (j != 0):
                    # print("j = ",j)
                    count += 1
    else:
        posisi_kosong = posisi(0,susunan_awal)
        count = 16 - posisi_kosong
    return count

def is_reachable(susunan_awal):
    total = 0
    X = find_X(susunan_awal)
    for i in range (1,17):
        total += kurang(i,susunan_awal)
    total += X
    print("X =",X,"total = ",total)
    if (total % 2 == 0):
        reachable = True
    else:
        reachable = False
    return reachable

# Jumlah ubin tidak kosong yang tidak terdapat pada susunan akhir
def g(susunan_awal, susunan_akhir):
    count = 0
    for i in range(4):
        for j in range(4):
            if (susunan_awal[i][j] != 0):
                if susunan_awal[i][j] != susunan_akhir[i][j]:
                    count += 1
    return count


s_1 = [[1,2,3,4],[5,6,7,8],[9,10,0,11],[13,14,15,12]]
print(g(s_1,susunan_akhir))
print("Reachable?", is_reachable(susunan_awal))
# print(find_X(susunan_awal))
# print(posisi(15,susunan_awal,susunan_akhir))
# print(kurang(15,susunan_awal,susunan_akhir))
# print(kurang(16,susunan_awal,susunan_akhir))
# def kurang(i, susunan):
