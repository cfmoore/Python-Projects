#Grid for test purposes
grid = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]


def print_grid():
    for i in range(len(grid)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(grid[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(grid[i][j])
            else:
                print(str(grid[i][j]) + " ", end="")
    print("- - - - - - - - - - - - - ")

def solver():
    for y in range(len(grid)):
        for x in range(len(grid)):
            if grid[y][x] == 0:
                for solution in range(1,10):
                    if possible_solution(y,x,solution):
                        grid[y][x] = solution
                        solver()
                        grid[y][x] = 0
                return
    print_grid()

def possible_solution(y,x,solution):
    for i in range(len(grid)):
        if grid[y][i] == solution:
            return False
    for i in range(len(grid)):
        if grid[i][x] == solution:
            return False
    square_x = -1
    square_y = -1
    if y<3:
        square_y = 0
    elif y < 6:
        square_y = 3
    else:
        square_y = 6
    if x<3:
        square_x = 0
    elif x<6:
        square_x = 3
    else:
        square_x = 6
    temp_y = square_y
    temp_x = square_x
    while(square_y < temp_y+3):
        while(square_x < temp_x+3):
            if grid[y][x] == solution:
        square_y += 1
    return True;

                return false
            square_x += 1
        square_x = temp_x
solver()