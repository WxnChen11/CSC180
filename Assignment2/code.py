"""Gomoku starter code
You should complete every incomplete function,
and add more functions and variables as needed.

Note that incomplete functions have 'pass' as the first statement:
pass is a Python keyword; it is a statement that does nothing.
This is a placeholder that you should remove once you modify the function.

Authors: Michael Guerzhoy.  Last modified: Nov. 4, 2015
"""



def is_empty(board):
    for row in board:
        for col in row:
            if col != " ":
                return False
                
    return True

def is_bounded(board, y_end, x_end, length, d_y, d_x):

    end_square = (y_end + d_y, x_end + d_x)
    start_square = ((y_end) - d_y * length, (x_end) - d_x * length)
    
    if end_square[0] <0 or end_square[0] >= len(board) or end_square[1] <0 or end_square[1] >= len(board):
        if start_square[0] <0 or start_square[0] >= len(board) or start_square[1] <0 or start_square[1] >= len(board):
            return "CLOSED"
        if board[start_square[0]][start_square[1]] != " ":
            return "CLOSED"
    
        return "SEMIOPEN"
        
    if start_square[0] <0 or start_square[0] >= len(board) or start_square[1] <0 or start_square[1] >= len(board):
        if board[end_square[0]][end_square[1]] != " ":
            return "CLOSED"
            
        return "SEMIOPEN"
        
    if board[end_square[0]][end_square[1]] == " " and board[start_square[0]][start_square[1]] == " ":
        return "OPEN"
    
    if board[end_square[0]][end_square[1]] != " " and board[start_square[0]][start_square[1]] != " ":
        return "CLOSED"
    
    return "SEMIOPEN"
    
    
    # if d_x == 0 and d_y == 1: #Vertical
    #     if length == len(board):
    #         return "CLOSED"
    #     if y_end + 1 == len(board):
    #         if board[(y_end + 1) - length][x_end] == " ":
    #             return "SEMIOPEN"
    #         else:
    #             return "CLOSED"
    #     if y_end - length == -1:
    #         if board[y_end + 1][x_end] == " ":
    #             return "SEMIOPEN"
    #         else:
    #             return "CLOSED"
    #     if board[y_end-length][x_end] == " " and board[x_end][y_end+1] == " ":
    #         return "OPEN"
    #     if board[y_end-length][x_end] == " " or board[x_end][y_end+1] == " ":
    #         return "SEMIOPEN"
    #     else:
    #         return "CLOSED"
    #         
    # if d_x == 1 and d_y == 0: #Horizontal
    #     if length == len(board):
    #         return "CLOSED"
    #     if x_end + 1 == len(board):
    #         if board[y_end][(x_end+1) - length] == " ":
    #             return "SEMICLOSED"
    #         else:
    #             return "CLOSED"
    #     if x_end - length == -1:
    #         if board[y_end][x_end + 1]== " ":
    #             return "SEMICLOSED"
    #         else:
    #             return "CLOSED"
    # 
    # if d_x == 1 and d_y == 1: #Diagonal bottom to right
    #     if length == len(board):
    #         return "CLOSED"
    #     if y_end == 0:
    #         if x_end - length == 1:
    #             return "CLOSED"
    #         if x_end :
    #     if x_end == len(board) -1 and y_end + length == len(board):
    #         return "CLOSED"
        
        
