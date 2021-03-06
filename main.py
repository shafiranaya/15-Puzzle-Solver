
import copy
from heapq import heapify, heappop, heappush
from Node import Node

# Asumsi: susunan_akhir itu terurut
susunan_awal = [[1,3,4,15],[2,0,5,12],[7,6,11,14],[8,9,10,13]]
# Note: kalau target, 0 nya itu jadi 16
# susunan_akhir = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
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
    if (total % 2 == 0):
        reachable = True
    else:
        reachable = False
    return reachable

def get_direction(i,j):
    dictionary = {"up":[-1,0],"right":[0,1],"down":[1,0],"left":[0,-1]}
    key_list = list(dictionary.keys())
    val_list = list(dictionary.values())
    delta = [i,j]
    direction = val_list.index(delta)
    return key_list[direction]

def get_child_nodes(node):
    children = []
    i_old, j_old = node.get_coordinate_by_value(0)
    # deltas priority: up, right, down, left
    deltas = [[-1,0],[0,1],[1,0],[0,-1]]
    for delta in deltas:
        i = delta[0]
        j = delta[1]
        if i*j != 0 or i == j:
            continue
        i_new, j_new = i_old + i, j_old + j
        if (not (0 <= i_new <= 3)) or (not (0 <= j_new <= 3)):
            continue
        direction = get_direction(i,j)
        position = node.get_position()
        position[i_old][j_old] = position[i_new][j_new]
        position[i_new][j_new] = 0
        moves = node.get_moves()
        moves.append(direction)
        g = node.get_g()
        h = node.get_h()
        child = Node(position, moves, g+h)
        children.append(child)
    return children

# Coba solve
def solve(susunan_awal):
    # Cek dulu apakah solvable
    solvable = is_reachable(susunan_awal)
    if (not solvable):
        return []
    else:
        expanded = []
        queue = []
        heapify(queue)
        node = Node(susunan_awal, [], 0)
        heappush(queue,node)
        node_count = 0
        iteration = 1
        while (queue):
            current_node = heappop(queue)
            # print("--- Iterasi ke-",iteration,"---")
            # current_node.print_node()
            iteration += 1
            if (current_node.get_g() == 0):
                # print("Goal ketemu")
                # print("Queue length: ",len(queue))
                # print("Simpul yang dibangkitkan",node_count)
                solution = current_node.get_moves()
                return solution, node_count # return list of moves
            children = get_child_nodes(current_node)
            for child in children:
                child_position = child.get_position()
                if child_position in expanded:
                    continue
                heappush(queue, child)
                expanded.append(child_position)
                node_count += 1
        return None

# # Command line print
# def print_solution(node, moves):
#     i = 1
#     for direction in moves:
#         print("Step "+str(i)+": "+ direction)
#         node.move(direction)
#         node.print_position()
#         i+=1

def convert_matrix_to_list(matrix):
    new_list = []
    for i in range(4):
        for j in range(4):
            new_list.append(matrix[i][j])
    return new_list

# Range: 0-15
def is_out_of_range(matrix):
    new_list = convert_matrix_to_list(matrix)
    # count_out_of_range = new_list.count(matrix[i][j])
    for i in range(4):
        for j in range(4):
            if (matrix[i][j] < 0 or matrix[i][j] > 15):
                return True
    return False

def is_not_unique(matrix):
    count_list = []
    new_list = convert_matrix_to_list(matrix)
    for i in range(16):
        count_list.append(new_list.count(i))
    for count in count_list:
        if count != 1:
            return True 
    return False

def is_valid(matrix):
    return (not is_out_of_range(matrix)) and (not is_not_unique(matrix))