import copy

class Node:
    def __init__(self, position, moves, cost):
        self.position = position
        self.moves  = moves # moves so far
        # self.current_move = current_move
        self.cost = cost # didapat dari fungsi g

    def get_position(self):
        return copy.deepcopy(self.position)

    def get_g(self):
        return self.cost

    def get_h(self):
        return len(self.moves)

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
        
    def print_node(self):
        # print("-----NODE-----")
        print("Position: ")
        print(self.position)
        print("Moves so far: ", self.moves)
        # print("Current move/prev move: ", self.current_move)
        print("Cost (nilai g): ",self.cost)
        # print("nilai f:",self.get_f())