def detect_row(board, col, y_start, x_start, length, d_y, d_x):
    
    y = y_start
    x = x_start
    
    num_open = 0
    num_semi = 0
    
    len_sequence = 0
    
    while y < len(board) and x < len(board) and y>=0:
        
        y1 = y
        x1 = x
        
        if board[y][x] == col:

            while y1 < len(board) and x1 < len(board) and y>=0 and board[y1][x1] == col:
                y1 += d_y
                x1 += d_x
                len_sequence += 1
            
            if len_sequence == length:
                if is_bounded(board, y1 - d_y, x1 - d_x, len_sequence, d_y, d_x) == "OPEN":
                    num_open += 1
                elif is_bounded(board, y1 - d_y, x1 - d_x, len_sequence, d_y, d_x) == "SEMIOPEN":
                    num_semi += 1
            
            len_sequence = 0
        
        if y1 == y and x1 == x:
            y += d_y
            x += d_x
        else:
            y = y1
            x = x1
    
    if len_sequence == length:
        if is_bounded(board, y1 - d_y, x1 - d_x, len_sequence, d_y, d_x) == "OPEN":
            num_open += 1
        elif is_bounded(board, y1 - d_y, x1 - d_x, len_sequence, d_y, d_x) == "SEMIOPEN":
            num_semi += 1
    
    return (num_open, num_semi)

    
    # for j in range(len(board)):
    #     
    #     if board[y][x] == col:
    #         
    #         if seq_start[0] == -5:
    #             seq_start[0] = y
    #             seq_start[1] = x
    #             
    #         len_sequence += 1
    #         
    #         if is_bounded(board, (seq_start[0]-1) + d_y*len_sequence , (seq_start[1]-1) + d_x*len_sequence, len_sequence, d_y, d_x) == "OPEN":
    #             num_open += 1
    #         elif is_bounded(board, (seq_start[0]-1) + d_y*len_sequence , (seq_start[1]-1) + d_x*len_sequence, len_sequence, d_y, d_x) == "SEMIOPEN":
    #             num_semi += 1
    #         
    #     else:
    #         len_sequence = 0
    #         seq_start = [-5, -5]

   ##       y += d_y
    #     x += d_x
    #     
    #     print("y", y)
    #     print("x", x)
    #     print(j)
    #     
    # return (num_open, num_semi)
        
def test_detect_row():
    
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_row(board, "w", 0 ,x,length,d_y,d_x) == (1,0):
        print("TEST CASE for detect_row PASSED")
    else:
        # print(detect_row(board, "w", 0,x,length,d_y,d_x))
        print("TEST CASE for detect_row FAILED")
            





def detect_rows(board, col, length):
    
    open_seq_count, semi_open_seq_count = 0, 0
    
    for i in range(len(board)):
        
        temp = detect_row(board, col, i, 0, length, 0, 1)
        open_seq_count += temp[0]
        semi_open_seq_count += temp[1]
            
        temp = detect_row(board, col, 0, i, length, 1, 0)
        open_seq_count += temp[0]
        semi_open_seq_count += temp[1]

        temp = detect_row(board, col, 0, i, length, 1, 1)
        open_seq_count += temp[0]
        semi_open_seq_count += temp[1]
        
        temp = detect_row(board, col, i, 0, length, 1, 1)
        open_seq_count += temp[0]
        semi_open_seq_count += temp[1]
        
        temp = detect_row(board, col, i, 0, length, -1, 1)
        open_seq_count += temp[0]
        semi_open_seq_count += temp[1]
        
        temp = detect_row(board, col, len(board)-1, i, length, -1, 1)
        open_seq_count += temp[0]
        semi_open_seq_count += temp[1]
    
    return open_seq_count, semi_open_seq_count
    
        
def test_detect_rows():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_rows(board, col,length) == (1,0):
        print("TEST CASE for detect_rows PASSED")
    else:
        print(detect_rows(board, col,length))
        print("TEST CASE for detect_rows FAILED")
    
    
def search_max(board):
    return move_y, move_x
    
def score(board):
    MAX_SCORE = 100000
    
    open_b = {}
    semi_open_b = {}
    open_w = {}
    semi_open_w = {}
    
    for i in range(2, 7):
        open_b[i], semi_open_b[i] = detect_rows(board, "b", i)
        open_w[i], semi_open_w[i] = detect_rows(board, "w", i)
        
    
    if open_b[5] >= 1 or semi_open_b[5] >= 1:
        return MAX_SCORE
    
    elif open_w[5] >= 1 or semi_open_w[5] >= 1:
        return -MAX_SCORE
        
    return (-10000 * (open_w[4] + semi_open_w[4])+ 
            500  * open_b[4]                     + 
            50   * semi_open_b[4]                + 
            -100  * open_w[3]                    + 
            -30   * semi_open_w[3]               + 
            50   * open_b[3]                     + 
            10   * semi_open_b[3]                +  
            open_b[2] + semi_open_b[2] - open_w[2] - semi_open_w[2])

    
def is_win(board):
    pass


def print_board(board):
    
    s = "*"
    for i in range(len(board[0])):
        s += str(i%10)
    s += "*\n"
    
    for i in range(len(board)):
        s += str(i%10)
        for j in range(len(board[0])):
            s += str(board[i][j])
    
        s += "*\n"
    s += (len(board[0])+2)*"*"
    
    print(s)
    

def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "]*sz)
    return board
                


