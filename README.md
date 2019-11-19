# TicTacToe_Game

This Game was a Personal Project without using any deep learning libraries and building the logic by learning some amazing tutorial.

<b>Functions</b> : main,compMove,game_board,game,win</br>
<b>Functionality</b>: Can be played between two humans OR human and computer OR computer and computer.</br>
               Can play move out of the game board.</br>
               Can scale upto any dimension board.</br>
               Gets the summary of the win and lose, with text that motivates you to play again.Until the session is not terminated by the  Input 'N' - Quit the game.</br>
               Human cannot win the game, that's the Assurity.</br>
              
Loop Holes Addressed: Once Move Played cannot be played again by any player.</br>
                      Cannot play outside the game_board considered invalid move and give another chance to play your move.</br>


Short Description of Each Function:</br></br>

compMove: Once the play move is done, it checks the possibility of winning the game by player1 and play that relevant move to curtail the chances of winning the game.</br>
It checks the hacks like corners move available, centre moves available, edge moves available etc.</br>

game_board : Sets up the enviroment of the board and starts the game.</br>
game : Takes the input by the player turn and then amending the change by passing it to the gameboard.</br>
win : Win checks is their any winner encountered and return True or False respective.</br>
main : Takes the players name, The input they wanna play on the board and sets the summary of play until the session is terminated.





