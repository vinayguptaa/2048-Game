import random
def start_game():
    mat= []
    for i in range(4):
        mat.append([0]*4)
    
    return mat

def add_new_2(mat):
    r = random.randint(0,3)
    c = random.randint(0,3)
    
    while mat[r][c] != 0:
        r = random.randint(0,3)
        c = random.randint(0,3)
        
    mat[r][c] = 2
    
    
def get_current_state(mat):
    #######won
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 2048:
                return "WON"
    
    #######in the game
    
    #check for empty position if any
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 0:
                return "GAME NOT OVER"
    
    #check for consecutive same els excpet in last row and last col
    for i in range(3):
        for j in range(3):
            if mat[i][j+1] == mat[i][j] or mat[i+1][j] == mat[i][j]:
                return "GAME NOT OVER"
    
    #last row
    for j in range(3):
        if mat[3][j] == mat[3][j+1]:
            return "GAME NOT OVER"
        
    for i in range(3):
        if mat[i][3] == mat[i+1][3]:
            return "GAME NOT OVER"
    
    return "LOST"


def compress(mat):
    new_mat = []
    changed = False
    for i in range(4):
        new_mat.append(4*[0])
    
    for i in range(4):
        pos = 0
        for j in range(4):
            if mat[i][j] != 0:
                new_mat[i][pos] = mat[i][j]
                if pos != j:
                    changed = True
                pos+=1
    
    return new_mat, changed

#left logic
def merge(mat):
    changed = False
    for i in range(4):
        for j in range(3):
            if mat[i][j] == mat[i][j+1] and mat[i][j]!=0:
                changed = True
                mat[i][j] = mat[i][j]*2
                mat[i][j+1] = 0
    
    return mat, changed

#reversing each row
def reverse(mat):
    for i in range(4):
        for j in range(2):
            mat[i][j], mat[i][4-j-1] = mat[i][4-j-1], mat[i][j]
    
    return mat
    
def transpose(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([0]*4)
    
    for i in range(4):
        for j in range(4):
            new_mat[j][i] = mat[i][j]
    
    return new_mat

def move_left(grid):
    grid,changed1 = compress(grid)
    grid,changed2 = merge(grid)
    changed = changed1 or changed2
    grid,temp = compress(grid)
    return grid, changed

def move_right(grid):
    grid = reverse(grid)
    grid,changed1 = compress(grid)
    grid,changed2 = merge(grid)
    changed = changed1 or changed2
    grid,temp = compress(grid)
    grid = reverse(grid)
    return grid, changed

def move_up(grid):
    grid = transpose(grid)
    grid,changed1 = compress(grid)
    grid,changed2 = merge(grid)
    changed = changed1 or changed2
    grid,temp = compress(grid)
    grid = transpose(grid)
    return grid, changed

def move_down(grid):
    grid = transpose(grid)
    grid = reverse(grid)
    grid,changed1 = compress(grid)
    grid,changed2 = merge(grid)
    changed = changed1 or changed2
    grid,temp = compress(grid)
    grid = reverse(grid)
    grid = transpose(grid)
    return grid, changed