def analysis(board):
    for c, full_name in [["w", "White"], ["b", "Black"]]:
        print("%s stones" % (full_name))
        for i in range(2, 6):
            open, semi_open = detect_rows(board, c, i);
            print("Open rows of length %d: %d" % (i, open))
            print("Semi-open rows of length %d: %d" % (i, semi_open))
    
def play_gomoku(board_size):
    board = make_empty_board(board_size)
    board_height = len(board)
    board_width = len(board[0])
    
    while True:
        print_board(board)
        if is_empty(board):
            move_y = board_height // 2
            move_x = board_width // 2
        else:
            move_y, move_x = search_max(board)
            
        print("Computer move: (%d, %d)" % (move_y, move_x))
        board[move_y][move_x] = "b"
        print_board(board)
        analysis(board)
        
        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res
            
            
        
        
        
        print("Your move:")
        move_y = int(input("y coord: "))
        move_x = int(input("x coord: "))
        board[move_y][move_x] = "w"
        print_board(board)
        analysis(board)
        
        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res
        
            
            
def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col        
        y += d_y
        x += d_x
        
def some_tests():
    board = make_empty_board(8)

    board[0][5] = "w"
    board[0][6] = "b"
    y = 5; x = 2; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    analysis(board)
    
    # Expected output:
    #       *01234567*
    #       0     wb *
    #       1        *
    #       2        *
    #       3        *
    #       4        *
    #       5  w     *
    #       6  w     *
    #       7  w     *
    #       **********
    #       Black stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 0
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    #       White stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 1
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    
    y = 3; x = 5; d_x = -1; d_y = 1; length = 2
    
    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)
    
    # Expected output:
    #         *01234567*
    #         0     wb *
    #         1        *
    #         2        *
    #         3     b  *
    #         4    b   *
    #         5  w     *
    #         6  w     *
    #         7  w     *
    #         **********
    #         Black stones:
    #         Open rows of length 2: 1
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 0
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #         White stones:
    #         Open rows of length 2: 0
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 1
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #     
    
    y = 5; x = 3; dX = -1; dY = 1; length = 1
    put_seq_on_board(board, y, x, d_y, d_x, length, "b");
    print_board(board);
    analysis(board);
    
    # Expected output:
    # *01234567*
    # 0     wb *
    # 1        *
    # 2        *
    # 3     b  *
    # 4    b   *
    # 5  wb    *
    # 6  w     *
    # 7  w     *
    # **********
    # Black stones:
    # Open rows of length 2: 0
    # Semi-open rows of length 2: 0
    # Open rows of length 3: 0
    # Semi-open rows of length 3: 1
    # Open rows of length 4: 0
    # Semi-open rows of length 4: 0
    # Open rows of length 5: 0
    # Semi-open rows of length 5: 0
    # White stones:
    # Open rows of length 2: 0
    # Semi-open rows of length 2: 0
    # Open rows of length 3: 0
    # Semi-open rows of length 3: 1
    # Open rows of length 4: 0
    # Semi-open rows of length 4: 0
    # Open rows of length 5: 0
    # Semi-open rows of length 5: 0

def test_is_empty():
    board  = make_empty_board(8)
    if is_empty(board):
        print("TEST CASE for is_empty PASSED")
    else:
        print("TEST CASE for is_empty FAILED")

def test_is_bounded():
    board = make_empty_board(8)
    x = 0; y = 7; d_x = 1; d_y = -1; length = 4
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    
    y_end = 0
    x_end = 7

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'CLOSED':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")
        
def test_detect_row():
    board = make_empty_board(8)
    x =1; y = 1; d_x = 1; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    put_seq_on_board(board, 2, 5, d_y, 0, 3, "w")

    print_board(board)
    if detect_row(board, "w", y,x,6,d_y,d_x) == (1,0):
        print(detect_row(board, "w", y,x,6,d_y,d_x))
        print("TEST CASE for detect_row PASSED")
    else:
        print(detect_row(board, "w", 0,5,3,1,0))
        print("TEST CASE for detect_row FAILED")
        
def test_detect_rows():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 4; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    put_seq_on_board(board, 4, 3, d_y, d_x, 4, "w")
    put_seq_on_board(board, 4, 0, -1, 1, 4, "w")

    print_board(board)
    
    print(detect_rows(board, col,length))

if __name__ == '__main__':
    
    test_is_bounded()
    test_is_empty()
    test_detect_row()
    test_detect_rows()
    # play_gomoku(8)
    