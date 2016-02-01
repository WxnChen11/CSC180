def get_move(board, col):
    '''Return a tuple which contains the coordinates of the move the AI wants
    to make for colour col on board board'''
    
    def num_threats(board, col):
        
        horizontal = [""]*len(board)
        vertical = [""]*len(board)
        diag_down_below = [""]*(len(board)-1)
        diag_down_above = [""]*len(board)
        diag_up_below = [""]*(len(board)-1)
        diag_up_above = [""]*len(board)
        
        for i in range(len(board)):
            for k in range(len(board[0])):
                if board[i][k] != " ":
                    horizontal[i] += board[i][k]
                else:
                    horizontal[i] += "s"
                    
        for i in range(len(board)):
            for k in range(len(board[0])):
                if board[k][i] != " ":
                    vertical[i] += board[k][i]
                else:
                    vertical[i] += "s"
        #diag_down_below
        for i in range(len(board)-1):
            
            y = i
            x = 0
            
            while y < len(board):
                if board[y][x] != " ":
                    diag_down_below[i] +=  board[y][x]
                else: 
                    diag_down_below[i] += "s"
                
                y += 1
                x += 1
                
        #diag_down_above
        for i in range(0 , len(board)):
            
            y = 0
            x = i
            
            while x < len(board):
                if board[y][x] != " ":
                    diag_down_above[i] += board[y][x]
                else: 
                    diag_down_above[i] += "s"
                
                y += 1
                x += 1        
        
        #diag_up_below
        for i in range(len(board)-1):
            
            y = len(board)-1
            x = i
            
            while x < len(board):
                if board[y][x] != " ":
                    diag_up_below[i] += board[y][x]
                else: 
                    diag_up_below[i] += "s"
                
                y -= 1
                x += 1
    
        #diag_up_above
        for i in range(len(board)):
            
            y = i
            x = 0
            
            while y >= 0:
                if board[y][x] != " ":
                    diag_up_above[i] += board[y][x]
                else: 
                    diag_up_above[i] += "s"
                
                y -= 1
                x += 1  
        
        L = [horizontal , vertical , diag_down_below, diag_down_above, diag_up_below, diag_up_above]
        
        threats = [ 0 , 0 ]
        #(3)three6, (4)broken3
        three6_1 = "ss" + 3*col + "s"
        three6_2 = "s" + 3*col + "ss"
        broken3_1 = "s"+ 2*col + "s" + col + "s"
        broken3_2 = "s"+ col + "s" + 2*col + "s"
        
        for list in L:
            for s in list:

                if three6_1 in s or three6_2 in s:
                    threats[0] += s.count(three6_1) + s.count(three6_2)
                if broken3_1 in s or broken3_2 in s:
                    threats[1] += s.count(broken3_1) + s.count(broken3_2)
        
        return threats
                
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
    
            
    def detect_row(board, col, y_start, x_start, length, d_y, d_x):
        
        y = y_start
        x = x_start
        
        num_open = 0
        num_semi = 0
        num_closed = 0
        
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
                    elif is_bounded(board, y1 - d_y, x1 - d_x, len_sequence, d_y, d_x) == "CLOSED":
                        num_closed += 1
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
            elif is_bounded(board, y1 - d_y, x1 - d_x, len_sequence, d_y, d_x) == "CLOSED":
                num_closed += 1
                
        return (num_open, num_semi, num_closed)
    
            
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
        
        open_seq_count, semi_open_seq_count, closed_seq_count = 0, 0, 0
        
        for i in range(len(board)):
            
            temp = detect_row(board, col, i, 0, length, 0, 1)
            open_seq_count += temp[0]
            semi_open_seq_count += temp[1]
            closed_seq_count += temp[2]
                
            temp = detect_row(board, col, 0, i, length, 1, 0)
            open_seq_count += temp[0]
            semi_open_seq_count += temp[1]
            closed_seq_count += temp[2]
            
            temp = detect_row(board, col, 0, i, length, 1, 1)
            open_seq_count += temp[0]
            semi_open_seq_count += temp[1]
            closed_seq_count += temp[2]
            
            temp = detect_row(board, col, i+1, 0, length, 1, 1)
            open_seq_count += temp[0]
            semi_open_seq_count += temp[1]
            closed_seq_count += temp[2]
            
            temp = detect_row(board, col, i-1, 0, length, -1, 1)
            open_seq_count += temp[0]
            semi_open_seq_count += temp[1]
            closed_seq_count += temp[2]
            
            temp = detect_row(board, col, len(board)-1, i, length, -1, 1)
            open_seq_count += temp[0]
            semi_open_seq_count += temp[1]
            closed_seq_count += temp[2]
        
        return open_seq_count, semi_open_seq_count, closed_seq_count

        
    def search_max(board, col):
        
        cur_score = -1000000000000000000
        y_pos = -1
        x_pos = -1
        
        
        for i in range(len(board)):
            for z in range(len(board[0])):
    
                if board[i][z] == " ":
                    board[i][z] = col
                
                    if score(board, col) > cur_score:
                        cur_score = score(board, col)
                        y_pos = i
                        x_pos = z
                
                    board[i][z] = " "
            
        return (y_pos, x_pos)
    
    def score(board, col):
        global a
        MAX_SCORE = 10000000
        
        open_b = {}
        semi_open_b = {}
        closed_b = {}
        open_w = {}
        semi_open_w = {}
        closed_w = {}
        
        for i in range(1, 6):
            open_b[i], semi_open_b[i], closed_b[i] = detect_rows(board, "b", i)
            open_w[i], semi_open_w[i], closed_w[i] = detect_rows(board, "w", i)
        
        threatsw = num_threats(board, "w")
        threatsb = num_threats(board, "b")
        
        #print(threatsw)
        
        moves = 0
        for rows in board:
            for s in rows:
                if s != " ":
                    moves += 1
        #print(moves)
        
        if col =="b":

            if open_b[5] >= 1 or semi_open_b[5]>=1 or closed_b[5]>= 1:
                return MAX_SCORE
            
            elif open_w[5] >= 1 or semi_open_w[5]>=1 or closed_w[5]>= 1:
                return -MAX_SCORE
            
            if moves <= 7:
                return (-1000000 * open_w[4] + -10000 * semi_open_w[4]+  
                        500  * open_b[4]                     +
                        150 * threatsb[0]                    +
                        50 * threatsb[1]                     +
                        5000 * semi_open_b[4]                + 
                        -10000  * open_w[3]                  + 
                        -10000  * threatsw[0]                +
                        -5000   * threatsw[1]                +
                        -300   * semi_open_w[3]              + 
                        50   * open_b[3]                     + 
                        10   * semi_open_b[3]                +  
                        open_b[2]*3 + semi_open_b[2]*2 - open_w[2]*8 - semi_open_w[2]*4 - open_w[1]*.2 - semi_open_w[1]*.1)
            else:
                #print("WE")
                return (-1000000 * open_w[4] + -10000 * semi_open_w[4]+ 
                        5000  * open_b[4]                     +
                        4500 * threatsb[0]                    +
                        3000 * threatsb[1]                    +
                        1000 * semi_open_b[4]                + 
                        -7000  * open_w[3]            + 
                        -10000  * threatsw[0]                +
                        -5000   * threatsw[1]                +
                        -3000   * semi_open_w[3]             + 
                        2000   * open_b[3]                    + 
                        500   * semi_open_b[3]               +
                        open_b[2]*.1 + semi_open_b[2]*.1 - open_w[2]*3 - semi_open_w[2]*2)
                    
        if col =="w":
            if open_w[5] >= 1 or semi_open_w[5]>=1 or closed_w[5]>= 1:
                return MAX_SCORE
            
            elif open_b[5] >= 1 or semi_open_b[5]>=1 or closed_b[5]>= 1:
                return -MAX_SCORE
                
            a = [threatsw[0] , open_b[1], semi_open_b[1], (-100000 * (open_b[4] + semi_open_b[4])+ 
                    500  * open_w[4]                     +
                    150 * threatsw[0]                    +
                    50 * threatsw[1]                     +
                    5000 * semi_open_w[4]                + 
                    -10000  * open_b[3]                  + 
                    -10000  * threatsb[0]                +
                    -5000   * threatsb[1]                +
                    -300   * semi_open_b[3]              + 
                    50   * open_w[3]                     + 
                    10   * semi_open_w[3]                +  
                    open_w[2]*3 + semi_open_w[2]*2 - open_b[2]*8 - semi_open_b[2]*4 - open_b[1]*.2 - semi_open_b[1]*.1)]
            
            if moves <= 7:
                return (-100000 * (open_b[4] + semi_open_b[4])+ 
                        50000  * open_w[4]                     +
                        150 * threatsw[0]                    +
                        50 * threatsw[1]                     +
                        5000 * semi_open_w[4]                + 
                        -10000  * open_b[3]                  + 
                        -10000  * threatsb[0]                +
                        -5000   * threatsb[1]                +
                        -300   * semi_open_b[3]              + 
                        50   * open_w[3]                     + 
                        10   * semi_open_w[3]                +  
                        open_w[2]*3 + semi_open_w[2]*2 - open_b[2]*8 - semi_open_b[2]*4 - open_b[1]*.2 - semi_open_b[1]*.1)
            else:
                #print("WE")
                return (-100000 * (open_b[4] + semi_open_b[4])+ 
                        50000  * open_w[4]                     +
                        2000 * threatsw[0]                    +
                        3000 * threatsw[1]                    +
                        1000 * semi_open_w[4]                + 
                        -7000  * open_b[3]            + 
                        -10000  * threatsb[0]                +
                        -5000   * threatsb[1]                +
                        -3000   * semi_open_b[3]             + 
                        2000   * open_w[3]                    + 
                        500   * semi_open_w[3]               +
                        open_w[2]*.1 + semi_open_w[2]*.1 - open_b[2]*3 - semi_open_b[2]*2)
    
    
    
    
    return search_max(board, col)