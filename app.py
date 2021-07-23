# GUI

# TODO: fungsi untuk cetak langkah2 dll
# TODO: fungsi utk cetak puzzle 

# TODO: sambungin pencetan solve
# TODO nanti kalo pencet solve, kebuka window baru yang isinya solusi. (DONE)
# TODO trus print2 puzzle nya, dimasukin ke scrollbar gitu deh (DONE)

from main import solve
from tkinter import *
from Node import Node
# from main import solve
entries = []

def initialize(arr):
    # print(arr)
    global matrix
    En = entries
    print("En=",En,"len=",len(En))
    matrix = [[0 for i in range(4)] for j in range(4)]
    for i in range(4):
        for j in range(4):
            if (not En[(4*i)+j].get()):
                matrix[i][j] = 0
            else:
                matrix[i][j] = int(En[(4*i)+j].get())
    print("MATRIX=",matrix)

# Buat print satu step gitu deh
def print_puzzle(top,matrix):
    btns_frame = Frame(top, width = 312, height = 272.5, bg = "grey")
    btns_frame.pack()
    numbers = [[0 for i in range(4)] for j in range(4)]
    for i in range(4):
        for j in range(4):
            if (matrix[i][j] == 0):
                numbers[i][j] = Label(btns_frame, text=" ", width=5, height=3, bd=0, bg="pink").grid(row=i, column=j,padx=1,pady=1)
            else:
                numbers[i][j] = Label(btns_frame, text=str(matrix[i][j]), width=5, height=3, bd=0, bg="#fff").grid(row=i, column=j,padx=1,pady=1)

def solution_GUI(matrix): 
    # Create canvas with scrollbar
    window = Tk()
    canvas = Canvas(window)
    scrollbar = Scrollbar(window, command=canvas.yview)
    canvas.configure(yscrollcommand = scrollbar.set)
    canvas.bind('<Configure>',  lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    solution_window = Frame(canvas)
    canvas.create_window((0,0), window=solution_window, anchor='nw')

    # Print puzzle soal
    title = Label(solution_window, text="\nSolution\n").pack()
    print_puzzle(solution_window, matrix)

    solution, node_count = solve(matrix)

    # Print ada berapa node yang dibangkitkan
    node_display = "Simpul yang dibangkitkan: " + str(node_count)
    node_label = Label(solution_window, text=node_display).pack()

    # Print ada berapa steps, stepsnya apa saja
    steps_display = "Jumlah langkah yang dibutuhkan untuk menyelesaikan puzzle: " + str(len(solution)) + "\n" + "Langkah: "
    for i in range(len(solution)):
        if (i != (len(solution)-1)):
            steps_display += solution[i] + " -> "
        else:
            steps_display += solution[i]
    steps_label = Label(solution_window, text=steps_display).pack()

    # Show position per step
    node = Node(matrix, [], 0)
    for i in range(len(solution)):
        node.move(solution[i])
        info_display = "\nStep " + str(i+1) + ": " + solution[i]
        info_label = Label(solution_window, text=info_display).pack()
        print_puzzle(solution_window,node.get_position())

    canvas.pack(side=LEFT,fill="both",expand=True)
    scrollbar.pack(side=RIGHT,fill="y")
    window.mainloop()

def problem_GUI():
    global matrix
    window = Tk()
    window.title("15-Puzzle Solver")
    canvas = Canvas(window, height=320, width =350)
    # top2 = Tk()
    # list_of_puzzles = []
    # jawaban = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]
    # list_of_puzzles.append(maze)
    # list_of_puzzles.append(jawaban)

    create_entry(window)
    create_buttons(window)
    # print_puzzle(top2,jawaban)
    # print_puzzle(top2,maze)
    canvas.pack(side = 'top')
    window.mainloop()
    # top2.mainloop()
    
def create_buttons(window):
    # button_solve = Button(top, text="Solve", justify='left', default='active', command = lambda: play_Game(top,maze))
    button_reset = Button(window, text="Reset", justify='right', command = lambda: reset())
    button_check = Button(window, text="Check", justify='left', default='active', command = lambda: solution_GUI(matrix))
    # button_print = Button(top, text="Print", justify='center', default='active', command = lambda: print_puzzle(initialize(top,maze)))
    # button_solve.place(x=70, y=275, height=30, width=60)
    button_check.place(x=70, y=275, height=30, width=60)
    button_reset.place(x=230, y=275, height=30, width=60)
    # button_print.place(x=300, y=275, height=30, width=60)

def reset():
    for e in entries:
        e.delete(0, END)

def create_entry(window):
    global matrix
    p,q=41.4,41.4
    for i in range(4):
        for j in range(4):
            E = Entry(window, width=3, font = 'BOLD')
            E.grid(row=i, column=j)
            E.place(x=p, y=q, height=20, width=25)
            entries.append(E)
            p+=30.0
        q+=24.5
        p=41.2
    
if __name__=="__main__":
    jawaban = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]
    # print_puzzle(jawaban)
    mat =[[0 for x in range(4)]for y in range(4)]
    # problem_GUI()
    # matrix = initialize(entries)
    soal1 = [[1,2,3,4],[5,6,0,8],[9,10,7,11],[13,14,15,12]]
    soal2 = [[0,2,3,4],[1,6,7,8],[5,10,11,12],[9,13,14,15]]

    solution_GUI(soal2)
    # print_maze(entries)
    print(entries)