import copy

# TODO: mungkin bikin atribut children (?) optional sih
class Node:
    def __init__(self, position, moves, cost):
        self.position = position
        self.moves  = moves # moves so far
        # self.current_move = current_move
        self.cost = cost # didapat dari fungsi g

    def get_position(self):
        return copy.deepcopy(self.position)

    def set_position(self, position):
        self.position = position

    # Jumlah ubin tidak kosong yang tidak terdapat pada susunan akhir
    def get_g(self):
        jawaban = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]
        count = 0
        for i in range(4):
            for j in range(4):
                if (self.get_position()[i][j] != 0):
                    if self.get_position()[i][j] != jawaban[i][j]:
                        count += 1
                        # print("i,j",i,j)
        return count

    def get_h(self):
        jawaban = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]
        distance = 0
        for i in range(4):
            for j in range(4):
                position = self.get_position()
                if (position[i][j] != 0):
                    i1 =  self.get_coordinate_by_value(position[i][j])[0]
                    j1 = self.get_coordinate_by_value(position[i][j])[1]
                    i2 = self.get_coordinate_by_value(jawaban[i][j])[0]
                    j2 = self.get_coordinate_by_value(jawaban[i][j])[1]
                    distance += abs(i1-i2) + abs(j1-j2)
        return distance
        # return len(self.moves)
    
    def get_heuristic_distance(self):
        jawaban = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]
        distance = 0
        for i in range(4):
            for j in range(4):
                position = self.get_position()
                if (position[i][j] != 0):
                    i1 = self.get_coordinate_by_value(position[i][j])[0]
                    j1 = self.get_coordinate_by_value(position[i][j])[1]
                    i2 = self.get_coordinate_by_value(jawaban[i][j])[0]
                    j2 = self.get_coordinate_by_value(jawaban[i][j])[1]
                    distance += abs(i1-i2) + abs(j1-j2)
        return distance
    
    def get_f(self):
        return self.get_g() + self.get_h()

    def get_moves(self):
        return copy.copy(self.moves)
    
    # def add_moves(self,move):
    #     moves = self.get_moves()
    #     moves.append(move)

    def get_coordinate_by_value(self, value):
        for i in range(4):
            for j in range(4):
                if value == self.position[i][j]:
                    x = i
                    y = j
        return [x,y]

    def __lt__(self, other):
        return self.get_f() < other.get_f()
    
    def print_position(self):
        for i in range(4):
            for j in range(4):
                print(self.position[i][j], end="\t")
            print()

    def print_node(self):
        # print("-----NODE-----")
        print("Position: ")
        self.print_position()
        print("Moves so far: ", self.moves)
        # print("Current move/prev move: ", self.current_move)
        print("Cost (nilai g): ",self.get_g())
        print("Heuristic: ",self.get_h())
        print("nilai f:",self.get_f())
    
    def move(self,direction):
        i_old, j_old = self.get_coordinate_by_value(0)
        position = self.get_position()
        if direction == "down":
            i = 1
            j = 0
        elif direction == "up":
            i = -1
            j = 0
        elif direction == "right":
            i = 0
            j = 1
        elif direction == "left":
            i = 0
            j = -1   
        i_new, j_new = i_old + i, j_old + j
        position[i_old][j_old] = position[i_new][j_new]
        position[i_new][j_new] = 0
        self.set_position(position)
