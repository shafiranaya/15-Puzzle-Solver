
import copy
from heapq import heapify, heappop, heappush
from Node import Node


# Asumsi: susunan_akhir itu terurut
susunan_awal = [[1,3,4,15],[2,0,5,12],[7,6,11,14],[8,9,10,13]]
# Note: kalau target, 0 nya itu jadi 16
susunan_akhir = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
jawaban = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]

def find_X(susunan):
    for i in range(4):
        for j in range(4):
            # Sel kosong pada posisi awal
            if (susunan[i][j] == 0):
                # Sel yang diarsir
                if ((i%2==0 and j%2==1) or (i%2==1 and j%2==0)):
                    X = 1
                # Sel putih
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

def get_direction(i,j):
    if (i == 1 and j == 0):
        move = "down"
    if (i == -1 and j == 0):
        move = "up"
    if (i == 0 and j == 1):
        move = "right"
    if (i == 0 and j == -1):
        move = "left"
    return move

# Masih bermasalah di moves
def get_child_nodes(node):
    children = []
    i_old, j_old = node.get_coordinate_by_value(0)

    # ver2: deltas
    # deltas priority: up, right, down, left
    # deltas = [[-1,0],[0,1],[1,0],[0,-1]]
    # for delta in deltas:
    #     i = delta[0]
    #     j = delta[1]

    # ver1 versi biasa
    delta = [0,-1,1]
    for i in delta:
        for j in delta:
            # prioritas gerak (-1,0,1): up, left, right, down
            # prioritas gerak (-1,1,0): up, down, left, right
            # prioritas gerak (1,0,-1): down, right, left, up
            # prioritas gerak (1,-1,0): down, up, right, left
            # prioritas gerak (0,1,-1): right, left, down, up
            # prioritas gerak (0,-1,1): left, right, up, down
            if i*j != 0 or i == j:
                continue
            i_new, j_new = i_old + i, j_old + j
            if (not (0 <= i_new <= 3)) or (not (0 <= j_new <= 3)):
                continue
            print("i,j: ",i,j,get_direction(i,j))
            move = get_direction(i,j)
            position = node.get_position()
            position[i_old][j_old] = position[i_new][j_new]
            position[i_new][j_new] = 0
            moves = node.get_moves()
            moves.append(move)
            # child_move = move
            child = Node(position, moves, g(node.position,jawaban))
            children.append(child)
    return children

# Coba solve
def solve(susunan_awal):
    queue = []
    heapify(queue)
    node = Node(susunan_awal, [], g(susunan_awal,jawaban))
    heappush(queue,node)
    iteration = 1
    while (queue):
        current_node = heappop(queue)
        if (current_node.get_g() == 0):
            print("Goal ketemu")
            # print("Solusi (position): ", current_node.get_position())
            return current_node.get_moves()
            # return moves
        children = get_child_nodes(current_node)
        for child in children:
            heappush(queue, child)
        print("--- Node ke-",iteration,"---")
        current_node.print_node()
        iteration += 1
    return None

s_1 = [[1,2,3,4],[5,6,7,8],[9,10,0,11],[13,14,15,12]]
soal = [[1,2,3,4],[5,6,0,8],[9,10,7,11],[13,14,15,12]]
# print(g(s_1,susunan_akhir))
# print("Reachable?", is_reachable(susunan_awal))
# node = Node(soal, [], g(soal,susunan_akhir))
# children_node = get_child_nodes(node)
# for child in children_node:
#     print("Child")
#     child.print_node()
# print(children_node)
print("---BATAS---")
moves = solve(soal)
# print("MOVES =",moves)
# print(find_X(susunan_awal))
# print(posisi(15,susunan_awal,susunan_akhir))
# print(kurang(15,susunan_awal,susunan_akhir))
# print(kurang(16,susunan_awal,susunan_akhir))
# def kurang(i, susunan):
