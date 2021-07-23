import copy
from tkinter import *
# TODO: mungkin bikin atribut children (?) optional sih
class Node:
    def __init__(self, position, moves, cost):
        self.position = position
        self.moves  = moves # moves so far
        self.cost = cost # didapat dari fungsi g

    def get_position(self):
        return copy.deepcopy(self.position)

    def set_position(self, position):
        self.position = position

    # # Jumlah manhattan distance (jarak antara posisi saat itu dengan posisi seharusnya) ubin tidak kosong yang tidak terdapat pada susunan akhir
    def get_g(self):
        jawaban = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]
        distance = 0
        for i in range(4):
            for j in range(4):
                position = self.get_position()
                if (position[i][j] != 0):
                    position_coordinate = self.get_coordinate_by_value(position[i][j])
                    solution_coordinate = self.get_coordinate_by_value(jawaban[i][j])
                    i1, j1 = position_coordinate
                    i2, j2 = solution_coordinate
                    distance += abs(i1-i2) + abs(j1-j2)
        return distance
    
    def get_h(self):
        return len(self.moves)
    
    def get_f(self):
        return self.get_g() + self.get_h()

    def get_moves(self):
        return copy.copy(self.moves)

    def get_coordinate_by_value(self, value):
        for i in range(4):
            for j in range(4):
                if value == self.position[i][j]:
                    x = i
                    y = j
        return x, y

    def __lt__(self, other):
        return self.get_f() < other.get_f()
    
    def print_position(self):
        for i in range(4):
            for j in range(4):
                print(self.position[i][j], end="\t")
            print()

    # def position_gui(self, parent):
    #     position_frame = Frame(parent, width = 312, height = 272.5, bg = "grey")
    #     position_frame.pack()
    #     numbers = [[0 for i in range(4)] for j in range(4)]
    #     for i in range(4):
    #         for j in range(4):
    #             numbers[i][j] = Label(btns_frame, text=str(self.position[i][j]), width=5, height=3, bd=0, bg="#fff").grid(row=i, column=j,padx=1,pady=1)
    #     return position_frame
    
    def print_node(self):
        # print("-----NODE-----")
        print("Position: ")
        self.print_position()
        print("Moves so far: ", self.moves)
        if (self.moves):
            print("Prev move: ", self.moves[-1])
        print("Cost (nilai g): ",self.get_g())
        print("Heuristic: ",self.get_h())
        print("nilai f:",self.get_f())

    # untuk move sesuai langkah (ganti posisi)
    def move(self,direction):
        dictionary = {"up":[-1,0],"right":[0,1],"down":[1,0],"left":[0,-1]}
        delta = dictionary[direction]
        i = delta[0]
        j = delta[1]
        i_old, j_old = self.get_coordinate_by_value(0)
        position = self.get_position() 
        i_new, j_new = i_old + i, j_old + j
        position[i_old][j_old] = position[i_new][j_new]
        position[i_new][j_new] = 0
        self.position = position