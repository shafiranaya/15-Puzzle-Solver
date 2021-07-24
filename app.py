# GUI

from main import solve, is_valid
from tkinter import *
from Node import Node
from tkinter import messagebox

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
    puzzle_frame = Frame(top, width = 312, height = 272.5, bg = "#F29191")
    puzzle_frame.pack()
    numbers = [[0 for i in range(4)] for j in range(4)]
    for i in range(4):
        for j in range(4):
            if (matrix[i][j] == 0):
                numbers[i][j] = Label(puzzle_frame, text=" ", width=5, height=3, bd=0, bg="#D1D9D9").grid(row=i, column=j,padx=1,pady=1)
            else:
                numbers[i][j] = Label(puzzle_frame, text=str(matrix[i][j]), width=5, height=3, bd=0, bg="#EEC4C4").grid(row=i, column=j,padx=1,pady=1)

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
    title = Label(solution_window, text="\nSoal: \n").pack()
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

def show_solution():
    initialize()
    # Validate input
    valid = is_valid(matrix)
    # Show solution
    if (valid):
        solution = solve(matrix)
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
    # centering
    window.grid_rowconfigure(0,weight=1)
    window.grid_columnconfigure(0,weight=1)

    create_entry(window)
    window.mainloop()
    
def create_buttons(window):
    title_label = Label(window, text="15 Puzzle Solver", justify="center",bg="#D1D9D9")
    title_label.grid(row=0, column=0,columnspan=4)
    # blank_label = Label(window,text="",bg="#94D0CC")
    # blank_label.grid(row=6,column=0,columnspan=4)
    button_reset = Button(window, text="Reset", justify='center', command = lambda: reset())
    button_solve = Button(window, text="Solve", justify='center', command = lambda: show_solution())
    button_solve.grid(row=5,column=0,columnspan=2)
    button_reset.grid(row=5,column=2,columnspan=2)
    title_label.grid(row=0, column=0,columnspan=4)

def reset():
    for e in entries:
        e.delete(0, END)

def create_entry(window):
    global matrix

    entries_frame = Frame(window, width = 312, height = 272.5, bg="#D1D9D9")
    entries_frame.grid(row=0,column=0)

    for i in range(4):
        for j in range(4):
            entry_label = Label(entries_frame, text=" ", width=5, height=3, bg="#ffffff",bd=0).grid(row=i+1, column=j,padx=1,pady=1)
            entry = Entry(entries_frame,width=3)
            entry.grid(row=i+1,column=j)
            entries.append(entry)

    create_buttons(entries_frame)

if __name__=="__main__":
    # jawaban = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]
    problem_GUI()
    # soal1 = [[1,2,3,4],[5,6,0,8],[9,10,7,11],[13,14,15,12]]
    # soal2 = [[0,2,3,4],[1,6,7,8],[5,10,11,12],[9,13,14,15]]
    # print(entries)
