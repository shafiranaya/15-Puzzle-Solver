# GUI

from main import solve, is_valid
from tkinter import *
from Node import Node
from tkinter import messagebox

# TODO: buat window solution nya jadi horizontally centered dan rapih2in GUI!
entries = []

def initialize():
    global matrix
    matrix = [[0 for i in range(4)] for j in range(4)]
    for i in range(4):
        for j in range(4):
            if (not entries[(4*i)+j].get()):
                matrix[i][j] = 0
            else:
                matrix[i][j] = int(entries[(4*i)+j].get())

# Buat print satu step gitu deh
def print_puzzle(top,matrix):
    puzzle_frame = Frame(top, width = 312, height = 272.5, bg = "grey")
    puzzle_frame.pack()
    numbers = [[0 for i in range(4)] for j in range(4)]
    for i in range(4):
        for j in range(4):
            if (matrix[i][j] == 0):
                numbers[i][j] = Label(puzzle_frame, text=" ", width=5, height=3, bd=0, bg="white").grid(row=i, column=j,padx=1,pady=1)
            else:
                numbers[i][j] = Label(puzzle_frame, text=str(matrix[i][j]), width=5, height=3, bd=0, bg="pink").grid(row=i, column=j,padx=1,pady=1)

def create_puzzle(matrix):
    puzzle_frame = Frame(width = 312, height = 272.5, bg = "grey")
    # puzzle_frame.pack()
    numbers = [[0 for i in range(4)] for j in range(4)]
    for i in range(4):
        for j in range(4):
            if (matrix[i][j] == 0):
                numbers[i][j] = Label(puzzle_frame, text=" ", width=5, height=3, bd=0, bg="white").grid(row=i, column=j,padx=1,pady=1)
            else:
                numbers[i][j] = Label(puzzle_frame, text=str(matrix[i][j]), width=5, height=3, bd=0, bg="pink").grid(row=i, column=j,padx=1,pady=1)
    return puzzle_frame

def create_puzzle_awal(matrix):
    puzzle_frame = Frame(width = 312, height = 272.5, bg = "grey")
    # puzzle_frame.pack()
    # Print puzzle soal
    title = Label(puzzle_frame, text="\nSolution\n").grid(row=0,column=0)
    # print_puzzle(create_puzzle, matrix)

    solution, node_count = solve(matrix)

    # Print ada berapa node yang dibangkitkan
    node_display = "Simpul yang dibangkitkan: " + str(node_count)
    node_label = Label(puzzle_frame, text=node_display).grid(row=1,column=0)

    # Print ada berapa steps, stepsnya apa saja
    steps_display = "Jumlah langkah yang dibutuhkan untuk menyelesaikan puzzle: " + str(len(solution))
    moves_display = "Langkah: "
    for i in range(len(solution)):
        if (i != (len(solution)-1)):
            moves_display += solution[i] + " -> "
        else:
            moves_display += solution[i]
    steps_label = Label(puzzle_frame, text=steps_display).grid(row=2,column=0)
    moves_label = Label(puzzle_frame, text=moves_display).grid(row=3,column=0)
    numbers = [[0 for i in range(4)] for j in range(4)]
    x = 0
    y = 1
    for i in range(4):
        for j in range(4):
            if (matrix[i][j] == 0):
                numbers[i][j] = Label(puzzle_frame, text=" ", width=5, height=3, bd=0, bg="white").grid(row=x+i, column=y+j,padx=1,pady=1)
            else:
                numbers[i][j] = Label(puzzle_frame, text=str(matrix[i][j]), width=5, height=3, bd=0, bg="pink").grid(row=x+i, column=y+j,padx=1,pady=1)
    return puzzle_frame

def create_puzzle_solution(matrix,direction,num):
    puzzle_frame = Frame(width = 312, height = 272.5, bg = "grey")
    # node = Node(matrix, [], 0)
    # for i in range(len(solution)):
    # node.move(direction)
    info_display = "\nStep " + str(num+1) + ": " + direction
    info_label = Label(text=info_display).grid(row=5, column=0)
    numbers = [[0 for i in range(4)] for j in range(4)]
    for i in range(4):
        for j in range(4):
            if (matrix[i][j] == 0):
                numbers[i][j] = Label(puzzle_frame, text=" ", width=5, height=3, bd=0, bg="white").grid(row=i, column=j,padx=1,pady=1)
            else:
                numbers[i][j] = Label(puzzle_frame, text=str(matrix[i][j]), width=5, height=3, bd=0, bg="pink").grid(row=i, column=j,padx=1,pady=1)
    return puzzle_frame

def solution_GUI(matrix): 
    # Create canvas with scrollbar
    window = Tk()
    window.title("15-Puzzle Solver - Solution")
    window.geometry("750x500")
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

    # Animation (kalo sempet aja)
    # animate_puzzle(window,solution)

    canvas.pack(side=LEFT,fill="both",expand=True)
    scrollbar.pack(side=RIGHT,fill="y")
    window.mainloop()

def show_solution():
    initialize()
    # Validate input
    valid = is_valid(matrix)
    solution = solve(matrix)
    # Show solution
    if (valid):
        if (solution == []):
            messagebox.showinfo("Error","Puzzle unsolvable")
        else:
            solution_GUI(matrix)
    else:
        messagebox.showinfo("Error","Input yang dimasukkan salah.")
        reset()

def problem_GUI():
    window = Tk()
    window.title("15-Puzzle Solver")
    window.geometry("750x500")
    window.grid_rowconfigure(0,weight=1)
    window.grid_columnconfigure(0,weight=1)
    # canvas = Canvas(window, height=320, width =350)
    create_entry(window)
    # canvas.pack(side = 'top')
    window.mainloop()
    
def create_buttons(window):
    button_reset = Button(window, text="Reset", justify='center', command = lambda: reset())
    button_solve = Button(window, text="Solve", justify='center', command = lambda: show_solution())
    button_solve.grid(row=5,column=1)
    button_reset.grid(row=5,column=2)

def reset():
    for e in entries:
        e.delete(0, END)

def create_entry(window):
    global matrix

    entries_frame = Frame(window, width = 312, height = 272.5, bg = "grey")
    entries_frame.grid(row=0,column=0)

    for i in range(4):
        for j in range(4):
            entry_label = Label(entries_frame, text=" ", width=5, height=3, bg="white",bd=0).grid(row=i, column=j,padx=1,pady=1)
            # entry = Entry(entries_frame,width=3).grid(row=0, column=0)
            entry = Entry(entries_frame,width=3)
            entry.grid(row=i,column=j)
            # entry.grid(row=i+1,column=j+1)
            entries.append(entry)
    create_buttons(entries_frame)

    
if __name__=="__main__":
    jawaban = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]
    problem_GUI()
    soal1 = [[1,2,3,4],[5,6,0,8],[9,10,7,11],[13,14,15,12]]
    soal2 = [[0,2,3,4],[1,6,7,8],[5,10,11,12],[9,13,14,15]]
    print(entries)
