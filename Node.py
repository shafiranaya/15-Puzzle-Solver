import copy

class Node:
    def __init__(self, position, moves, cost):
        self.position = position
        self.moves = moves
        self.cost = cost
        
    def get_position(self):
        return copy.deepcopy(self.position)
    def get_h(self):
        return self.cost
    def get_g(self):
        return len(self.moves)
    def get_f(self):
        return self.get_g() + self.get_h()
    def get_moves(self):
        return self.moves
    def add_moves(self,move):
        moves = self.get_moves()
        moves.append(move)
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
        print("Position: ")
        print(self.position)
        print("Moves: ")
        print(self.moves)
        print("Cost: ")
        print(self.cost)
