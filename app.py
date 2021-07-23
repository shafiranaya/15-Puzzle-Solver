# GUI

# TODO: fungsi untuk cetak langkah2 dll
# TODO: fungsi utk cetak puzzle 
# TODO: validasi input ->
# - Harus ada satu cell kosong
# - Utk cell ga kosong, angkanya mesti 1-15
# - gaboleh ada angka yg double

from tkinter import *
# from main import solve
entries = []

def initialize(top,arr):
    print(arr)
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

def print_puzzle(top,matrix):
    btns_frame = Frame(top, width = 312, height = 272.5, bg = "grey")
    btns_frame.pack()
    numbers = [[0 for i in range(4)] for j in range(4)]
    for i in range(4):
        for j in range(4):
            numbers[i][j] = Button(btns_frame, text=str(matrix[i][j]), width=10, height=3, bd=0, bg="#fff").grid(row=i, column=j,padx=1,pady=1)

# def print_solution():
#     return 

def create_GUI(maze):
    top = Tk()
    top.title("15-Puzzle Solver")
    canvas = Canvas(top, height=320, width =350)
    # createRow(canvas)
    # createCol(canvas)
    top2 = Tk()
    jawaban = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]
    create_entry(top)
    create_buttons(top,maze)
    print_puzzle(top2,jawaban)
    canvas.pack(side = 'top')
    top.mainloop()
    top2.mainloop()
    
def create_buttons(top,maze):
    # button_solve = Button(top, text="Solve", justify='left', default='active', command = lambda: play_Game(top,maze))
    button_reset = Button(top, text="Reset", justify='right', command = lambda: reset())
    button_check = Button(top, text="Check", justify='left', default='active', command = lambda: initialize(top,maze))
    # button_print = Button(top, text="Print", justify='center', default='active', command = lambda: print_puzzle(initialize(top,maze)))
    # button_solve.place(x=70, y=275, height=30, width=60)
    button_check.place(x=70, y=275, height=30, width=60)
    button_reset.place(x=230, y=275, height=30, width=60)
    # button_print.place(x=300, y=275, height=30, width=60)

def reset():
    for e in entries:
        e.delete(0, END)
    
def create_entry(top):
    p,q=41.4,41.4
    for i in range(4):
        for j in range(4):
            E = Entry(top, width=3, font = 'BOLD')
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
    create_GUI(mat)
    initialize(entries)
    # print_maze(entries)
    print(entries)