# pythonwordgame
Python 3 - word guess code

## Steps to run the code ##
Run the below commands to trigger the guess program.

python main.py

This will ask user input for the following:
1. name of the player at the start of the game
2. guess letter but within a defined set of attempts

## Execution order of the game ##
1. It takes the player name
2. It trigger the functions in the below order
        1. fn_game()
            create a secret word from the list of words mentioned in the word file
            reads the player guesses and checks the guesses for a word
        2. fn_game_score()
            if word matches then add 10 points for a user else no points will be added to the scoreboard
            once the guesses finishes or word match is a success then
        3. fn_game_top_score()
            this function displays the top 10 scorer of the game.
        4. fn_game_again()
            this function ask the same player if player wants to play again.
        5. fn_print_lines()
            this function is being called at multiple places to print the dashes.
            
## Current settings for the game ##
List of the parameters set for the game to run:
1. Number of chances user will get to guess = 5
2. Number of points allocated to user in each win = 10
3. Number of top score players to show in start of the game = 10
4. Name of the word file to change the list of the words

## Code Details ##
This code contains the 4 files:

a. main.py:
contains the logic defined in the following different functions.

1. fn_game_top_score()
    To find out the list of top n players score
2. fn_game_score(v_player_name)
    To calculate the new score for an existing or a new player
3. fn_print_lines()
    To print the static lines between the messages
4. fn_game_again()
    If the player wants to play again then press 'y'
5. fn_game()
    To read the input from user and logic to check if the user guess is correct or not

b. game_words.txt:
Contains the list of words each in separate line

c. game_config.py:
contains variables to store the following:
1. v_chances = number of chances user will get to guess
2. v_winner_points = number of points allocated to user in each win
3. v_topscorelistnumber = number of top score players to show in start of the game
4. v_wordfile_name = name of the word file to configure
5. v_scoresfile_name = name of the score file to configure

d. game_scores.txt:
file that will keep the track of the scores for players

## Unit Test Details ##
1. Checked the game if there is no score before and if it is the first time any player is playing, it will not fail due to a check.
2. Currently, the game is not showing any points if the player lose the game as it's 0 but if the player wins then it is 10 points addition to the scoreboard.
3. This game can also be created as an executable code file in later stages.
4. Tested the parameters like number of chances, number of top score displayed in scoreboard in the game.
5. Tested the scenario where the player is passing the name in lower or upper case.
6. Some other checks like alphabet input only can also be applied in later stages.
