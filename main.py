import random
import os
from game_config import *

# function definition - to read the top score players of the game

def fn_game_top_score():
    v_checkfilesize = os.stat(v_scoresfile_name).st_size == 0
    if v_checkfilesize is False:
        with open(v_scoresfile_name) as f:
            tmp_d = f.read()

        data_dic = eval(tmp_d)
        sorted_data_dic = dict(sorted(data_dic.items(), key=lambda item: item[1], reverse=True)[:v_topscorelistnumber])
        print("SCOREBOARD\tList of top {} players\n".format(v_topscorelistnumber))
        print("{:25} {}".format("Player", "Score"))
        for key, value in sorted_data_dic.items():
            print("{:25} {}".format(key, value))
    else:
        pass

# function definition - to add the score of the player in the scoreboard

def fn_game_score(v_player_name):
    v_checkfilesize = os.stat(v_scoresfile_name).st_size == 0
    if v_checkfilesize is False:
        with open(v_scoresfile_name) as f:
            tmp_d = f.read()
        data_dic = eval(tmp_d)
    else:
        data_dic = {}

    v_score = v_winner_points
    v_playername = v_player_name
    if v_playername in data_dic.keys():
        v_playerlastscore = data_dic[v_playername]
        v_playernewscore = v_playerlastscore + v_score
        data_dic[v_playername]=v_playernewscore
    else:
        v_playernewscore = v_score
        data_dic[v_playername]=v_playernewscore

    f = open(v_scoresfile_name, "w")
    f.write( str(data_dic) )
    f.close()

# function definition - to print the lines

def fn_print_lines():
    print("---------------------------------")

# function definition - to ask if the player wants to play game again

def fn_game_again():
    v_game_again_input = input('\nWould you like to play again? Type "y" to play one more time or press something else to exit the game\n')
    if v_game_again_input == 'y' or v_game_again_input == 'Y':
        fn_print_lines()
        print("Let's play again")
        fn_game()
    else:
        fn_print_lines()
        print("Thanks for playing the game")
        fn_print_lines()
        exit()

# function definition - to create the logic for the guesses based on the attempts

def fn_game():
    fn_print_lines()
    from game_config import v_chances
    v_player_input_collection = ''
    print("Start your letter guesses - only {} guess attempts".format(v_chances))
    with open(v_wordfile_name) as v_input_file:
        v_words = v_input_file.read().splitlines()

    v_word_tmp = random.choice(v_words)
    v_word = v_word_tmp.upper()
    real_word = v_word_tmp

    while v_chances > 0:
        v_counter = 0
        for i in v_word:
            if i in v_player_input_collection:
                print(i, end=" ")
            else:
                print("_", end=" ")

                v_counter = v_counter + 1
        print("")
        if v_counter == 0:
            fn_print_lines()
            print("Your guess matched with the word '{}'".format(real_word))
            print("You are a winner ! Got {} points for this win ".format(v_winner_points))
            fn_print_lines()
            fn_game_score(v_name)
            fn_game_top_score()
            break

        print("")
        v_player_input = input("guess a character:").upper()
        print("")

        v_player_input_collection = v_player_input_collection + v_player_input

        if v_player_input not in v_word:
            v_chances = v_chances - 1
            print('Wrong guess, Enter your next guess, Only {} attempt left'.format(v_chances))
            if v_chances == 0:
                print("Guess Not Matched")
                print("You lose")
                fn_print_lines()
                fn_game_top_score()
                print("Game Finished")
                fn_print_lines()

    fn_game_again()

# function calling - to start the game

fn_print_lines()
print("Game Started")
fn_print_lines()
#fn_game_top_score()
v_name = input("Enter the player name : ").upper()
fn_game()



