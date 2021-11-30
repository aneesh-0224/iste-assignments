game= True
print('welcome to tic-tac-toe')
player=['player2','player1']
print('enter the name of player 1- ')
player[1]=input()
print('enter the name of player 2- ')
player[0]=input()
tt = [['*','*','*'] , ['*','*','*'] , ['*','*','*']]
cha=['o','x']
option ='r'
win=0
while(option):
    print('press r for rules, or press s to skip')
    option=input()
    if(option=='r' or option=='s'):
        break
    else:
        print('invalid option')
#rules of the game
if(option=='r'):
    print('this is a 3 by 3 tic tac toe game. each cell will be initally filled with asteriks.')
    print('press either one of O(alpahbet) or X')

while(game):
    for i in range(3):
        for j in range(3):
            print(tt[i][j], end=' ')
        print('')
        round =1
    while(round<10):
        m = round % 2
        print(f'its {player[m]} turn')
        print(f'print the row and colums number of the cell where {cha[m]} is to be printed ')
        a = 0
        b = 0
        a=int(input())
        b=int(input())
        #checking any error
        if(a<1 or a>3 or b<1 or b>3):
            print('type proper row and column between 1 and 3,both included')
            continue
        if(tt[a-1][b-1]=='x' or tt[a-1][b-1]=='o'):
            print('type proper row and column number.the present cell has been taken')
            continue
        tt[a - 1][b - 1] = cha[m]
        round+=1
        # displaying the matrix again
        for i in range(3):
            for j in range(3):
                print(tt[i][j], end=' ')
            print('')

        # checking whether a player has won
        if ((a == 1 and b == 1) or (a == 3 and b == 3)):
            if (tt[0][0] == tt[1][1] and tt[1][1] == tt[2][2]):
                print(f'{player[m]} wins')
                win=1
                break
        elif ((a == 1 and b == 3) or (a == 3 and b == 1)):
            if ((tt[2][0] == tt[1][1]) and (tt[1][1] == tt[0][2])):
                print(f'{player[m]} wins')
                win = 1
                break
        same_r = 0
        for i in range(0, 2):
            if (tt[a - 1][i] == tt[a - 1][i + 1]):
                same_r += 1
        if (same_r == 2):
            print(f'{player[m]} wins')
            win = 1
            break
        same_c = 0
        for i in range(0, 2):
            if (tt[i][b - 1] == tt[i + 1][b - 1]):
                same_c += 1
        if (same_c == 2):
            print(f'{player[m]} wins')
            win = 1
            break
        if (a == 2 and b == 2):
            if (tt[0][0] == tt[1][1] and tt[1][1] == tt[2][2]):
                print(f'{player[m]} wins')
                win = 1
                break
            if ((tt[2][0] == tt[1][1]) and (tt[1][1] == tt[0][2])):
                print(f'{player[m]} wins')
                win = 1
                break
    #after the game has finished
    if(not win):
        print('tiee!!')
    print('press p to play again and press q to quit')
    op = 'q'
    op = input()
    if (op == 'q'):
        game = False
    else:
        game = True
        for i in range(3):
            for j in range(3):
                tt[i][j] = 0

print('thanks for playing the game:)')

























