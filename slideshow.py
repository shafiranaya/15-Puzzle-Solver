from app import create_puzzle, create_puzzle_solution
from tkinter import *
from PIL import ImageTk, Image
# import playsound
from main import solve
from Node import Node
def forward(puzzle_number):
    global puzzle_label
    global image_label
    global button_forward
    global button_back

    puzzle_label.grid_forget()
    # puzzle_label = create_puzzle(puzzle_list[puzzle_number-1])
    puzzle_label = create_puzzle_solution(puzzle_list[puzzle_number-1],moves_list[puzzle_number-1],(puzzle_number-1))

    button_back = Button(root, text='<--', command=lambda: back(puzzle_number-1))

    if puzzle_number == len(puzzle_list):
        button_forward = Button(root, text='-->', state=DISABLED)
    else:
        button_forward = Button(root, text='-->', command=lambda: forward(puzzle_number+1))
    
    puzzle_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

def back(puzzle_number):
    global puzzle_label
    global image_label
    global button_forward
    global button_back

    puzzle_label.grid_forget()
    # puzzle_label = create_puzzle(puzzle_list[puzzle_number-1])
    puzzle_label = create_puzzle_solution(puzzle_list[puzzle_number-1],moves_list[puzzle_number-1],(puzzle_number-1))

    button_forward = Button(root, text='-->', command=lambda: back(puzzle_number+1))

    if puzzle_number == 1:
        button_back = Button(root, text='<--', state=DISABLED)
    else:
        button_back = Button(root, text='<--', command=lambda: back(puzzle_number-1))
    
    puzzle_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

root = Tk()
root.title('Solution')


soal1 = [[1,2,3,4],[5,6,0,8],[9,10,7,11],[13,14,15,12]]
soal2 = [[0,2,3,4],[1,6,7,8],[5,10,11,12],[9,13,14,15]]
soal3 = [[6,5,2,4],[9,1,3,8],[10,0,7,15],[13,14,12,11]]
soal4 = [[1,9,4,8],[3,2,6,7],[13,10,11,12],[14,5,15,0]] #

puzzle_list = []
node = Node(soal1, [], 0)
moves_list = solve(soal1)[0]
# print(solution)
# puzzle_list.append(soal1)
for sol in moves_list:
    node.move(sol)
    puzzle_list.append(node.get_position())
# print(solution)
# print(node.get_position_so_far())
# node.move(direction)
# puzzle_list = node.get_position_so_far()

# puzzle_list.insert(0,soal1)

print("PRINT PUZZLE LIST = ",puzzle_list)
print(len(puzzle_list))
# puzzle_list = [soal1,soal2,soal3,soal4]

puzzle_label = create_puzzle(soal1)

puzzle_label.grid(row=0,column=0,columnspan=3)

button_back = Button(root, text='<--', state=DISABLED)
button_exit = Button(root, text='Exit', command=root.quit)
button_forward = Button(root, text='-->', command=lambda:forward(1))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

root.mainloop()