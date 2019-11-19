import itertools
import os
import time

def compMove(game,player = 'NA', choice = 'TBA'):

    total_moves = []
    possibleMoves = []

    for i, x in enumerate(game):
        for j in range(len(x)):
            total_moves.append([i,j])
            if (x[j] == '*'):
                possibleMoves.append([i,j])
    #print(possibleMoves)

    for let in ['O', 'X']:
        for row,column in possibleMoves:
            gameCopy = game[:]
            gameCopy[row][column] = let
            if (win(gameCopy,current_player = player)):
                #print(f'Returning {row} {column} from compMove')
                gameCopy[row][column] = '*'
                return row, column
            else:
                gameCopy[row][column] = '*'

    cornersOpen = []
    end_pos = len(game[0])-1
    corners = [[0,0],[0,end_pos],[end_pos,0],[end_pos,end_pos]]
    for i in possibleMoves:
        if(i in corners):
            cornersOpen.append(i)
            
    #print('Corner Moves')
    #print(cornersOpen)
      
    if len(cornersOpen) > 0:
        row,column = selectRandom(cornersOpen)
        return row,column

    game_length = len(game[0])
    if ( game_length % 2 == 1 ):
        row = column = int((game_length + 1) / 2  -1)
        if([row,column] in possibleMoves):
            return row,column
    else:
        centres = [[int((game_length / 2) -1 ),int((game_length / 2) -1 )], [int((game_length + 2) / 2 -1 ), int((game_length + 2) / 2 -1 )]]
        for i in centres:
            if([row,column] in possibleMoves):
                return row, column

    edgesOpen = total_moves[:]
    edges = []
    for i in corners:
        if i in edgesOpen:
            edgesOpen.remove(i)
    for i in possibleMoves:
        if (i in edgesOpen):
            edges.append(i)
            
    if len(edges) > 0:
        row,column = selectRandom(edges)
        return row,column

    return -1,-1
	
	
def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]
	
	
def win(game,current_player = 'NA'):
    # horizontal
    for row in game:
        #print(row)
        if (row.count(row[0]) == len(row) and row[0] != '*'):
            #print(f'Player {current_player} is the winner horizontally!')
            return True

    
    for col in range(len(game[0])):
        check = []
        for row in game:
            check.append(row[col])
        if (check.count(check[0]) == len(check) and check[0] != '*'):
            #print(f'Player {current_player} is the winner vertically!')
            return True
            
    diags = []
    for idx, reverse_idx in enumerate(reversed(range(len(game)))):
        diags.append(game[idx][reverse_idx])
  
    if (diags.count(diags[0]) == len(diags) and diags[0] != '*'):
        #print(f"Player {current_player} has won Diagonally ")
        return True
        
    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])

    if (diags.count(diags[0]) == len(diags) and diags[0] != '*'):
        #print(f'Player {current_player} has won Diagonally')
        return True
        
        
    return False
	
def game_board(game_map, player='NA', row=0, column=0,choice = 'TBA',just_display=False,):
    try:
        #print(row, column)
        #print(f'Player {player} chance to play the game')
        #print(f'Value at {row}{column} is ')
        #print(game_map[row][column])
        if not just_display:
            while(game_map[row][column] != '*'):
                print('Already played the move, please select other positions')
                column = int(input("Which column? "))
                row = int(input("Which row? "))
                #game_board(game_map,player,row,column,choice)
            
          
            game_map[row][column] = choice

        for count, row in enumerate(game_map):
            print(count, row)
        return game_map
    except IndexError:
        print("Did you attempt to play a row or column outside the range ? (IndexError)")
        return False
    except Exception as e:
        print(str(e))
        return False


if __name__ == '__main__':
    
    print("Let's start with Tic Tac Toe")
    time.sleep(3)
    play = True
    won_p1 = 0
    won_p2 = 0
    game = []
    player_1 = input('Name of player 1').lower()
    player_2 = input('Name of player 2').lower()
    while play:
        no_of_moves = 0
        row_choice = -1
        column_choice = -1  #that was made earlier as -11
        game = []
        print('Enter the game board dimensions X x X ')
        dimension = int(input('X : '))
        for i in range(dimension):
            game.append(['*'] * dimension)
            
  
        print('Please wait while we set the gaming environment')
        time.sleep(3)
     
        game_won = False
        player_cycle = itertools.cycle([player_1,player_2])
        choice_select = itertools.cycle('XO')
        
        #Display the game
        game_board(game, just_display=True)
        
        while not game_won:
            current_player = next(player_cycle)
            choice_selection = next(choice_select)
            print(f"Player: {current_player} your turn.")
            if ( current_player == 'comp' or current_player == 'computer'):
                row_choice, column_choice = compMove(game, player = current_player, choice = choice_selection)
                #print(f'Received {row_choice}, {column_choice} from compMove ')
                if (row_choice == -1 or column_choice == -1):
                    print('Match is drawn')
                    break
            else:
                column_choice = int(input("Which column? "))
                row_choice = int(input("Which row? "))
            
            game = game_board(game, player=current_player, row=row_choice, column=column_choice, choice = choice_selection)
            no_of_moves += 1

            
            game_won = win(game,current_player)

            if (game_won):
                if(current_player == player_1):
                    won_p1 +=1
                    print(f'Congratulations {player_1}, you won the game!!')
                else:
                    won_p2 +=1
                    print(f'Sorry, {player_2} won the game :( Better luck next time !!')
                    
            elif(no_of_moves == (dimension*dimension)):
                print('Match is drawn')
                break
                        
        print('Summary of play')
        print('-------------------------')
        print('  Win|Lose')
        print(f'{player_1}  {won_p1}|{won_p2}')
        print(f'{player_2} {won_p2}|{won_p1}')
            
        play = input('Do you want to play again? Type: Y/N ').lower()
        if(play == 'n' or play == 'no'):
            break
    print('Thank you for playing Tic Tac Toe')
	
	
	
