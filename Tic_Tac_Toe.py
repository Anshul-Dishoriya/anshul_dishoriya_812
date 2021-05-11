import os 
os.system("cls")
print('Tic Tac Toe'.center(50,"-"))
b = [[' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ' ,' ', ' ']]

def format_board(b):
    board = "|{:^10}"*3+"|"
    txt = "|{:^10}"*3+"|"
    for row in b:
        print(("-"*34).center(100))
        print(txt.format(" "," ", " ").center(100))
        print(board.format(*row).center(100))
        print(txt.format(" "," ", " ").center(100))
    print(("-"*34).center(100))
format_board(b)
player1 = input("Enter your choice X / O  :   ").upper().strip()
if player1 !="X" and player1  != "O":
    print("Invalid Choice (Now your Choice will be 'X') ".rjust(50))
    player1 = "X"
if player1 == "X" :
    player2 = "O" 
else:
    player2 ="X"


chances  = 9
def tic_tac_toe(chances):
    while chances:
        if (chances-1)%2==0:
            print(f"Player 1 chance {player1}".rjust(50))
            n = int(input("Enter the position (0 - 9) :-".rjust(50)))
            val = player1
        else:
            print(f"Player 2 chance {player2} ".rjust(50))
            n = int(input("Enter the position (0 - 9) :-".rjust(50)))
            val = player2
        if n>9:
            print("\nInvalid Index".rjust(50))
            tic_tac_toe(chances)
        i = (n-1)//3
        j = (n-1)%3
        if b[i][j] == "X" or b[i][j] == "O":
            print("\n\nAlready Filled! Index".rjust(50))
            print("\nPlease Enter Other Index ".rjust(50))
            tic_tac_toe(chances)
        else:
            pass
        b[i][j] = val

        os.system("cls")
        format_board(b)


        winboard=[( b[0][0] , b[0][1] , b[0][2]),
                ( b[1][0] , b[1][1] , b[1][2]),
                ( b[2][0] , b[2][1] , b[2][2]), 
                
                ( b[0][0] , b[1][0] , b[2][0]),
                ( b[0][1] , b[1][1] , b[2][1]),
                ( b[0][2] , b[1][2] , b[2][2]),
                ( b[0][0] , b[1][1] , b[2][2]),
                ( b[0][2] , b[1][1] , b[2][0]),]


        if (player1,player1,player1) in winboard:
            print('\n\n\nPlayer-1 Won the Mathch'.center(50,"-"))
            break
        if (player2,player2,player2) in winboard:
            print('\n\n\nPlayer-2 Won the Mathch'.center(50,'-'))
            break
        chances = chances -1
    else:
        print("\n\n\nDraw".center(50,"-"))

tic_tac_toe(chances)



