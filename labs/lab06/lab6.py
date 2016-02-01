'''
 X | O | X
---+---+---
 O | O | X    
---+---+---
   | X | 
'''

import random


def print_board_and_legend(board):
    for i in range(3):
        line1 = " " +  board[i][0] + " | " + board[i][1] + " | " +  board[i][2]
        line2 = "  " + str(3*i+1)  + " | " + str(3*i+2)  + " | " +  str(3*i+3) 
        print(line1 + " "*5 + line2)
        if i < 2:
            print("---+---+---" + " "*5 + "---+---+---")
    print("")
    print("")
    
    
def make_empty_board():
    board = []
    for i in range(3):
        board.append([" "]*3)
    return board
    
def num_to_list(square_num):
    
    return [((square_num-1)//3),square_num-((((square_num-1)//3))*3+1)]

def put_in_board(board, mark, square_num):
    
    board[num_to_list(square_num)[0]][num_to_list(square_num)[1]] = mark

def get_free_squares(board):
    
    res = []
    
    for i in range(len(board)):
        for z in range(len(board[0])):
            if board[i][z] == " ":
                res.append([i,z])
                
    return res
                
def make_random_move(board, mark):
    
    if len(get_free_squares(board))>0:
        r = get_free_squares(board)[int((len(get_free_squares(board))) * random.random())]
    
        board[r[0]][r[1]] = mark
        
def is_row_all_marks(board, row_i, mark):
    
    for z in range(len(board[row_i])):
        if board[row_i][z] != mark:
            return False
    
    return True

def is_col_all_marks(board, col_i, mark):
    
    for z in range(len(board)):
        if board[z][col_i] != mark:
            return False
    
    return True
    
def is_win(board, mark):
    
    if board[0][0] == mark and board[1][1] == mark and board[2][2] == mark:
        return True
    if board[2][0] == mark and board[1][1] == mark and board[0][2] == mark:
        return True
    
    for i in range (3):
    
        if is_row_all_marks(board, i, mark):
            return  True
        if is_col_all_marks(board, i, mark):
            return True
    
    return False

def make_move_smart(board, mark):
    

    if len(get_free_squares(board))>0:
        
        for r in range(len(get_free_squares(board))):
            
            tempboard=list(board)
            
            i = get_free_squares(tempboard)[r]
            
            tempboard[i[0]][i[1]] = mark
            
            if is_win(tempboard, mark):
                
                board[i[0]][i[1]] = mark
                return
    
    make_random_move(board, mark)

if __name__ == '__main__':
    
    board = make_empty_board()
    print_board_and_legend(board)    
    
    print(num_to_list(1))
    
    put_in_board(board, "X", 5)
    put_in_board(board, "X", 4)
    put_in_board(board, "X", 1)

    print_board_and_legend(board)    

    print (get_free_squares(board))
    
    make_random_move(board, "X")
    print_board_and_legend(board)
    make_random_move(board, "X")
    print_board_and_legend(board)
    make_random_move(board, "X")
    print_board_and_legend(board)
    # make_random_move(board, "X")
    # print_board_and_legend(board)
    # make_random_move(board, "X")
    # print_board_and_legend(board)
    # make_random_move(board, "X")
    # print_board_and_legend(board)
    # make_random_move(board, "X")
    # print_board_and_legend(board)
        
    print(is_col_all_marks(board, 0, "X"))
    print(is_col_all_marks(board, 1, "X"))
    print(is_col_all_marks(board, 2, "X"))
    
    board = make_empty_board()
    
    print(list(board))
    print(board)
    
    
    while(True):
    
        print_board_and_legend(board)  

        if is_win(board, "X"):
            print("Congratulations! X Has Won the Game.")
            break
        if is_win(board, "O"):
            print("Congratulations! O Has Won the Game.")
            break
            
        move = int(input('Enter your move: '))
        put_in_board(board, "O", move)
        print_board_and_legend(board)  
        #make_move_smart(board, "X")
        make_random_move(board, "X")
        #print_board_and_legend(board)  
    
        