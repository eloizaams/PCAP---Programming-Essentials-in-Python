board = [[" " for i in range(3)]for j in range(3)]
k=1
player_X = "X"
plyer_O = "O"

for i in range(3):
    for j in range(3):
        if k != 5:
            board[i][j] = k
        else:
            board[i][j] = player_X
        k+=1
      
def display_board(board): 
    num = " "
    str_number = ('"|"," "*3,') + num + " "*3
    for i in range(3):
        print (("+"+"-"*7)*3+ "+")
        print (("|"+" "*7)*3+ "|")
        for j in range(3):
            num = str(board[i][j])
            print("|"," ", num, " "*2, end="")
        print (""*3+"|")    
        print (("|"+" "*7)*3+ "|")
    print (("+"+"-"*7)*3+ "+")  
        
def victory_for(board, sign):
    return ((board[0][0]==sign and board [0][1]==sign and board [0][2]==sign) or
            (board[1][0]==sign and board [1][1]==sign and board [1][2]==sign) or
            (board[2][0]==sign and board [2][1]==sign and board [2][2]==sign) or
            (board[0][0]==sign and board [1][0]==sign and board [2][0]==sign) or
            (board[0][1]==sign and board [1][1]==sign and board [2][1]==sign) or
            (board[0][2]==sign and board [1][2]==sign and board [2][2]==sign) or
            (board[0][0]==sign and board [1][1]==sign and board [2][2]==sign) or
            (board[0][2]==sign and board [1][1]==sign and board [2][0]==sign) )

def make_list_of_free_fields(board):
    list = []
    for i in range(3):
        for j in range(3):
            if type(board [i][j]) == int:
                position = (i,j)     
                list.append(position)   
    return list  

def enter_move(board):  
    move = int(input("Enter your move: "))
    if move not in range(1,10):
        return False
    for position in make_list_of_free_fields(board):
            if board[position[0]][position[1]] == move:
                board[position[0]][position[1]] = plyer_O
                display_board(board)    
                return True
    return False
                 
def draw_move(board):
    from random import randrange
    move =randrange(8)+1
    print("numero gerado", move)
    for position in make_list_of_free_fields(board):
            if board[position[0]][position[1]] == move:
                board[position[0]][position[1]] = player_X
                display_board(board)    
                return True
    return False
            
def game(board):
    
    make_list_of_free_fields(board)
    display_board(board)
    while True:
        if len(make_list_of_free_fields(board))==0:
            return None    
        while True:
            if enter_move(board)==True:
                if victory_for(board, plyer_O) ==True:
                    return plyer_O
                else:
                    break         
        while True:
            if draw_move(board)==True:
                if victory_for(board, player_X) ==True:
                    return player_X
                else:
                    break
                       
winner = game(board)  
    
if (winner == player_X):
    print ("You lost")
elif (winner == plyer_O):
    print ("You win")
else:
    print("Cat's game!")
