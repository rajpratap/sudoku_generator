import random
sudoku=[
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]]
def gen(board):
    find=find_empty(board)
    if not find:
        return True
    else:
        row,col=find
    l=random.sample(range(1,10),9)
    for i in l:
        if valid(board,i,(row,col)):
            board[row][col]=i
            if gen(board):
                return True
            board[row][col]=0
    return False
def valid(board,num,pos):
    #check for row
    for i in range(9):
        if board[pos[0]][i]==num and pos[1]!=i:
            return False
    #check for column
    for i in range(9):
        if board[i][pos[1]]==num and pos[0]!=i:
            return False
    #check for box
    box_x=pos[1]//3
    box_y=pos[0]//3
    for i in range(box_y*3,box_y*3+3):
        for j in range(box_x*3,box_x*3+3):
            if board[i][j]==num and (i,j)!=pos:
                return False
    return True
def print_sudoku(board):
    for i in range(9):
        if i==3 or i==6:
            print("- - - - - - - - - - -")
        for j in range(9):
            if j==3 or j==6:
                print("|",end=" ")
            print(board[i][j],end=" ")
        print()
def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j]==0:
                return (i,j)
    return None
def puzzle(board):
    x=[]
    for i in board:
        for j in i:
            x.append(j)
    x1=random.sample(range(81),random.choice(range(35,50)))
    for i in x1:
        x[i]=0
    board=[]
    t=0
    for i in range(9):
        temp=[]
        for j in range(9):
            temp.append(x[t])
            t+=1
        board.append(temp)
    return board
gen(sudoku)
print_sudoku(sudoku)
print()
pu=puzzle(sudoku)
print_sudoku(pu)
