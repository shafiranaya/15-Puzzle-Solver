
import copy
from heapq import heapify, heappop, heappush
from Node import Node

# TODO: ada berapa simpul yang dibangkitkan?
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
def misplaced(susunan_awal, susunan_akhir):
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
    deltas = [[-1,0],[0,1],[1,0],[0,-1]]
    for delta in deltas:
        i = delta[0]
        j = delta[1]

    # ver1 versi biasa
    # delta = [0,-1,1]
    # for i in delta:
    #     for j in delta:
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
        # print("i,j: ",i,j,get_direction(i,j))
        move = get_direction(i,j)
        position = node.get_position()
        position[i_old][j_old] = position[i_new][j_new]
        position[i_new][j_new] = 0
        moves = node.get_moves()
        moves.append(move)
        # child_move = move
        g = node.get_g()
        # child = Node(position, moves, g(node.get_position(),jawaban))
        child = Node(position, moves, g)
        children.append(child)
    return children

# Coba solve
def solve(susunan_awal):
    # Cek dulu apakah solvable
    solvable = is_reachable(susunan_awal)
    if (not solvable):
        return "Unsolvable"
    else:
        expanded = []
        queue = []
        heapify(queue)
        node = Node(susunan_awal, [], 0) # TODO costnya ganti ga ya (?)
        heappush(queue,node)
        node_count = 0
        iteration = 1
        while (queue):
            # print("Queue: ",queue)
            # print("Queue length: ",len(queue))
            current_node = heappop(queue)
            print("--- Iterasi ke-",iteration,"---")
            current_node.print_node()
            iteration += 1
            if (current_node.get_h() == 0): # TODO ganti
                print("Goal ketemu")
                print("Queue length: ",len(queue))
                # print("Solusi (position): ", current_node.get_position())
                print("Simpul yang dibangkitkan",node_count)
                return current_node.get_moves()
                # return moves
            children = get_child_nodes(current_node)
            for child in children:
                child_position = child.get_position()
                if child_position in expanded:
                    continue
                heappush(queue, child)
                expanded.append(child_position)
                node_count += 1
        return None

def print_solution(node, moves):
    i = 1
    for direction in moves:
        print("Step "+str(i)+": "+ direction)
        node.move(direction)
        node.print_position()
        i+=1

s_1 = [[1,2,3,4],[5,6,7,8],[9,10,0,11],[13,14,15,12]]
soal1 = [[1,2,3,4],[5,6,0,8],[9,10,7,11],[13,14,15,12]]
soal2 = [[0,2,3,4],[1,6,7,8],[5,10,11,12],[9,13,14,15]]
soal3 = [[6,5,2,4],[9,1,3,8],[10,0,7,15],[13,14,12,11]]
soal4 = [[1,9,4,8],[3,2,6,7],[13,10,11,12],[14,5,15,0]] #

puzzle2 = [[5,1,3,4],[9,2,6,7],[13,10,11,8],[0,14,15,12]]
puzzle3 = [[5,1,3,4],[9,2,6,7],[13,11,0,8],[14,10,15,12]]
puzzle4 = [[1,6,7,5],[9,3,10,2],[13,8,4,12],[14,11,15,0]]

soal_susah = [[1,9,5,6],[2,3,4,10],[7,8,13,15],[11,12,14,0]] #
# print(g(s_1,susunan_akhir))
# print("Reachable?", is_reachable(susunan_awal))
# node = Node(soal, [], g(soal,susunan_akhir))
# children_node = get_child_nodes(node)
# for child in children_node:
#     print("Child")
#     child.print_node()
# print(children_node)
print("---BATAS---")
# # SOAL 1
# m1 = misplaced(soal1,jawaban)
# ASTAR
# iterasi: 4
# simpul: 10
# steps: 3
# # SOAL 2
# m2 = misplaced(soal2,jawaban)
# ASTAR
# iterasi: 7
# simpul: 12
# steps: 6
# # SOAL 3
# m3 = misplaced(soal3,jawaban)
# BNB
# iterasi: 405
# simpul: 844
# steps: 17
# ASTAR
# iterasi: 534
# simpul: 1066
# steps: 83
# ASTAR REVISI

# # SOAL 4
# m4 = misplaced(soal4,jawaban)
# # SOAL SUSAH
# m5 = misplaced(soal_susah,jawaban)
# print(m1,m2,m3,m4,m5)

# PUZZLE 2
# ASTAR
# iterasi: 10
# simpul: 20
# steps: 9
# PUZZLE 3
# ASTAR
# iterasi: 13
# simpul: 28
# steps: 12
moves = solve(puzzle4)
print("MOVES =",moves)
node1 = Node(puzzle4, [], 0) # TODO costnya ganti ga ya (?)
print("Solusi:")
print_solution(node1, moves)

# print(find_X(susunan_awal))
# print(posisi(15,susunan_awal,susunan_akhir))
# print(kurang(15,susunan_awal,susunan_akhir))
# print(kurang(16,susunan_awal,susunan_akhir))
# def kurang(i, susunan):
