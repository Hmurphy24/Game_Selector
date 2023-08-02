import random

########################################################################################################################


def game_selector_greeting():

    print()

    print('Welcome to the Game Selector!')

    print()

    print('The current available games are "Rock, Paper Scissors" (RPS), "Twenty-One" (21), "Tic-Tac-Toe (TTT), '
          'the "Python Quiz" (PQ), "Hang Man" (HM), "Go Fish" (GF), "Uno" (1) and "War"!')

    print()


def game_selector_hub():

    while True:

        user_game_input = input('Enter the game you would like to play, or if you need help type "Help" if you want me '
                                'state the different games. Or if you don\'t want to play anything type "Quit" ')

        if (user_game_input.upper() == 'RPS') or (user_game_input.upper() == 'ROCK, PAPER SCISSORS'):

            rock_paper_scissors_game()

        elif (user_game_input.upper() == 'TWENTY-ONE') or (user_game_input.upper() == '21'):

            twenty_one_game()

        elif (user_game_input.upper() == 'TIC-TAC-TOE') or (user_game_input.upper() == 'TTT'):

            tic_tac_toe_game()

        elif (user_game_input.upper() == 'PYTHON QUIZ') or (user_game_input.upper() == 'PQ'):

            python_quiz_game()

        elif (user_game_input.upper() == 'HANG MAN') or (user_game_input.upper() == 'HM'):

            hang_man_game()

        elif user_game_input.upper() == 'HELP':

            print()

            print('The current available games are "Rock, Paper Scissors" (RPS), "Twenty-One" (21), "Tic-Tac-Toe (TTT), the "Python Quiz" (PQ), "Hang Man" (HM), "Go Fish (GF) and "Uno" (1)!')

            print()

        elif (user_game_input.upper() == 'GO FISH') or (user_game_input.upper() == 'GF'):

            go_fish_game()

        elif (user_game_input.upper() == 'UNO') or (user_game_input.upper() == '1'):

            uno_game()

        elif user_game_input.upper() == 'WAR':

            war_game()

        elif user_game_input.upper() == 'QUIT':

            print('See you later alligator!')

            exit()

        else:

            print('Please type in a valid input!')

########################################################################################################################


def rock_paper_scissors_game():

    rock_paper_scissors_dictionary = {'Wins': 0, 'Losses': 0, 'Ties': 0, 'Games Played': 0}

    def rock_paper_scissors_game_rules():

        print()

        print('Welcome to Rock, Paper Scissors! Try your best to beat the computer!')

        print()

    def rock_paper_scissors_weapon_picker():

        rock_paper_scissors_weapons = ['ROCK', 'PAPER', 'SCISSORS']

        rock_paper_scissors_computer_weapon = random.choice(rock_paper_scissors_weapons)

        while True:

            rock_paper_scissors_user_weapon = input('Do you want to use Rock, Paper or Scissors? ')

            if rock_paper_scissors_user_weapon.upper() in rock_paper_scissors_weapons:

                break

            else:

                print('Please pick Rock, Paper or Scissors!')

        return rock_paper_scissors_computer_weapon.upper(), rock_paper_scissors_user_weapon.upper()

    def rock_paper_scissors_outcome_calc(computer_weapon, user_weapon):

        if computer_weapon == user_weapon:

            print('You and the computer both picked the same thing!')

            rock_paper_scissors_dictionary['Ties'] += 1

        elif computer_weapon == 'ROCK' and user_weapon == 'SCISSORS':

            print('The computer crushed your scissors!')

            rock_paper_scissors_dictionary['Losses'] += 1

        elif computer_weapon == 'PAPER' and user_weapon == 'ROCK':

            print('The computer covered your rock!')

            rock_paper_scissors_dictionary['Losses'] += 1

        elif computer_weapon == 'SCISSORS' and user_weapon == 'PAPER':

            print('The computer cut your paper!')

            rock_paper_scissors_dictionary['Losses'] += 1

        elif user_weapon == 'ROCK' and computer_weapon == 'SCISSORS':

            print('You crushed the computer\'s scissors!')

            rock_paper_scissors_dictionary['Wins'] += 1

        elif user_weapon == 'PAPER' and computer_weapon == 'ROCK':

            print('You covered the computer\'s rock!')

            rock_paper_scissors_dictionary['Wins'] += 1

        elif user_weapon == 'SCISSORS' and computer_weapon == 'PAPER':

            print('You cut the computer\'s paper!')

            rock_paper_scissors_dictionary['Wins'] += 1

    def rock_paper_scissors_replay():

        print()

        print('Here\'s the score:')

        print(rock_paper_scissors_dictionary)

        print()

        while True:

            rock_paper_scissors_replay_input = input('Do you want to play again? ')

            if rock_paper_scissors_replay_input.upper() == 'YES':

                print('Okay, here we go again!')

                print()

                break

            elif rock_paper_scissors_replay_input.upper() == 'NO':

                print('Okay, I\'ll see you later!')

                print()

                game_selector_hub()

                break

            else:

                print('Please enter either "Yes" or "No"!')

    rock_paper_scissors_game_rules()

    while True:

        rock_paper_scissors_computer_user_weapons = rock_paper_scissors_weapon_picker()

        rock_paper_scissors_outcome_calc(rock_paper_scissors_computer_user_weapons[0], rock_paper_scissors_computer_user_weapons[1])

        rock_paper_scissors_dictionary['Games Played'] += 1

        rock_paper_scissors_replay()

########################################################################################################################


def twenty_one_game():

    twenty_one_card_dictionary = {'Ace': 0, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10}

    twenty_one_score_dictionary = {'Wins': 0, 'Losses': 0, 'Ties': 0, 'Games Played': 0}

    def twenty_one_rules():

        print()

        print('Welcome to 21! Try and get as close to 21 as possible!')

        print()

        print('If you go over 21 you lose! The same applies if the computer goes over 21, then it loses!')

        print('The deck will be shuffled an indicated amount of times and will be distributed between you and the computer.')

        print('When prompted, type either you want a card or not, the player with the highest number wins! (Given that you didn\'t bust!)')

        print()

        print('Good luck!')

        print()

    def twenty_one_deck_maker():

        twenty_one_entire_card_deck = []

        twenty_one_suit_deck = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

        twenty_one_deck_counter = 0

        while twenty_one_deck_counter < 4:

            for card in twenty_one_suit_deck:

                twenty_one_entire_card_deck.append(card)

            twenty_one_deck_counter += 1

        while True:

            twenty_one_times_shuffled = input('How many times do you want the deck to be shuffled? ')

            if twenty_one_times_shuffled.isdigit():

                twenty_one_shuffles = int(twenty_one_times_shuffled)

                break

            else:

                print('Type in an integer!')

                print()

        print('The deck will be shuffled {} time(s)!'.format(twenty_one_shuffles))

        while twenty_one_shuffles > 0:

            random.shuffle(twenty_one_entire_card_deck)

            twenty_one_shuffles -= 1

        return twenty_one_entire_card_deck

    def twenty_one_gameplay(card_deck):

        twenty_one_user_hand = []

        twenty_one_computer_hand_hidden = []

        twenty_one_computer_hand_visible = []

        twenty_one_first_card = 0

        while twenty_one_first_card < 2:

            twenty_one_user_hand.append(card_deck[0])

            card_deck.remove(card_deck[0])

            twenty_one_computer_hand_hidden.append(card_deck[0])

            card_deck.remove(card_deck[0])

            twenty_one_first_card += 1

        twenty_one_computer_hand_visible.append(twenty_one_computer_hand_hidden[0])

        twenty_one_computer_hand_visible.append('X')

        print()

        print('Your Hand:')

        print(twenty_one_user_hand)

        print()

        print('Computer\'s Hand:')

        print(twenty_one_computer_hand_visible)

        print()

        twenty_one_user_hand_value = 0

        for card in twenty_one_user_hand:

            if card == 'Ace':

                while True:

                    twenty_one_ace_value = input('Do you want your Ace to have a value of 1 or 11? ')

                    if twenty_one_ace_value.isdigit():

                        if (twenty_one_ace_value == '1') or (twenty_one_ace_value == '11'):

                            twenty_one_user_hand_value = twenty_one_user_hand_value + int(twenty_one_ace_value)

                            break

                        else:

                            print('The value has to be 1 or 11!')

                            print()

                    else:

                        print('Type in either "1" or "11".')

                        print()

            else:

                twenty_one_user_hand_value = twenty_one_user_hand_value + twenty_one_card_dictionary[card]

        twenty_one_computer_hand_value = 0

        for card in twenty_one_computer_hand_hidden:

            if card == 'Ace':

                if twenty_one_computer_hand_value <= 10:

                    twenty_one_computer_hand_value = twenty_one_computer_hand_value + 11

                else:

                    twenty_one_computer_hand_value = twenty_one_computer_hand_value + 1

            else:

                twenty_one_computer_hand_value = twenty_one_computer_hand_value + twenty_one_card_dictionary[card]

        twenty_one_user_stay_counter = 0

        twenty_one_computer_stay_counter = 0

        while True:

            if (twenty_one_user_stay_counter == 1) and (twenty_one_computer_stay_counter == 1):

                print('Okay, you and the computer both want to stay!')

                print()

                break

            if twenty_one_user_hand_value == 21:

                print('You got 21! Congrats!')

                print()

                break

            elif twenty_one_user_hand_value > 21:

                print('You went over 21! You busted!')

                print()

                break

            else:

                print('Your hand\'s current value is {}.'.format(twenty_one_user_hand_value))

                print()

                while True:

                    twenty_one_user_input = input('Do you want to draw a card? ("Yes"/"No") ')

                    if twenty_one_user_input.upper() == 'YES':

                        print('You drew a card!')

                        print()

                        twenty_one_card_draw = card_deck[0]

                        twenty_one_user_hand.append(twenty_one_card_draw)

                        card_deck.remove(twenty_one_card_draw)

                        if twenty_one_card_draw == 'Ace':

                            while True:

                                twenty_one_ace_value = input('Do you want your Ace to have a value of 1 or 11? ')

                                if twenty_one_ace_value.isdigit():

                                    if (twenty_one_ace_value == '1') or (twenty_one_ace_value == '11'):

                                        twenty_one_user_hand_value = twenty_one_user_hand_value + int(twenty_one_ace_value)

                                        break

                                    else:

                                        print('The value has to be 1 or 11!')

                                        print()

                                else:

                                    print('Type in either "1" or "11".')

                                    print()

                        else:

                            twenty_one_user_hand_value = twenty_one_user_hand_value + twenty_one_card_dictionary[twenty_one_card_draw]

                            break

                    elif twenty_one_user_input.upper() == 'NO':

                        twenty_one_user_stay_counter = 1

                        print('Okay, you decided to stay.')

                        print()

                        break

                    else:

                        print('Please enter either "Yes" or "No".')

                        print()

            if twenty_one_computer_hand_value == 21:

                print('The computer got 21!')

                print()

                break

            elif twenty_one_computer_hand_value > 21:

                print('The computer busted!')

                print()

                break

            elif 16 <= twenty_one_computer_hand_value <= 20:

                twenty_one_computer_stay_counter = 1

                print('The computer decided to stay!')

                print()

            else:

                print('The computer drew a card!')

                twenty_one_computer_hand_hidden.append(card_deck[0])

                twenty_one_computer_hand_value = twenty_one_computer_hand_value + twenty_one_card_dictionary[card_deck[0]]

                card_deck.remove(card_deck[0])

                twenty_one_computer_hand_visible.append('X')

                print()

            print('Your Hand:')

            print(twenty_one_user_hand)

            print()

            print('Computer\'s Hand:')

            print(twenty_one_computer_hand_visible)

            print()

            if (twenty_one_user_stay_counter == 1) and (twenty_one_computer_stay_counter == 1):

                print('Okay, you and the computer both want to stay!')

                print()

                break

        print('Ending Hands:')

        print()

        print('Your Hand:')

        print(twenty_one_user_hand)

        print('Hand value: {}'.format(twenty_one_user_hand_value))

        print()

        print('Computer\'s Hand:')

        print(twenty_one_computer_hand_hidden)

        print('Hand value: {}'.format(twenty_one_computer_hand_value))

        print()

        return twenty_one_user_hand_value, twenty_one_computer_hand_value

    def twenty_one_replay(user_value, computer_value):

        if (user_value > 21) and (computer_value > 21):

            print('You and the computer both busted!')

            print()

            twenty_one_score_dictionary['Ties'] += 1

        elif user_value == computer_value:

            print('You tied with the computer!')

            print()

            twenty_one_score_dictionary['Ties'] += 1

        elif (user_value < 22) and (computer_value > 21):

            print('You win since the computer busted!')

            print()

            twenty_one_score_dictionary['Wins'] += 1

        elif (user_value < 22) and (computer_value < 22) and (user_value > computer_value):

            print('You won since you had a higher score than the computer!')

            print()

            twenty_one_score_dictionary['Wins'] += 1

        elif (user_value > 21) and (computer_value < 22):

            print('You lost since you busted!')

            print()

            twenty_one_score_dictionary['Losses'] += 1

        elif (user_value < 22) and (computer_value < 22) and (computer_value > user_value):

            print('You lost since the computer had a higher score than you!')

            print()

            twenty_one_score_dictionary['Losses'] += 1

        print('Here\'s the score:')

        print(twenty_one_score_dictionary)

        print()

        while True:

            twenty_one_replay_input = input('Would you like to play again? ("Yes"/"No") ')

            if twenty_one_replay_input.upper() == 'YES':

                print('Okay, let\'s go again!')

                print()

                break

            elif twenty_one_replay_input.upper() == 'NO':

                print('Okay, have a good day!')

                print()

                game_selector_hub()

            else:

                print('Please type either "Yes" or "No"!')

                print()

    twenty_one_rules()

    while True:

        twenty_one_gameplay_deck = twenty_one_deck_maker()

        twenty_one_hand_values = twenty_one_gameplay(twenty_one_gameplay_deck)

        twenty_one_score_dictionary['Games Played'] += 1

        twenty_one_replay(twenty_one_hand_values[0], twenty_one_hand_values[1])

########################################################################################################################


def tic_tac_toe_game():

    tic_tac_toe_dictionary = {'Wins': 0, 'Losses': 0, 'Ties': 0, 'Games Played': 0}

    tic_tac_toe_board_unseen = [' ', ' ', ' ',
                                ' ', ' ', ' ',
                                ' ', ' ', ' ']

    def tic_tac_toe_game_rules():

        print()

        print('Welcome to Tic Tac Toe! Try to get your X\'s to be three in a row!')

        print()

        print('Here is the board.')

        print()

        print('1 | 2 | 3')
        print('----------')
        print('4 | 5 | 6')
        print('----------')
        print('7 | 8 | 9')

        print()

        print('The numbers correspond to the places in which you, or the computer, can put an "X" or "O".')

        print()

        print('There will be a coin toss to see who goes first.')

        print()

    def tic_tac_toe_coin_toss():

        tic_tac_toe_coin = random.randint(0, 1)

        tic_tac_toe_user_coin = input('Do you pick heads or tales? ("1" for heads, "0" for tales) ')

        if (tic_tac_toe_user_coin != '0') and (tic_tac_toe_user_coin != '1'):

            print('Input either "1" for heads or "0" for tales!')

            return tic_tac_toe_coin_toss()

        elif int(tic_tac_toe_user_coin) != tic_tac_toe_coin:

            print('The computer won the coin toss!')

            tic_tac_toe_first_turn = 0

        else:

            print('You won the coin toss!')

            tic_tac_toe_first_turn = 1

        return tic_tac_toe_first_turn

    def tic_tac_toe_gameplay_hub(tic_tac_toe_player_1):

        if tic_tac_toe_player_1 == 0:

            tic_tac_toe_computer_player_1()

        elif tic_tac_toe_player_1 == 1:

            tic_tac_toe_user_player_1()

    def tic_tac_toe_computer_player_1():

        tic_tac_toe_computer_turns = 5

        print()

        print('The computer gets the first move.')

        print()

        while True:

            while True:

                tic_tac_toe_computer_index = random.randint(0, 8)

                if (tic_tac_toe_board_unseen[tic_tac_toe_computer_index] != 'O') and (tic_tac_toe_board_unseen[tic_tac_toe_computer_index] != 'X'):

                    tic_tac_toe_board_unseen[tic_tac_toe_computer_index] = 'O'

                    tic_tac_toe_computer_turns -= 1

                    print('The computer placed its\' "O"!')

                    print(tic_tac_toe_board_unseen[0], ' | ', tic_tac_toe_board_unseen[1], ' | ',tic_tac_toe_board_unseen[2])
                    print('--------------')
                    print(tic_tac_toe_board_unseen[3], ' | ', tic_tac_toe_board_unseen[4], ' | ',tic_tac_toe_board_unseen[5])
                    print('--------------')
                    print(tic_tac_toe_board_unseen[6], ' | ', tic_tac_toe_board_unseen[7], ' | ',tic_tac_toe_board_unseen[8])

                    print()

                    break

                else:

                    continue

            if tic_tac_toe_board_unseen[0] == 'O' and tic_tac_toe_board_unseen[1] == 'O' and tic_tac_toe_board_unseen[2] == 'O':

                print('The computer got three in a row!')

                tic_tac_toe_dictionary['Losses'] += 1

                break

            elif tic_tac_toe_board_unseen[3] == 'O' and tic_tac_toe_board_unseen[4] == 'O' and tic_tac_toe_board_unseen[5] == 'O':

                print('The computer got three in a row!')

                tic_tac_toe_dictionary['Losses'] += 1

                break

            elif tic_tac_toe_board_unseen[6] == 'O' and tic_tac_toe_board_unseen[7] == 'O' and tic_tac_toe_board_unseen[8] == 'O':

                print('The computer got three in a row!')

                tic_tac_toe_dictionary['Losses'] += 1

                break

            elif tic_tac_toe_board_unseen[0] == 'O' and tic_tac_toe_board_unseen[3] == 'O' and tic_tac_toe_board_unseen[6] == 'O':

                print('The computer got three in a row!')

                tic_tac_toe_dictionary['Losses'] += 1

                break

            elif tic_tac_toe_board_unseen[1] == 'O' and tic_tac_toe_board_unseen[4] == 'O' and tic_tac_toe_board_unseen[7] == 'O':

                print('The computer got three in a row!')

                tic_tac_toe_dictionary['Losses'] += 1

                break

            elif tic_tac_toe_board_unseen[2] == 'O' and tic_tac_toe_board_unseen[5] == 'O' and tic_tac_toe_board_unseen[8] == 'O':

                print('The computer got three in a row!')

                tic_tac_toe_dictionary['Losses'] += 1

                break

            elif tic_tac_toe_board_unseen[0] == 'O' and tic_tac_toe_board_unseen[4] == 'O' and tic_tac_toe_board_unseen[8] == 'O':

                print('The computer got three in a row!')

                tic_tac_toe_dictionary['Losses'] += 1

                break

            elif tic_tac_toe_board_unseen[2] == 'O' and tic_tac_toe_board_unseen[4] == 'O' and tic_tac_toe_board_unseen[6] == 'O':

                print('The computer got three in a row!')

                tic_tac_toe_dictionary['Losses'] += 1

                break

            elif tic_tac_toe_computer_turns == 0:

                print('The game is a tie!')

                tic_tac_toe_dictionary['Ties'] += 1

                break

            while True:

                tic_tac_toe_user_index = input('Enter the position where you want to put your "X" (A number from 1 to 9)): ')

                if (tic_tac_toe_user_index != '1') and (tic_tac_toe_user_index != '2') and (tic_tac_toe_user_index != '3') and (tic_tac_toe_user_index != '4') and (tic_tac_toe_user_index != '5') and (tic_tac_toe_user_index != '6') and (tic_tac_toe_user_index != '7') and (tic_tac_toe_user_index != '8') and (tic_tac_toe_user_index != '9'):

                    print('Please input a valid position!')

                elif tic_tac_toe_board_unseen[int(tic_tac_toe_user_index) - 1] == 'O':

                    print('The computer already has an "O" in this position!')

                elif tic_tac_toe_board_unseen[int(tic_tac_toe_user_index) - 1] == 'X':

                    print('You already have an "X" in this position!')

                else:

                    tic_tac_toe_board_unseen[int(tic_tac_toe_user_index) - 1] = 'X'

                    print('You placed your "X"!')

                    print(tic_tac_toe_board_unseen[0], ' | ', tic_tac_toe_board_unseen[1], ' | ',tic_tac_toe_board_unseen[2])
                    print('--------------')
                    print(tic_tac_toe_board_unseen[3], ' | ', tic_tac_toe_board_unseen[4], ' | ',tic_tac_toe_board_unseen[5])
                    print('--------------')
                    print(tic_tac_toe_board_unseen[6], ' | ', tic_tac_toe_board_unseen[7], ' | ',tic_tac_toe_board_unseen[8])

                    print()

                    break

            if tic_tac_toe_board_unseen[0] == 'X' and tic_tac_toe_board_unseen[1] == 'X' and tic_tac_toe_board_unseen[2] == 'X':

                print('You got three in a row!')

                tic_tac_toe_dictionary['Wins'] += 1

                break

            elif tic_tac_toe_board_unseen[3] == 'X' and tic_tac_toe_board_unseen[4] == 'X' and tic_tac_toe_board_unseen[5] == 'X':

                print('You got three in a row!')

                tic_tac_toe_dictionary['Wins'] += 1

                break

            elif tic_tac_toe_board_unseen[6] == 'X' and tic_tac_toe_board_unseen[7] == 'X' and tic_tac_toe_board_unseen[8] == 'X':

                print('You got three in a row!')

                tic_tac_toe_dictionary['Wins'] += 1

                break

            elif tic_tac_toe_board_unseen[0] == 'X' and tic_tac_toe_board_unseen[3] == 'X' and tic_tac_toe_board_unseen[6] == 'X':

                print('You got three in a row!')

                tic_tac_toe_dictionary['Wins'] += 1

                break

            elif tic_tac_toe_board_unseen[1] == 'X' and tic_tac_toe_board_unseen[4] == 'X' and tic_tac_toe_board_unseen[7] == 'X':

                print('You got three in a row!')

                tic_tac_toe_dictionary['Wins'] += 1

                break

            elif tic_tac_toe_board_unseen[2] == 'X' and tic_tac_toe_board_unseen[5] == 'X' and tic_tac_toe_board_unseen[8] == 'X':

                print('You got three in a row!')

                tic_tac_toe_dictionary['Wins'] += 1

                break

            elif tic_tac_toe_board_unseen[0] == 'X' and tic_tac_toe_board_unseen[4] == 'X' and tic_tac_toe_board_unseen[8] == 'X':

                print('You got three in a row!')

                tic_tac_toe_dictionary['Wins'] += 1

                break

            elif tic_tac_toe_board_unseen[2] == 'X' and tic_tac_toe_board_unseen[4] == 'X' and tic_tac_toe_board_unseen[6] == 'X':

                print('You got three in a row!')

                tic_tac_toe_dictionary['Wins'] += 1

                break

    def tic_tac_toe_user_player_1():

        tic_tac_toe_user_turns = 5

        print()

        print('You get the first move.')

        print()

        while True:

            while True:

                tic_tac_toe_user_index = input('Enter the position where you want to put your "X" (A number from 1 to 9)): ')

                if (tic_tac_toe_user_index != '1') and (tic_tac_toe_user_index != '2') and (tic_tac_toe_user_index != '3') and (tic_tac_toe_user_index != '4') and (tic_tac_toe_user_index != '5') and (tic_tac_toe_user_index != '6') and (tic_tac_toe_user_index != '7') and (tic_tac_toe_user_index != '8') and (tic_tac_toe_user_index != '9'):

                    print('Please input a valid position!')

                elif tic_tac_toe_board_unseen[int(tic_tac_toe_user_index) - 1] == 'O':

                    print('The computer already has an "O" in this position!')

                elif tic_tac_toe_board_unseen[int(tic_tac_toe_user_index) - 1] == 'X':

                    print('You already have an "X" in this position!')

                else:

                    tic_tac_toe_board_unseen[int(tic_tac_toe_user_index) - 1] = 'X'

                    tic_tac_toe_user_turns -= 1

                    print('You placed your "X"!')

                    print(tic_tac_toe_board_unseen[0], ' | ', tic_tac_toe_board_unseen[1], ' | ',tic_tac_toe_board_unseen[2])
                    print('--------------')
                    print(tic_tac_toe_board_unseen[3], ' | ', tic_tac_toe_board_unseen[4], ' | ',tic_tac_toe_board_unseen[5])
                    print('--------------')
                    print(tic_tac_toe_board_unseen[6], ' | ', tic_tac_toe_board_unseen[7], ' | ',tic_tac_toe_board_unseen[8])

                    print()

                    break

            if tic_tac_toe_board_unseen[0] == 'X' and tic_tac_toe_board_unseen[1] == 'X' and tic_tac_toe_board_unseen[2] == 'X':

                print('You got three in a row!')

                tic_tac_toe_dictionary['Wins'] += 1

                break

            elif tic_tac_toe_board_unseen[3] == 'X' and tic_tac_toe_board_unseen[4] == 'X' and tic_tac_toe_board_unseen[5] == 'X':

                print('You got three in a row!')

                tic_tac_toe_dictionary['Wins'] += 1

                break

            elif tic_tac_toe_board_unseen[6] == 'X' and tic_tac_toe_board_unseen[7] == 'X' and tic_tac_toe_board_unseen[8] == 'X':

                print('You got three in a row!')

                tic_tac_toe_dictionary['Wins'] += 1

                break

            elif tic_tac_toe_board_unseen[0] == 'X' and tic_tac_toe_board_unseen[3] == 'X' and tic_tac_toe_board_unseen[6] == 'X':

                print('You got three in a row!')

                tic_tac_toe_dictionary['Wins'] += 1

                break

            elif tic_tac_toe_board_unseen[1] == 'X' and tic_tac_toe_board_unseen[4] == 'X' and tic_tac_toe_board_unseen[7] == 'X':

                print('You got three in a row!')

                tic_tac_toe_dictionary['Wins'] += 1

                break

            elif tic_tac_toe_board_unseen[2] == 'X' and tic_tac_toe_board_unseen[5] == 'X' and tic_tac_toe_board_unseen[8] == 'X':

                print('You got three in a row!')

                tic_tac_toe_dictionary['Wins'] += 1

                break

            elif tic_tac_toe_board_unseen[0] == 'X' and tic_tac_toe_board_unseen[4] == 'X' and tic_tac_toe_board_unseen[8] == 'X':

                print('You got three in a row!')

                tic_tac_toe_dictionary['Wins'] += 1

                break

            elif tic_tac_toe_board_unseen[2] == 'X' and tic_tac_toe_board_unseen[4] == 'X' and tic_tac_toe_board_unseen[6] == 'X':

                print('You got three in a row!')

                tic_tac_toe_dictionary['Wins'] += 1

                break

            elif tic_tac_toe_user_turns == 0:

                print('The game is a tie!')

                tic_tac_toe_dictionary['Ties'] += 1

                break

            while True:

                tic_tac_toe_computer_index = random.randint(0, 8)

                if (tic_tac_toe_board_unseen[tic_tac_toe_computer_index] != 'O') and (tic_tac_toe_board_unseen[tic_tac_toe_computer_index] != 'X'):

                    tic_tac_toe_board_unseen[tic_tac_toe_computer_index] = 'O'

                    print('The computer placed its\' "O"!')

                    print(tic_tac_toe_board_unseen[0], ' | ', tic_tac_toe_board_unseen[1], ' | ',tic_tac_toe_board_unseen[2])
                    print('--------------')
                    print(tic_tac_toe_board_unseen[3], ' | ', tic_tac_toe_board_unseen[4], ' | ',tic_tac_toe_board_unseen[5])
                    print('--------------')
                    print(tic_tac_toe_board_unseen[6], ' | ', tic_tac_toe_board_unseen[7], ' | ',tic_tac_toe_board_unseen[8])

                    print()

                    break

                else:

                    continue

            if tic_tac_toe_board_unseen[0] == 'O' and tic_tac_toe_board_unseen[1] == 'O' and tic_tac_toe_board_unseen[2] == 'O':

                print('The computer got three in a row!')

                tic_tac_toe_dictionary['Losses'] += 1

                break

            elif tic_tac_toe_board_unseen[3] == 'O' and tic_tac_toe_board_unseen[4] == 'O' and tic_tac_toe_board_unseen[5] == 'O':

                print('The computer got three in a row!')

                tic_tac_toe_dictionary['Losses'] += 1

                break

            elif tic_tac_toe_board_unseen[6] == 'O' and tic_tac_toe_board_unseen[7] == 'O' and tic_tac_toe_board_unseen[8] == 'O':

                print('The computer got three in a row!')

                tic_tac_toe_dictionary['Losses'] += 1

                break

            elif tic_tac_toe_board_unseen[0] == 'O' and tic_tac_toe_board_unseen[3] == 'O' and tic_tac_toe_board_unseen[6] == 'O':

                print('The computer got three in a row!')

                tic_tac_toe_dictionary['Losses'] += 1

                break

            elif tic_tac_toe_board_unseen[1] == 'O' and tic_tac_toe_board_unseen[4] == 'O' and tic_tac_toe_board_unseen[7] == 'O':

                print('The computer got three in a row!')

                tic_tac_toe_dictionary['Losses'] += 1

                break

            elif tic_tac_toe_board_unseen[2] == 'O' and tic_tac_toe_board_unseen[5] == 'O' and tic_tac_toe_board_unseen[8] == 'O':

                print('The computer got three in a row!')

                tic_tac_toe_dictionary['Losses'] += 1

                break

            elif tic_tac_toe_board_unseen[0] == 'O' and tic_tac_toe_board_unseen[4] == 'O' and tic_tac_toe_board_unseen[8] == 'O':

                print('The computer got three in a row!')

                tic_tac_toe_dictionary['Losses'] += 1

                break

            elif tic_tac_toe_board_unseen[2] == 'O' and tic_tac_toe_board_unseen[4] == 'O' and tic_tac_toe_board_unseen[6] == 'O':

                print('The computer got three in a row!')

                tic_tac_toe_dictionary['Losses'] += 1

                break

    def tic_tac_toe_replay():

        print()

        print('Here\'s the scoreboard:')

        print(tic_tac_toe_dictionary)

        print()

        while True:

            tic_tac_toe_replay_input = input('Do you want to play again? ("Yes"/"No") ')

            if tic_tac_toe_replay_input.upper() == 'YES':

                print('Okay, let\'s go again!')

                tic_tac_toe_board_unseen[0] = ' '
                tic_tac_toe_board_unseen[1] = ' '
                tic_tac_toe_board_unseen[2] = ' '
                tic_tac_toe_board_unseen[3] = ' '
                tic_tac_toe_board_unseen[4] = ' '
                tic_tac_toe_board_unseen[5] = ' '
                tic_tac_toe_board_unseen[6] = ' '
                tic_tac_toe_board_unseen[7] = ' '
                tic_tac_toe_board_unseen[8] = ' '

                print()

                break

            elif tic_tac_toe_replay_input.upper() == 'NO':

                print('Okay, I\'ll see you later!')

                print()

                game_selector_hub()

            else:

                print('Please input either "Yes" or "No"!')

    tic_tac_toe_game_rules()

    while True:

        tic_tac_toe_first_play = tic_tac_toe_coin_toss()

        tic_tac_toe_gameplay_hub(tic_tac_toe_first_play)

        tic_tac_toe_dictionary['Games Played'] += 1

        tic_tac_toe_replay()

########################################################################################################################


def python_quiz_game():

    python_quiz_dictionary = {'Lives': 3, 'Hints': 3, 'Last Section Completed': 0}

    python_quiz_answers_list = ['A', 'B', 'C', 'D']

    def python_quiz_rules():

        print()

        print('Welcome to the Python Quiz!')

        print()

        print('The quiz is broken up into three different sections, each with five questions each. There is an easy, medium and hard section each with questions with their respective difficulty.')

        print('Within the quiz you only have three lives, if a question is missed you lose a life. Once you\'re all out of lives, the quiz is over!!')

        print('You are also given three hints, however once you use all of them you can\'t use them again!')

        print('After each section there will be a bonus question, if you answer it correctly you will be given an extra life!')

        print()

        print('Good Luck!')

        print()

    def python_quiz_easy_sec():

        print()

        print('Section 1 - Difficulty Easy:')

        print()
        print()

        print('1. What is not true of a variable in Python?')
        print('A) It stores a value that you assign to it.')
        print('B) It\'s name can start with a number.')
        print('C) It\'s value can be overwritten/updated by reassigning it later on in a program.')
        print('D) You can add variables together.')

        while True:

            python_quiz_question_1 = input('Enter "A", "B", "C", "D" or "Hint": ')

            if python_quiz_question_1.upper() == 'HINT':

                if python_quiz_dictionary['Hints'] > 0:

                    print('Try to remember the rules for naming variables.')

                    python_quiz_dictionary['Hints'] -= 1

                else:

                    print('You are out of hints!')

            elif python_quiz_question_1.upper() not in python_quiz_answers_list:

                print('Please input a valid answer!')

            elif python_quiz_question_1.upper() != 'B':

                print('That\'s incorrect! The correct answer is "B"!')

                python_quiz_dictionary['Lives'] -= 1

                break

            else:

                print('That\'s right!')

                break

        if python_quiz_dictionary['Lives'] == 0:
            print('You ran out of lives!')

            print()

            python_quiz_replay()

        print()
        print()

        print('2. What is the symbol that goes after calling a function?')
        print('A) "_"')
        print('B) "#"')
        print('C) "()"')
        print('D) "*"')

        while True:

            python_quiz_question_2 = input('Enter "A", "B", "C", "D" or "Hint": ')

            if python_quiz_question_2.upper() == 'HINT':

                if python_quiz_dictionary['Hints'] > 0:

                    print('Look at python\'s many functions such as "print" and "input". What do they have in common?')

                    python_quiz_dictionary['Hints'] -= 1

                else:

                    print('You are out of hints!')

            elif python_quiz_question_2.upper() not in python_quiz_answers_list:

                print('Please input a valid answer!')

            elif python_quiz_question_2.upper() != 'C':

                print('That\'s incorrect! The correct answer is "C"!')

                python_quiz_dictionary['Lives'] -= 1

                break

            else:

                print('That\'s right!')

                break

        if python_quiz_dictionary['Lives'] == 0:

            print('You ran out of lives!')

            print()

            python_quiz_replay()

        print()
        print()

        print('3. What is the output of this code?')
        print()
        print('a = 5')
        print('b = 10')
        print('print(a + b)')
        print()
        print('A) "5"')
        print('B) "10"')
        print('C) "ab"')
        print('D) "15"')

        while True:

            python_quiz_question_3 = input('Enter "A", "B", "C", "D" or "Hint": ')

            if python_quiz_question_3.upper() == 'HINT':

                if python_quiz_dictionary['Hints'] > 0:

                    print('Remember that variables store the values that they are assigned.')

                    python_quiz_dictionary['Hints'] -= 1

                else:

                    print('You are out of hints!')

            elif python_quiz_question_3.upper() not in python_quiz_answers_list:

                print('Please input a valid answer!')

            elif python_quiz_question_3.upper() != 'D':

                print('That\'s incorrect! The correct answer is "D"!')

                python_quiz_dictionary['Lives'] -= 1

                break

            else:

                print('That\'s right!')

                break

        if python_quiz_dictionary['Lives'] == 0:

            print('You ran out of lives!')

            print()

            python_quiz_replay()

        print()
        print()

        print('4. Which of the following creates an empty list?')
        print('A) "list = {}"')
        print('B) "list = []"')
        print('C) "list = ()"')
        print('D) "list = | |"')

        while True:

            python_quiz_question_4 = input('Enter "A", "B", "C", "D" or "Hint": ')

            if python_quiz_question_4.upper() == 'HINT':

                if python_quiz_dictionary['Hints'] > 0:

                    print('Within the answers "A", "B" and "C", there is a tuple, list and dictionary being made.')

                    python_quiz_dictionary['Hints'] -= 1

                else:

                    print('You are out of hints!')

            elif python_quiz_question_4.upper() not in python_quiz_answers_list:

                print('Please input a valid answer!')

            elif python_quiz_question_4.upper() != 'B':

                print('That\'s incorrect! The correct answer is "B"!')

                python_quiz_dictionary['Lives'] -= 1

                break

            else:

                print('That\'s right!')

                break

        if python_quiz_dictionary['Lives'] == 0:

            print('You ran out of lives!')

            print()

            python_quiz_replay()

        print()
        print()

        print('5. True or False, you can change the data type of a variable?')
        print('A) True')
        print('B) False')

        while True:

            python_quiz_question_5 = input('Enter "A", "B", "C", "D" or "Hint": ')

            if python_quiz_question_5.upper() == 'HINT':

                if python_quiz_dictionary['Hints'] > 0:

                    print('Try to remember python\'s functions for the specific data types.')

                    python_quiz_dictionary['Hints'] -= 1

                else:

                    print('You are out of hints!')

            elif python_quiz_question_5.upper() not in python_quiz_answers_list:

                print('Please input a valid answer!')

            elif python_quiz_question_5.upper() != 'A':

                print('That\'s incorrect! The correct answer is "A"!')

                python_quiz_dictionary['Lives'] -= 1

                break

            else:

                print('That\'s right!')

                break

        if python_quiz_dictionary['Lives'] == 0:

            print('You ran out of lives!')

            print()

            python_quiz_replay()

        print()

        print('Here\'s what you ended the first section with:')

        python_quiz_dictionary['Last Section Completed'] += 1

        print(python_quiz_dictionary)

        print()

        print('I\'ll also give you an extra hint for later!')

        python_quiz_dictionary['Hints'] += 1

    def python_quiz_medium_sec():

        print()
        print()

        print('Section 2 - Difficulty Medium:')

        print()
        print()

        print('6. What is the index of "b" in this list?')
        print('list = [a, b, c, d]')
        print('A) 0')
        print('B) 1')
        print('C) 2')
        print('D) 3')

        while True:

            python_quiz_question_6 = input('Enter "A", "B", "C", "D" or "Hint": ')

            if python_quiz_question_6.upper() == 'HINT':

                if python_quiz_dictionary['Hints'] > 0:

                    print('Remember that when counting indexes you start at 0.')

                    python_quiz_dictionary['Hints'] -= 1

                else:

                    print('You are out of hints!')

            elif python_quiz_question_6.upper() not in python_quiz_answers_list:

                print('Please input a valid answer!')

            elif python_quiz_question_6.upper() != 'B':

                print('That\'s incorrect! The correct answer is "B"!')

                python_quiz_dictionary['Lives'] -= 1

                break

            else:

                print('That\'s right!')

                break

        if python_quiz_dictionary['Lives'] == 0:

            print('You ran out of lives!')

            print()

            python_quiz_replay()

        print()
        print()

        print('7. What is the statement used to end a loop?')
        print('A) "continue"')
        print('B) "pass"')
        print('C) "break"')
        print('D) "exit"')

        while True:

            python_quiz_question_7 = input('Enter "A", "B", "C", "D" or "Hint": ')

            if python_quiz_question_7.upper() == 'HINT':

                if python_quiz_dictionary['Hints'] > 0:

                    print('The term "exit" applies to a function used to exit the program so that\'s probably not it.')

                    python_quiz_dictionary['Hints'] -= 1

                else:

                    print('You are out of hints!')

            elif python_quiz_question_7.upper() not in python_quiz_answers_list:

                print('Please input a valid answer!')

            elif python_quiz_question_7.upper() != 'C':

                print('That\'s incorrect! The correct answer is "C"!')

                python_quiz_dictionary['Lives'] -= 1

                break

            else:

                print('That\'s right!')

                break

        if python_quiz_dictionary['Lives'] == 0:

            print('You ran out of lives!')

            print()

            python_quiz_replay()

        print()
        print()

        print('8. What is the main purpose of a for loop?')
        print('A) To loop through a program until a specific condition is met.')
        print('B) To iterate through something such as a string or list.')
        print('C) To loop through a program infinitely.')
        print('D) To serve as a place to store values for variables.')

        while True:

            python_quiz_question_8 = input('Enter "A", "B", "C", "D" or "Hint": ')

            if python_quiz_question_8.upper() == 'HINT':

                if python_quiz_dictionary['Hints'] > 0:

                    print('Think of how a for loop works, try to read a program that uses one and see how it does so.')

                    python_quiz_dictionary['Hints'] -= 1

                else:

                    print('You are out of hints!')

            elif python_quiz_question_8.upper() not in python_quiz_answers_list:

                print('Please input a valid answer!')

            elif python_quiz_question_8.upper() != 'B':

                print('That\'s incorrect! The correct answer is "B"!')

                python_quiz_dictionary['Lives'] -= 1

                break

            else:

                print('That\'s right!')

                break

        if python_quiz_dictionary['Lives'] == 0:

            print('You ran out of lives!')

            print()

            python_quiz_replay()

        print()
        print()

        print('9. What does the following code output?')
        print()
        print('a = 5')
        print('b = 5')
        print('while True:')
        print('print(a + b)')
        print()
        print('A) "10"')
        print('B) "5"')
        print('C) "ab"')
        print('D) "10" an infinite number of times.')

        while True:

            python_quiz_question_9 = input('Enter "A", "B", "C", "D" or "Hint": ')

            if python_quiz_question_9.upper() == 'HINT':

                if python_quiz_dictionary['Hints'] > 0:

                    print('Notice if the loop has any way of exiting.')

                    python_quiz_dictionary['Hints'] -= 1

                else:

                    print('You are out of hints!')

            elif python_quiz_question_9.upper() not in python_quiz_answers_list:

                print('Please input a valid answer!')

            elif python_quiz_question_9.upper() != 'D':

                print('That\'s incorrect! The correct answer is "D"!')

                python_quiz_dictionary['Lives'] -= 1

                break

            else:

                print('That\'s right!')

                break

        if python_quiz_dictionary['Lives'] == 0:

            print('You ran out of lives!')

            print()

            python_quiz_replay()

        print()
        print()

        print('10. Is there a difference between "round(var, 2)" and ":.2f" when used in a program?')
        print('A) Yes, "round(var, 2)" rounds the variable to two decimals while the other does not.')
        print('B) No, they both do the same thing in terms of rounding the variable to two decimals.')
        print('C) Yes, ":.2f" rounds to two decimals while the other does not.')
        print('D) No, they both add two zeros at the end of the variable value.')

        while True:

            python_quiz_question_10 = input('Enter "A", "B", "C", "D" or "Hint": ')

            if python_quiz_question_10.upper() == 'HINT':

                if python_quiz_dictionary['Hints'] > 0:

                    print('The "f" in ":.2f" is for "float", meaning a decimal number.')

                    python_quiz_dictionary['Hints'] -= 1

                else:

                    print('You are out of hints!')

            elif python_quiz_question_10.upper() not in python_quiz_answers_list:

                print('Please input a valid answer!')

            elif python_quiz_question_10.upper() != 'B':

                print('That\'s incorrect! The correct answer is "B"!')

                python_quiz_dictionary['Lives'] -= 1

                break

            else:

                print('That\'s right!')

                break

        if python_quiz_dictionary['Lives'] == 0:

            print('You ran out of lives!')

            print()

            python_quiz_replay()

        print()

        print('Here\'s what you ended the second section with:')

        python_quiz_dictionary['Last Section Completed'] += 1

        print(python_quiz_dictionary)

        print()

        print('I\'ll also give you an extra hint for later!')

        python_quiz_dictionary['Hints'] += 1

    def python_quiz_hard_sec():

        print('Section 3 - Difficulty Hard:')

        print()
        print()

        print('11. True or False, the replace function only replaces characters of a string.')
        print('A) True')
        print('B) False')

        while True:

            python_quiz_question_11 = input('Enter "A", "B", "C", "D" or "Hint": ')

            if python_quiz_question_11.upper() == 'HINT':

                if python_quiz_dictionary['Hints'] > 0:

                    print('It is typically used to replace a specified phrase.')

                    python_quiz_dictionary['Hints'] -= 1

                else:

                    print('You are out of hints!')

            elif python_quiz_question_11.upper() not in python_quiz_answers_list:

                print('Please input a valid answer!')

            elif python_quiz_question_11.upper() != 'A':

                print('That\'s incorrect! The correct answer is "A"!')

                python_quiz_dictionary['Lives'] -= 1

                break

            else:

                print('That\'s right!')

                break

        if python_quiz_dictionary['Lives'] == 0:

            print('You ran out of lives!')

            print()

            python_quiz_replay()

        print()
        print()

        print('12. How would you access a value of a variable that you return from a function with it being the second returned value of the function?')
        print()
        print('Assume it was returned like this: return var1, var2, var3. And that it was stored in a variable called "var".')
        print()
        print('A) You would type the variable name "var".')
        print('B) You would type "var2"')
        print('C) You would type "var[var2]"')
        print('D) You would type "var[1]"')

        while True:

            python_quiz_question_12 = input('Enter "A", "B", "C", "D" or "Hint": ')

            if python_quiz_question_12.upper() == 'HINT':

                if python_quiz_dictionary['Hints'] > 0:

                    print('Think about how indexing works when trying to access a specific value of an index.')

                    python_quiz_dictionary['Hints'] -= 1

                else:

                    print('You are out of hints!')

            elif python_quiz_question_12.upper() not in python_quiz_answers_list:

                print('Please input a valid answer!')

            elif python_quiz_question_12.upper() != 'D':

                print('That\'s incorrect! The correct answer is "D"!')

                python_quiz_dictionary['Lives'] -= 1

                break

            else:

                print('That\'s right!')

                break

        if python_quiz_dictionary['Lives'] == 0:

            print('You ran out of lives!')

            print()

            python_quiz_replay()

        print()
        print()

        print('13. How is it possible to have a loop in a program without using any loop statements?')
        print('A) By using recursive functions to keep calling the same function until a condition is met.')
        print('B) It isn\'t possible to do loops without any loop statements.')
        print('C) You can by using only if statements to keep checking for a condition.')
        print('D) In order to do this you would have to import a specific library.')

        while True:

            python_quiz_question_13 = input('Enter "A", "B", "C", "D" or "Hint": ')

            if python_quiz_question_13.upper() == 'HINT':

                if python_quiz_dictionary['Hints'] > 0:

                    print('Think of how a loop works in terms of doing the same thing over and over.')

                    python_quiz_dictionary['Hints'] -= 1

                else:

                    print('You are out of hints!')

            elif python_quiz_question_13.upper() not in python_quiz_answers_list:

                print('Please input a valid answer!')

            elif python_quiz_question_13.upper() != 'A':

                print('That\'s incorrect! The correct answer is "A"!')

                python_quiz_dictionary['Lives'] -= 1

                break

            else:

                print('That\'s right!')

                break

        if python_quiz_dictionary['Lives'] == 0:

            print('You ran out of lives!')

            print()

            python_quiz_replay()

        print()
        print()

        print('14. What is the difference between a tuple and a list?')
        print('A) You can modify a list, since it is mutable, while you cannot modify a tuple, since it is immutable.')
        print('B) You can modify a tuple, which is mutable, while you cannot modify a list, since it is immutable.')
        print('C) You can only use indexing with a list.')
        print('D) You can only use indexing with a tuple.')

        while True:

            python_quiz_question_14 = input('Enter "A", "B", "C", "D" or "Hint": ')

            if python_quiz_question_14.upper() == 'HINT':

                if python_quiz_dictionary['Hints'] > 0:

                    print('What happens when you try to add something to a tuple compared to a list?')

                    python_quiz_dictionary['Hints'] -= 1

                else:

                    print('You are out of hints!')

            elif python_quiz_question_14.upper() not in python_quiz_answers_list:

                print('Please input a valid answer!')

            elif python_quiz_question_14.upper() != 'A':

                print('That\'s incorrect! The correct answer is "A"!')

                python_quiz_dictionary['Lives'] -= 1

                break

            else:

                print('That\'s right!')

                break

        if python_quiz_dictionary['Lives'] == 0:
            print('You ran out of lives!')

            print()

            python_quiz_replay()

        print()
        print()

        print('15. When importing a library such as random, what syntax needs to be used when attempting to use the specific function "randint" from the library?')
        print('A) No special syntax is needed since the library is already imported.')
        print('B) You would type the name of the library with the variable inside parenthesis. random(var)')
        print('C) You type it with the library name followed by a period then the function with the variable in parenthesis. (random.randint(var))')
        print('D) You would type it with the library name followed by a period then the function being used while storing the value in a variable. (var = random.randint(x, y))')

        while True:

            python_quiz_question_15 = input('Enter "A", "B", "C", "D" or "Hint": ')

            if python_quiz_question_15.upper() == 'HINT':

                if python_quiz_dictionary['Hints'] > 0:

                    print('If you are generating a random number for a dice game for instance, where would you store it and how would you type it out?')

                    python_quiz_dictionary['Hints'] -= 1

                else:

                    print('You are out of hints!')

            elif python_quiz_question_15.upper() not in python_quiz_answers_list:

                print('Please input a valid answer!')

            elif python_quiz_question_15.upper() != 'D':

                print('That\'s incorrect! The correct answer is "D"!')

                python_quiz_dictionary['Lives'] -= 1

                break

            else:

                print('That\'s right!')

                break

        if python_quiz_dictionary['Lives'] == 0:

            print('You ran out of lives!')

            print()

            python_quiz_replay()

        print()

        print('Here\'s what you ended the third section with:')

        python_quiz_dictionary['Last Section Completed'] += 1

        print(python_quiz_dictionary)

        print()

    def python_quiz_bonus_questions():

        print()

        if python_quiz_dictionary['Last Section Completed'] == 1:

            print('Welcome to the first bonus question!')

            print()

            print('What year was the Python language born in?')

            while True:

                python_bonus_1_answer = input('Enter the year: ')

                if (python_bonus_1_answer.isnumeric()) and (python_bonus_1_answer != '1991') and (len(python_bonus_1_answer) == 4):

                    print('That\'s incorrect! Good try though!')

                    break

                elif python_bonus_1_answer == '1991':

                    print('Great Job! You earned an extra life!')

                    python_quiz_dictionary['Lives'] += 1

                    break

                else:

                    print('Type a valid year!')

        elif python_quiz_dictionary['Last Section Completed'] == 2:

            print('Here is the second bonus question!')

            print()

            print('What type of language is python?')

            print('A) Object-Oriented')
            print('B) Logic')
            print('C) Procedural')
            print('D) Scripting')

            while True:

                python_bonus_2_answer = input('Enter either "A", "B", "C" or "D": ')

                if python_bonus_2_answer.upper() not in python_quiz_answers_list:

                    print('Enter a valid answer please!')

                elif python_bonus_2_answer.upper() == 'A':

                    print('Great job! Here\'s an extra life!')

                    python_quiz_dictionary['Lives'] += 1

                    break

                else:

                    print('That\'s incorrect!')

                    break

    def python_quiz_replay():

        print()

        if python_quiz_dictionary['Lives'] == 5:

            print('Great Job! You didn\'t lose any lives as well as got both bonuses right!')

        elif python_quiz_dictionary['Lives'] == 4:

            print('You finished with an extra life! Awesome!')

        elif python_quiz_dictionary['Lives'] == 3:

            print('You started with three lives and ended with three lives, great work!')

        elif python_quiz_dictionary['Lives'] == 2:

            print('You ended with two lives left! I would go and review a little bit.')

        elif python_quiz_dictionary['Lives'] == 1:

            print('You barely made it through the quiz! I would go and study if I were you!')

        elif python_quiz_dictionary['Lives'] == 0:

            print('You lost all of your lives! You need to go do some studying!')

        print()

        while True:

            python_quiz_play_again = input('Would like to try the quiz again? ("Yes/"No") ')

            if python_quiz_play_again.upper() == 'YES':

                print('Cool, let\'s go again!')

                python_quiz_dictionary['Lives'] = 3

                python_quiz_dictionary['Hints'] = 3

                python_quiz_dictionary['Last Section Completed'] = 0

                python_quiz_gameplay_loop()

                break

            elif python_quiz_play_again.upper() == 'NO':

                print('Okay, see you later!')

                print()

                game_selector_hub()

            else:

                print('Please input either a "Yes" or a "No"!')

    def python_quiz_gameplay_loop():

        while True:

            python_quiz_easy_sec()
            python_quiz_bonus_questions()
            python_quiz_medium_sec()
            python_quiz_bonus_questions()
            python_quiz_hard_sec()
            python_quiz_replay()

    python_quiz_rules()

    python_quiz_gameplay_loop()


########################################################################################################################

def hang_man_game():

    hang_man_score = {'Wins': 0, 'Losses': 0, 'Games Played': 0}

    def hang_man_rules():

        print()

        print('Welcome to Hangman!')

        print()

        print('Try and guess the letters of a word to reveal more of the word, or guess the word if you know what it is!')
        print('If you guess the letter correctly, it will appear and nothing happens to the man.')
        print('However, if you guess incorrectly then the man gradually gets drawn to look like he\'s hanging!')
        print('If that happens then you lose and the man dies!')
        print('So try and guess correctly and use your big brain!')
        print('Oh, and you also have 6 lives, broken into 7 stages!')
        print()
        input('Type any key to continue: ')
        print()
        print('Here\'s the different stages of the man being drawn.')
        print()
        print('Stage 1:')
        print('It\'s just the noose.')
        print(''
              '   __________\n'
              '   |        |\n'
              '            |\n'
              '            |\n'
              '            |\n'
              '            |\n')
        print()
        print('Stage 2:')
        print('The head is added.')
        print(''
              '   __________\n'
              '   |        |\n'
              '   O        |\n'
              '            |\n'
              '            |\n'
              '            |\n')
        print()
        print('Stage 3:')
        print('The body is added.')
        print(''
              '   __________\n'
              '   |        |\n'
              '   O        |\n'
              '   |        |\n'
              '            |\n'
              '            |\n')
        print()
        print('Stage 4:')
        print('The left arm is added.')
        print(''
              '   __________\n'
              '   |        |\n'
              '   O        |\n'
              '   |\       |\n'
              '            |\n'
              '            |\n')
        print()
        print('Stage 5:')
        print('The right arm is added.')
        print(''
              '   __________\n'
              '   |        |\n'
              '   O        |\n'
              '  /|\       |\n'
              '            |\n'
              '            |\n')
        print()
        print('Stage 6:')
        print('The left leg is added.')
        print(''
              '   __________\n'
              '   |        |\n'
              '   O        |\n'
              '  /|\       |\n'
              '    \       |\n'
              '            |\n')
        print()
        print('Stage 7:')
        print('The right leg is added. And the man dies :(')
        print(''
              '   __________\n'
              '   |        |\n'
              '   O        |\n'
              '  /|\       |\n'
              '  / \       |\n'
              '            |\n')
        print()
        input('Type any key to continue: ')
        print()
        print()
        print()

        print('Let\'s get started!')

    def hang_man_word_generator():

        hang_man_word_list = ['python', 'computer', 'hacker', 'pancakes', 'apollo', 'programming', 'telephone', 'network', 'website', 'gameplay', 'airpods', 'apple', 'component']

        hang_man_word_choice = random.choice(hang_man_word_list)

        return hang_man_word_choice

    def hang_man_gameplay(hang_man_word):

        hang_man_lives = 6

        hang_man_word_length = len(hang_man_word)

        hang_man_current_word_list = []

        hang_man_gameplay_list = []

        hang_man_guessed_letters_list = []

        for letter in hang_man_word:

            hang_man_current_word_list.append(letter)

        while hang_man_word_length > 0:

            hang_man_gameplay_list.append('_')

            hang_man_word_length -= 1

        while True:

            if hang_man_lives == 6:

                print(''
                      '   __________\n'
                      '   |        |\n'
                      '            |\n'
                      '            |\n'
                      '            |\n'
                      '            |\n')

            elif hang_man_lives == 5:

                print(''
                      '   __________\n'
                      '   |        |\n'
                      '   O        |\n'
                      '            |\n'
                      '            |\n'
                      '            |\n')

            elif hang_man_lives == 4:

                print(''
                      '   __________\n'
                      '   |        |\n'
                      '   O        |\n'
                      '   |        |\n'
                      '            |\n'
                      '            |\n')

            elif hang_man_lives == 3:

                print(''
                      '   __________\n'
                      '   |        |\n'
                      '   O        |\n'
                      '   |\       |\n'
                      '            |\n'
                      '            |\n')

            elif hang_man_lives == 2:

                print(''
                      '   __________\n'
                      '   |        |\n'
                      '   O        |\n'
                      '  /|\       |\n'
                      '            |\n'
                      '            |\n')

            elif hang_man_lives == 1:

                print(''
                      '   __________\n'
                      '   |        |\n'
                      '   O        |\n'
                      '  /|\       |\n'
                      '    \       |\n'
                      '            |\n')

            else:

                print(''
                      '   __________\n'
                      '   |        |\n'
                      '   O        |\n'
                      '  /|\       |\n'
                      '  / \       |\n'
                      '            |\n')

                print('You ran out of lives!')
                print()
                print('The word was ' + hang_man_word + '.')

                hang_man_score['Losses'] += 1

                break

            print(*hang_man_gameplay_list)

            if '_' not in hang_man_gameplay_list:

                print('You guessed the word correctly!')

                hang_man_score['Wins'] += 1

                break

            print()
            print()

            print('Letters guessed:')

            print(*hang_man_guessed_letters_list)

            hang_man_user_word_guess = input('Guess a letter of the word, or guess the entire word: ')

            if hang_man_user_word_guess.lower() == hang_man_word:

                print('Congrats! That\'s the right word!')

                hang_man_score['Wins'] += 1

                break

            elif hang_man_user_word_guess.lower() in hang_man_guessed_letters_list:

                print('You already guessed that!')

                print()

            elif len(hang_man_user_word_guess) == len(hang_man_word):

                print('Good guess, but that\'s not the right word!')

                hang_man_lives -= 1

                print()

            elif not (hang_man_user_word_guess.lower().isalpha()) or (1 < len(hang_man_user_word_guess) < len(hang_man_word)) or (len(hang_man_user_word_guess) > len(hang_man_word)):

                print('This isn\'t in the alphabet!')

                print()

            elif hang_man_user_word_guess.lower() in hang_man_current_word_list:

                print(hang_man_user_word_guess.upper(), 'is a letter of the word!')

                for index in (i for i, letter in enumerate(hang_man_current_word_list) if letter == hang_man_user_word_guess):

                    hang_man_gameplay_list[index] = hang_man_user_word_guess

                hang_man_guessed_letters_list.append(hang_man_user_word_guess)

            else:

                print(hang_man_user_word_guess.upper(), 'isn\'t one of the letters of the word!')

                print()

                hang_man_lives -= 1

                hang_man_guessed_letters_list.append(hang_man_user_word_guess)

    def hang_man_replay():

        print()

        print('Here\'s the score:')

        print(hang_man_score)

        print()

        while True:

            hang_man_user_replay = input('Would you like to play again? ("Yes"/"No") ')

            if hang_man_user_replay.lower() == 'yes':

                print('Okay, let\'s play again!')

                print()

                break

            elif hang_man_user_replay.lower() == 'no':

                print('Okay, thanks for playing!')

                print()

                game_selector_hub()

            else:

                print('Please type either "Yes" or "No"!')

    hang_man_rules()

    while True:

        hang_man_computer_word = hang_man_word_generator()

        hang_man_gameplay(hang_man_computer_word)

        hang_man_score['Games Played'] += 1

        hang_man_replay()


########################################################################################################################

def go_fish_game():

    go_fish_match_dictionary = {'User Books': 0, 'Computer Books': 0}

    go_fish_score_dictionary = {'Wins': 0, 'Losses': 0, 'Ties': 0, 'Games Played': 0}

    def go_fish_rules():

        print()

        print('Welcome to Go Fish!')

        print()

        print('The deck will be shuffled a number of times specified by you and will be distributed between you and the computer.')

        print('Once you have four of the same card, you have a book!')

        print('When it\'s your turn, ask the computer if they have a card you want. If they don\'t then you draw from the deck.')

        print('The same applies when it is the computer\'s turn as well.')

        print('When asking for a card, type in either "Ace", "Jack", "Queen", "King", "2", "3", etc.')

        print()

        print('The end goal is to try to have more books than the computer!')

        print('Good luck!')

        print()

    def go_fish_card_sorter():

        go_fish_entire_card_deck = []

        go_fish_cards_list_one = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

        go_fish_cards_list_two = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

        go_fish_cards_list_three = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

        go_fish_cards_list_four = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

        for card in go_fish_cards_list_one:

            go_fish_entire_card_deck.append(card)

        for card in go_fish_cards_list_two:

            go_fish_entire_card_deck.append(card)

        for card in go_fish_cards_list_three:

            go_fish_entire_card_deck.append(card)

        for card in go_fish_cards_list_four:

            go_fish_entire_card_deck.append(card)

        go_fish_times_shuffled = int(input('How many times do you want the deck to be shuffled? '))

        print('The deck will be shuffled {} time(s)!'.format(go_fish_times_shuffled))

        print()

        while go_fish_times_shuffled > 0:

            random.shuffle(go_fish_entire_card_deck)

            go_fish_times_shuffled -= 1

        go_fish_valid_requests = []

        for card in go_fish_cards_list_one:

            go_fish_valid_requests.append(card)

        for card in go_fish_cards_list_two:

            go_fish_valid_requests.append(card)

        for card in go_fish_cards_list_three:

            go_fish_valid_requests.append(card)

        for card in go_fish_cards_list_four:

            go_fish_valid_requests.append(card)

        return go_fish_entire_card_deck, go_fish_valid_requests

    def go_fish_card_dealer(total_deck):

        go_fish_card_sort_counter = 0

        go_fish_remaining_deck = []

        go_fish_computer_deck = []

        go_fish_user_deck = []

        while go_fish_card_sort_counter < 7:

            go_fish_computer_deck.append(total_deck[0])

            total_deck.remove(total_deck[0])

            go_fish_user_deck.append(total_deck[0])

            total_deck.remove(total_deck[0])

            go_fish_card_sort_counter += 1

        for card in total_deck:

            go_fish_remaining_deck.append(card)

        return go_fish_remaining_deck, go_fish_computer_deck, go_fish_user_deck

    def go_fish_gameplay(card_pile, computer_hand, user_hand, valid_requests):

        go_fish_computer_matches = []

        go_fish_user_matches = []

        # Checking For Computer Matches

        for card in computer_hand:

            go_fish_matches_counter = computer_hand.count(card)

            if go_fish_matches_counter > 3:

                go_fish_computer_matches.append(card)

                go_fish_match_dictionary['Computer Books'] += 0.25

        for card in go_fish_computer_matches:

            if card in computer_hand:

                computer_hand.remove(card)

        for card in go_fish_computer_matches:

            if card in valid_requests:

                valid_requests.remove(card)

        # Checking For User Matches

        for card in user_hand:

            go_fish_matches_counter = user_hand.count(card)

            if go_fish_matches_counter > 3:

                go_fish_user_matches.append(card)

                go_fish_match_dictionary['User Books'] += 0.25

        for card in go_fish_user_matches:

            if card in user_hand:

                user_hand.remove(card)

        for card in go_fish_user_matches:

            if card in valid_requests:

                valid_requests.remove(card)

        # Main Game Loop

        print('Starting Hands:')

        print('User Hand:')

        print(user_hand)

        print()

        print('Books:')

        print('User Books:')

        print(go_fish_user_matches)

        print()

        print('Computer Books:')

        print(go_fish_computer_matches)

        print()

        while True:

            if (len(user_hand) == 0) and (len(computer_hand) == 0) and (len(card_pile) == 0):

                print('All of the cards have been booked!')

                break

            # Getting The User's Card Request

            while True:

                if len(user_hand) == 0:

                    print('You have no cards, so you draw!')

                    print()

                    user_hand.append(card_pile[0])

                    card_pile.remove(card_pile[0])

                    break

                else:

                    go_fish_user_request = input('Which card(s) do you want to ask the computer for? ')

                    print()

                    if (go_fish_user_request.capitalize() in valid_requests) and (go_fish_user_request.capitalize() in computer_hand):

                        print('The computer had that card! It was added to your hand!')

                        print()

                        for card in computer_hand:

                            if card == go_fish_user_request.capitalize():

                                user_hand.append(card)

                        computer_hand = [i for i in computer_hand if i != go_fish_user_request.capitalize()]

                        if len(user_hand) == 0:

                            print('You are out of cards, so you draw a card!')

                            user_hand.append(card_pile[0])

                            card_pile.remove(card_pile[0])

                        break

                    elif (go_fish_user_request.capitalize() in valid_requests) and (go_fish_user_request.capitalize() not in computer_hand):

                        print('Go Fish!')

                        print('You drew a card!')

                        print()

                        user_hand.append(card_pile[0])

                        card_pile.remove(card_pile[0])

                        break

                    elif (go_fish_user_request.capitalize() in go_fish_user_matches) or (go_fish_user_request.capitalize() in go_fish_computer_matches):

                        print('This card already has it\'s book made!')

                    else:

                        print('Please enter a valid card!')

                        print()

            # Checking For User Matches

            for card in user_hand:

                go_fish_matches_counter = user_hand.count(card)

                if go_fish_matches_counter > 3:

                    go_fish_user_matches.append(card)

                    go_fish_match_dictionary['User Books'] += 0.25

            for card in go_fish_user_matches:

                if card in user_hand:

                    user_hand.remove(card)

            for card in go_fish_user_matches:

                if card in valid_requests:

                    valid_requests.remove(card)

            # Computer Turn

            print('Updated Hands:')

            print('User Hand:')

            print(user_hand)

            print()

            print('Books:')

            print('User Books:')

            print(go_fish_user_matches)

            print()

            print('Computer Books:')

            print(go_fish_computer_matches)

            print()

            if (len(user_hand) == 0) and (len(computer_hand) == 0) and (len(card_pile) == 0):

                print('All of the cards have been booked!')

                break

            if len(computer_hand) == 0:

                print('The computer has no cards in it\'s hand, so it draws a card!')

                print()

                computer_hand.append(card_pile[0])

                card_pile.remove(card_pile[0])

            else:

                go_fish_computer_turn = random.choice(computer_hand)

                print('The computer asked for a ' + go_fish_computer_turn + '!')

                print()

                if go_fish_computer_turn in user_hand:

                    print('The computer took your card(s)!')

                    print()

                    for card in user_hand:

                        if card == go_fish_computer_turn:

                            computer_hand.append(card)

                    user_hand = [i for i in user_hand if i != go_fish_computer_turn]

                    if len(computer_hand) == 0:

                        print('The computer is out of cards, so it draws a card!')

                        computer_hand.append(card_pile[0])

                        card_pile.remove(card_pile[0])

                elif go_fish_computer_turn not in user_hand:

                    print('The computer had to Go Fish!')

                    print()

                    computer_hand.append(card_pile[0])

                    card_pile.remove(card_pile[0])

            # Checking For Computer Matches

            for card in computer_hand:

                go_fish_matches_counter = computer_hand.count(card)

                if go_fish_matches_counter > 3:

                    go_fish_computer_matches.append(card)

                    go_fish_match_dictionary['Computer Books'] += 0.25

            for card in go_fish_computer_matches:

                if card in computer_hand:

                    computer_hand.remove(card)

            for card in go_fish_computer_matches:

                if card in valid_requests:

                    valid_requests.remove(card)

            print('Updated Hands:')

            print('User Hand:')

            print(user_hand)

            print()

            print('Books:')

            print('User Books:')

            print(go_fish_user_matches)

            print()

            print('Computer Books:')

            print(go_fish_computer_matches)

            print()

        print()

        print('Here\'s the end of game statistics:')

        print()

        print('Books:')

        print('User Books:')

        print(go_fish_user_matches)

        print()

        print('Computer Books:')

        print(go_fish_computer_matches)

        print()

        print(go_fish_match_dictionary)

        print()

        if len(go_fish_user_matches) > len(go_fish_computer_matches):

            print('You had more books! So you won the game!')

            print()

            go_fish_score_dictionary['Wins'] += 1

        elif len(go_fish_user_matches) < len(go_fish_computer_matches):

            print('You had less books than the computer, so you lost!')

            print()

            go_fish_score_dictionary['Losses'] += 1

        else:

            print('You had the same number of books as the computer, so it\'s a tie!')

            print()

            go_fish_score_dictionary['Ties'] += 1

    def go_fish_replay():

        print('Here\'s the score:')

        print(go_fish_score_dictionary)

        while True:

            print()

            go_fish_replay_request = input('Would you like to play again/ ("Yes"/"No"): ')

            if go_fish_replay_request.upper() == 'YES':

                print('Okay! Let\'s go!')

                break

            elif go_fish_replay_request.upper() == 'NO':

                print('Okay, bye!')

                game_selector_hub()

            else:

                print('Please type either "Yes" or "No"!')

    go_fish_rules()

    while True:

        go_fish_total_deck = go_fish_card_sorter()

        go_fish_gameplay_decks = go_fish_card_dealer(go_fish_total_deck[0])

        go_fish_gameplay(go_fish_gameplay_decks[0], go_fish_gameplay_decks[1], go_fish_gameplay_decks[2],go_fish_total_deck[1])

        go_fish_score_dictionary['Games Played'] += 1

        go_fish_replay()

########################################################################################################################


def uno_game():

    uno_score = {'User Wins': 0, 'Computer Wins': 0}

    def uno_game_greeting():

        print()

        print('Welcome to Uno! Try to be the first player to get rid of all of the cards in your hand!')

        print()

        print('The standard Uno rules apply, meaning that you can only play the same color card or the same type of card such as the same number or symbol.')

        print('However, wild cards can be played whenever, regardless of which card is on the top of the discard pile.')

        print()

        print('The deck will be shuffled before the game begins and will also be reshuffled in the event that the draw pile runs out of cards.')

        print()

        print('IMPORTANT NOTE: When playing a card be sure to type it out EXACTLY as it is displayed in your hand. I haven\'t implemented a way to check for different cases in the user input yet.')

        print()

        print('Good Luck and Have Fun!')

        print()

        input('Press "Enter" to continue: ')

        print()

    def uno_deck_maker():

        uno_zero_cards = ['Red_0', 'Blue_0', 'Green_0', 'Yellow_0']

        uno_red_number_cards = ['Red_1', 'Red_2', 'Red_3', 'Red_4', 'Red_5', 'Red_6', 'Red_7', 'Red_8', 'Red_9']

        uno_red_number_cards_2 = uno_red_number_cards

        uno_red_action_cards = ['Red_Skip', 'Red_Reverse', 'Red_Draw_2+']

        uno_red_action_cards_2 = uno_red_action_cards

        red_cards = uno_red_number_cards + uno_red_number_cards_2 + uno_red_action_cards + uno_red_action_cards_2

        blue_cards = []

        for card in red_cards:

            x = card.replace('Red', 'Blue')

            blue_cards.append(x)

        green_cards = []

        for card in red_cards:

            x = card.replace('Red', 'Green')

            green_cards.append(x)

        yellow_cards = []

        for card in red_cards:

            x = card.replace('Red', 'Yellow')

            yellow_cards.append(x)

        wild_cards = ['Wild_Card', 'Wild_Card', 'Wild_Card', 'Wild_Card', 'Wild_Draw_4', 'Wild_Draw_4', 'Wild_Draw_4','Wild_Draw_4']

        uno_total_deck = uno_zero_cards + red_cards + blue_cards + green_cards + yellow_cards + wild_cards

        return uno_total_deck

    def uno_deck_shuffler(deck):

        print()

        break_out_flag = False

        while True:

            if break_out_flag:

                break

            user_shuffle_input = input('Type "0" to pick how many times the deck is shuffled or type "1" to have it randomly shuffled. ')

            print()

            if user_shuffle_input.isdigit():

                if user_shuffle_input == '0':

                    while True:

                        user_shuffle_number = input('Enter how many times you want the deck shuffled: ')

                        print()

                        if user_shuffle_number.isdigit():

                            times_shuffled = int(user_shuffle_number)

                            print('The deck will be shuffled {} time(s)!'.format(times_shuffled))

                            print()

                            break_out_flag = True

                            break

                        else:

                            print('Please enter an integer!')

                            print()

                elif user_shuffle_input == '1':

                    times_shuffled = random.randint(1, 10)

                    print('The deck will be shuffled {} time(s)!'.format(times_shuffled))

                    print()

                    break

                else:

                    print('You entered a number, but not a "0" or a "1".')

                    print()

            else:

                print('Please type either a "0" or a "1"! You entered a word!')

                print()

        while times_shuffled > 0:

            random.shuffle(deck)

            times_shuffled -= 1

        print('The deck was shuffled!')

        print()

        print()

        input('Press "Enter" to continue: ')

        print()

        print()

        return deck

    def card_dealer(game_deck):

        game_deck_actual = game_deck

        uno_user_hand = []

        uno_computer_hand = []

        cards_dealt = 7

        while cards_dealt > 0:

            uno_user_hand.append(game_deck_actual[0])

            game_deck.remove(game_deck_actual[0])

            uno_computer_hand.append(game_deck_actual[0])

            game_deck.remove(game_deck_actual[0])

            cards_dealt -= 1

        return uno_user_hand, uno_computer_hand, game_deck_actual

    def gameplay_function(user_hand, computer_hand, draw_pile):

        discard_pile = []

        discard_pile.append(draw_pile[0])

        draw_pile.remove(draw_pile[0])

        print('Let\'s toss a coin to see who goes first.')

        print()

        coin_toss_list = ['HEADS', 'TALES']

        coin_toss_value = random.choice(coin_toss_list)

        while True:

            user_coin_value = input('Type either "heads" or "tales": ')

            print()

            if user_coin_value.upper() not in coin_toss_list:

                print('You didn\'t type "heads" or "tales"!')

                print()

            else:

                if user_coin_value.upper() == coin_toss_value:

                    print('You won the coin toss!')

                    print()

                    user_turn = 1

                    break

                else:

                    print('The computer won the coin toss!')

                    print()

                    user_turn = 2

                    break

        input('Press "Enter" to continue: ')

        print()

        while True:

            user_invalid_card = False

            computer_invalid_card = False

            user_card_chosen_flag = False

            if (len(user_hand) == 0) or (len(computer_hand) == 0):

                if len(user_hand) == 0:

                    print('You\'re out of cards!')

                    uno_score['User Wins'] += 1

                    break

                else:

                    print('The computer is out of cards!')

                    uno_score['Computer Wins'] += 1

                    break

            if len(draw_pile) == 0:

                print('The draw pile is out of cards, we\'ll reshuffle the cards in the discard pile and continue play.')

                print()

                for card in discard_pile:

                    draw_pile.append(card)

                    discard_pile.remove(card)

                shuffle_number = random.randint(1, 10)

                while shuffle_number > 0:

                    random.shuffle(draw_pile)

                    shuffle_number -= 1

                discard_pile.append(draw_pile[0])

                draw_pile.remove(draw_pile[0])

            if user_turn % 2 != 0:

                print('---------------------------------------------------------------------------------------------------')

                print()

                print('Computer\'s Hand:')

                computer_hand_hidden = []

                computer_hand_length = len(computer_hand)

                while computer_hand_length > 0:

                    computer_hand_hidden.append('X')

                    computer_hand_length -= 1

                print(computer_hand_hidden)

                print()

                print('Discard Pile Top Card:')

                print(discard_pile[0])

                print()

                print('Number of Cards In Draw Pile:')

                print(len(draw_pile))

                print()

                print('Your Hand:')

                print(user_hand)

                print()

                print('It\'s your turn!')

                print()

                if discard_pile[0][0] == 'W':

                    while True:

                        user_choice = input('Enter any card since there\'s a wild card in the discard pile! ')

                        print()

                        if user_choice not in user_hand:

                            print('That is not a valid card to play!')

                            print()

                        else:

                            user_card_chosen = user_choice

                            discard_pile.insert(0, user_card_chosen)

                            break

                else:

                    user_choices = []

                    for card in user_hand:

                        if (card[0] == discard_pile[0][0]) or (card[0] == 'W') or (card[-1] == discard_pile[0][-1]):

                            user_choices.append(card)

                    if len(user_choices) == 0:

                        print('You have no valid cards to play!')

                        print('That means you draw from the deck!')

                        print()

                        user_hand.append(draw_pile[0])

                        draw_pile.remove(draw_pile[0])

                        user_turn += 1

                        user_invalid_card = True

                        input('Press "Enter" to continue: ')

                        print()

                    else:

                        while True:

                            user_choice = input('Enter the card that you want to play: ')

                            print()

                            if user_choice not in user_hand:

                                print('That is not a valid card to play!')

                                print()

                            elif (user_choice[0] == discard_pile[0][0]) or (user_choice[0] == 'W') or (user_choice[-1] == discard_pile[0][-1]):

                                user_card_chosen = user_choice

                                user_choices.clear()

                                user_card_chosen_flag = True

                                break

                            else:

                                print('Type in a card with the matching color, the matching value or a wild card!')

                                print()

                        discard_pile.insert(0, user_card_chosen)

                if user_card_chosen_flag:

                    for card in user_hand:

                        if card == user_card_chosen:

                            user_hand.remove(card)

                uno_action_cards = ['Wild_Card', 'Wild_Draw_4', 'Red_Skip', 'Red_Reverse', 'Red_Draw_2+', 'Blue_Skip',
                                    'Blue_Reverse', 'Blue_Draw_2+', 'Green_Skip', 'Green_Reverse', 'Green_Draw_2+',
                                    'Yellow_Skip', 'Yellow_Reverse', 'Yellow_Draw_2+']

                if user_invalid_card:

                    print('Your turn is over!')

                    print()

                    input('Press "Enter" to continue: ')

                    print()

                elif user_card_chosen in uno_action_cards:

                    if '4' in user_card_chosen:

                        print('You made the computer draw four cards!')

                        print()

                        draw_4_counter = 4

                        while draw_4_counter > 0:

                            computer_hand.append(draw_pile[0])

                            draw_pile.pop(0)

                            draw_4_counter -= 1

                        color_picker = ['RED', 'BLUE', 'GREEN', 'YELLOW']

                        while True:

                            print()

                            wild_card_color = input('Enter a color to make the wild card: ')

                            print()

                            if wild_card_color.upper() not in color_picker:

                                print('Enter a valid color!')

                            else:

                                break

                        if wild_card_color.upper() == 'RED':

                            print('You changed the color to red!')

                            print()

                            discard_pile.insert(0, wild_card_color.upper())

                            input('Press "Enter" to continue: ')

                            print()

                        elif wild_card_color.upper() == 'BLUE':

                            print('You changed the color to blue!')

                            print()

                            discard_pile.insert(0, wild_card_color.upper())

                            input('Press "Enter" to continue: ')

                            print()

                        elif wild_card_color.upper() == 'GREEN':

                            print('You changed the color to green!')

                            print()

                            discard_pile.insert(0, wild_card_color.upper())

                            input('Press "Enter" to continue: ')

                            print()

                        else:

                            print('You changed the color to yellow!')

                            print()

                            discard_pile.insert(0, wild_card_color.upper())

                            input('Press "Enter" to continue: ')

                            print()

                    elif '2' in user_card_chosen:

                        print('You made the computer draw two cards!')

                        print()

                        draw_2_counter = 2

                        while draw_2_counter > 0:

                            computer_hand.append(draw_pile[0])

                            draw_pile.pop(0)

                            draw_2_counter -= 1

                        input('Press "Enter" to continue: ')

                        print()

                    elif 'Reverse' in user_card_chosen:

                        print('The order was reversed, so it\'s your turn again!')

                        print()

                        input('Press "Enter" to continue: ')

                        print()

                    elif 'Skip' in user_card_chosen:

                        print('You skipped the computer\'s turn!')

                        print()

                        input('Press "Enter" to continue: ')

                        print()

                    else:

                        print('You played a wild card!')

                        print()

                        user_turn += 1

                        color_picker = ['RED', 'BLUE', 'GREEN', 'YELLOW']

                        while True:

                            print()

                            wild_card_color = input('Enter a color to make the wild card: ')

                            print()

                            if wild_card_color.upper() not in color_picker:

                                print('Enter a valid color!')

                            else:

                                break

                        if wild_card_color.upper() == 'RED':

                            print('You changed the color to red!')

                            print()

                            discard_pile.insert(0, wild_card_color.upper())

                            input('Press "Enter" to continue: ')

                            print()

                        elif wild_card_color.upper() == 'BLUE':

                            print('You changed the color to blue!')

                            print()

                            discard_pile.insert(0, wild_card_color.upper())

                            input('Press "Enter" to continue: ')

                            print()

                        elif wild_card_color.upper() == 'GREEN':

                            print('You changed the color to green!')

                            print()

                            discard_pile.insert(0, wild_card_color.upper())

                            input('Press "Enter" to continue: ')

                            print()

                        else:

                            print('You changed the color to yellow!')

                            print()

                            discard_pile.insert(0, wild_card_color.upper())

                            input('Press "Enter" to continue: ')

                            print()

                else:

                    print('You played your card!')

                    print()

                    user_turn += 1

                    input('Press "Enter" to continue: ')

                    print()

                if len(user_hand) == 1:
                    print('You have one card left, UNO!')

                    print()

                    input('Press "Enter" to continue: ')

                    print()

            if (len(user_hand) == 0) or (len(computer_hand) == 0):

                if len(user_hand) == 0:

                    print('You\'re out of cards!')

                    uno_score['User Wins'] += 1

                    break

                else:

                    print('The computer is out of cards!')

                    uno_score['Computer Wins'] += 1

                    break

            if len(draw_pile) == 0:

                print(
                    'The draw pile is out of cards, we\'ll reshuffle the cards in the discard pile and continue play.')

                print()

                for card in discard_pile:

                    draw_pile.append(card)

                    discard_pile.remove(card)

                shuffle_number = random.randint(1, 10)

                while shuffle_number > 0:

                    random.shuffle(draw_pile)

                    shuffle_number -= 1

                discard_pile.append(draw_pile[0])

                draw_pile.remove(draw_pile[0])

                input('Press "Enter" to continue: ')

                print()

            if user_turn % 2 == 0:

                print('---------------------------------------------------------------------------------------------------')

                print()

                print('Computer\'s Hand:')

                computer_hand_hidden = []

                computer_hand_length = len(computer_hand)

                while computer_hand_length > 0:

                    computer_hand_hidden.append('X')

                    computer_hand_length -= 1

                print(computer_hand_hidden)

                print()

                print('Discard Pile Top Card:')

                print(discard_pile[0])

                print()

                print('Number of Cards In Draw Pile:')

                print(len(draw_pile))

                print()

                print('Your Hand:')

                print(user_hand)

                print()

                print('It\'s the computer\'s turn!')

                print()

                computer_card_choices = []

                if discard_pile[0][0] == 'W':

                    for card in computer_hand:

                        computer_card_choices.append(card)

                else:

                    for card in computer_hand:

                        if (card[0] == discard_pile[0][0]) or (card[0] == 'W') or (card[-1] == discard_pile[0][-1]):

                            computer_card_choices.append(card)

                if len(computer_card_choices) == 0:

                    print('The computer doesn\'t have a card to play so it draws from the deck!')

                    print()

                    computer_hand.append(draw_pile[0])

                    draw_pile.remove(draw_pile[0])

                    computer_hand_hidden.append('X')

                    user_turn += 1

                    computer_invalid_card = True

                    input('Press "Enter" to continue: ')

                    print()

                else:

                    computer_card_chosen = random.choice(computer_card_choices)

                    computer_card_choices.clear()

                    discard_pile.insert(0, computer_card_chosen)

                    computer_hand_hidden.pop(0)

                    for card in computer_hand:

                        if card == computer_card_chosen:

                            computer_hand.remove(card)

                    uno_action_cards = ['Wild_Card', 'Wild_Draw_4', 'Red_Skip', 'Red_Reverse', 'Red_Draw_2+',
                                        'Blue_Skip', 'Blue_Reverse', 'Blue_Draw_2+', 'Green_Skip', 'Green_Reverse',
                                        'Green_Draw_2+', 'Yellow_Skip', 'Yellow_Reverse', 'Yellow_Draw_2+']

                    if computer_invalid_card:

                        print('The computer\'s turn is over!')

                        print()

                        input('Press "Enter" to continue: ')

                        print()

                    elif computer_card_chosen in uno_action_cards:

                        if '4' in computer_card_chosen:

                            print('The computer made you draw four cards!')

                            print()

                            draw_4_counter = 4

                            while draw_4_counter > 0:

                                user_hand.append(draw_pile[0])

                                draw_pile.pop(0)

                                draw_4_counter -= 1

                            color_picker = ['RED', 'BLUE', 'GREEN', 'YELLOW']

                            wild_card_color = random.choice(color_picker)

                            if wild_card_color == 'RED':

                                print('The computer changed the color to red!')

                                print()

                                discard_pile.insert(0, wild_card_color)

                                input('Press "Enter" to continue: ')

                                print()

                            elif wild_card_color == 'BLUE':

                                print('The computer changed the color to blue!')

                                print()

                                discard_pile.insert(0, wild_card_color)

                                input('Press "Enter" to continue: ')

                                print()

                            elif wild_card_color == 'GREEN':

                                print('The computer changed the color to green!')

                                print()

                                discard_pile.insert(0, wild_card_color)

                                input('Press "Enter" to continue: ')

                                print()

                            else:

                                print('The computer changed the color to yellow!')

                                print()

                                discard_pile.insert(0, wild_card_color)

                                input('Press "Enter" to continue: ')

                                print()

                        elif '2' in computer_card_chosen:

                            print('The computer made you draw two cards!')

                            print()

                            draw_2_counter = 2

                            while draw_2_counter > 0:

                                user_hand.append(draw_pile[0])

                                draw_pile.pop(0)

                                draw_2_counter -= 1

                            input('Press "Enter" to continue: ')

                            print()

                        elif 'Reverse' in computer_card_chosen:

                            print('The order was reversed, so it\'s the computer\'s turn again!')

                            print()

                            input('Press "Enter" to continue: ')

                            print()

                        elif 'Skip' in computer_card_chosen:

                            print('The computer skipped your turn!')

                            print()

                            input('Press "Enter" to continue: ')

                            print()

                        else:

                            print('The computer played a wild card!')

                            print()

                            user_turn += 1

                            color_picker = ['RED', 'BLUE', 'GREEN', 'YELLOW']

                            wild_card_color = random.choice(color_picker)

                            if wild_card_color == 'RED':

                                print('The computer changed the color to red!')

                                print()

                                discard_pile.insert(0, wild_card_color)

                                input('Press "Enter" to continue: ')

                                print()

                            elif wild_card_color == 'BLUE':

                                print('The computer changed the color to blue!')

                                print()

                                discard_pile.insert(0, wild_card_color)

                                input('Press "Enter" to continue: ')

                                print()

                            elif wild_card_color == 'GREEN':

                                print('The computer changed the color to green!')

                                print()

                                discard_pile.insert(0, wild_card_color)

                                input('Press "Enter" to continue: ')

                                print()

                            else:

                                print('The computer changed the color to yellow!')

                                print()

                                discard_pile.insert(0, wild_card_color)

                                input('Press "Enter" to continue: ')

                                print()

                    else:

                        print('The computer played its card!')

                        print()

                        user_turn += 1

                        input('Press "Enter" to continue: ')

                        print()

                if len(computer_hand) == 1:

                    print('The computer has one card left, UNO!')

                    print()

                    input('Press "Enter" to continue: ')

                    print()

    def uno_replay():

        print()

        print('Here\'s the score:')

        print(uno_score)

        print()

        while True:

            print()

            uno_user_replay = input('Would you like to play again? ("Yes"/"No") ')

            if uno_user_replay.lower() == 'yes':

                print('Okay, let\'s play again!')

                print()

                break

            elif uno_user_replay.lower() == 'no':

                print('Okay, thanks for playing!')

                game_selector_hub()

            else:

                print('Please type either "Yes" or "No"!')

    uno_game_greeting()

    while True:

        uno_completed_deck = uno_deck_maker()

        shuffled_deck = uno_deck_shuffler(uno_completed_deck)

        gameplay_decks = card_dealer(shuffled_deck)

        gameplay_function(gameplay_decks[0], gameplay_decks[1], gameplay_decks[2])

        uno_replay()

#######################################################################################################################


def war_game():

    card_value_dictionary = {'Joker': 14, 'Ace': 13, 'King': 12, 'Queen': 11, 'Jack': 10, '10': 9, '9': 8, '8': 7,
                             '7': 6, '6': 5, '5': 4, '4': 3, '3': 2, '2': 1}

    war_score = {'User Wins': 0, 'Computer Wins': 0, 'Games Played': 0}

    def war_rules():

        print()

        print('Welcome to War! Be the first player to collect all 54 cards!')

        print()

        print('Each player will compare their first card in their hand with each other. The player with the highest '
              'value card wins and that player gets both cards put into their card pile.')

        print('If both cards are the same value then their is a WAR!')

        print('Once the WAR starts the two compared cards, along with the next three cards from each player\'s hand '
              'will be added to the WAR pile.')

        print('The two players will then compare their next card and the player with the highest value card wins the '
              'WAR and gets all of the cards in the WAR pile.')

        print('In the event that a player does not have enough cards for a WAR, the other player wins automatically.')

        print('If both players do not have enough cards for a WAR, then the player with the most cards wins.')

        print('Lastly, if both players have the same amount of cards and cannot have a WAR, the last card in the '
              'player hand is compared to the other player, with the highest value being the winner.')

        print('In the event of a tie in this case, the cards will all be shuffled and dealt out again.')

        print()

        print('Good luck!')

        print()

        input('Press "enter" to continue: ')

        print()

    def create_deck():

        created_deck = []

        counter = 4

        card_suite = ['Ace', 'King', 'Queen', 'Jack', '10', '9', '8', '7', '6', '5', '4', '3', '2']

        jokers = ['Joker', 'Joker']

        while counter > 0:

            for card in card_suite:

                created_deck.append(card)

                if len(created_deck) % 13 == 0:

                    counter -= 1

        for card in jokers:

            created_deck.append(card)

        return created_deck

    def deck_shuffler(deck):

        shuffle_number = 0

        user_pick_shuffle = False

        random_shuffle = False

        while True:

            shuffle_choice = input('Type "0" to pick how many times the deck is shuffled or type "1" to have it '
                                   'shuffled randomly: ')

            if shuffle_choice == '0':

                user_pick_shuffle = True

                break

            elif shuffle_choice == '1':

                random_shuffle = True

                break

            else:

                print('Please type either a "0" or a "1".')

                print()

        if user_pick_shuffle:

            while True:

                times_shuffled = input('Enter how many times to shuffle the deck: ')

                if times_shuffled.isdigit():

                    if times_shuffled == '0':

                        print('Type in a number greater than 1.')

                        print()

                    else:

                        shuffle_number = int(times_shuffled)

                        print('The deck will be shuffled {} time(s).'.format(shuffle_number))

                        print()

                        break

                else:

                    print('Please enter a valid integer.')

                    print()

        elif random_shuffle:

            shuffle_number = random.randint(1, 10)

            print('The deck will be shuffled {} time(s).'.format(shuffle_number))

            print()

        while shuffle_number > 0:

            random.shuffle(deck)

            shuffle_number -= 1

        input('Press "enter" to continue: ')

        print()

        return deck

    def deck_dealer(deck):

        user_hand = deck[0::2]

        computer_hand = deck[1::2]

        return user_hand, computer_hand

    def gameplay_function(user_hand, computer_hand):

        turn = 1

        user_card_pile = []

        computer_card_pile = []

        war_card_list = []

        war_card_shuffle = []

        while True:

            print('Turn: {}'.format(turn))

            print('-------------------------------------------------------------------------------------------------------')

            print()

            print('Computer Info:')

            print('Computer\'s Current Card: {}'.format(computer_hand[0]))

            print('Number of Cards in Computer\'s Pile: {}'.format(len(computer_card_pile)))

            print('Number of Cards in The Computer\'s Hand: {}'.format(len(computer_hand)))

            print()

            print('User Info:')

            print('Your Current Card: {}'.format(user_hand[0]))

            print('Number of Cards in Your Pile: {}'.format(len(user_card_pile)))

            print('Number of Cards in Your Hand: {}'.format(len(user_hand)))

            print()

            print('-------------------------------------------------------------------------------------------------------')

            # input('Press enter to continue: ')

            print()

            if card_value_dictionary[computer_hand[0]] < card_value_dictionary[user_hand[0]]:

                print('Your card has a higher value, so you get both cards.')

                print()

                user_card_pile.append(user_hand[0])

                user_hand.remove(user_hand[0])

                user_card_pile.append(computer_hand[0])

                computer_hand.remove(computer_hand[0])

                turn += 1

                # input('Press enter to continue: ')

                print()

            elif card_value_dictionary[computer_hand[0]] > card_value_dictionary[user_hand[0]]:

                print('The computer\'s card has a higher value, so it gets both cards.')

                print()

                computer_card_pile.append(user_hand[0])

                user_hand.remove(user_hand[0])

                computer_card_pile.append(computer_hand[0])

                computer_hand.remove(computer_hand[0])

                turn += 1

                # input('Press enter to continue: ')

                print()

            else:

                print('You and the computer have the same value card, so it\'s WAR!')

                print()

                print('The cards that were compared, along with three other cards from each players hand, will be put '
                      'into the war pile for the winner to collect.')

                print()

                # input('Press enter to continue: ')

                print()

                while True:

                    war_counter = 3

                    war_card_list.append(user_hand[0])

                    user_hand.remove(user_hand[0])

                    war_card_list.append(computer_hand[0])

                    computer_hand.remove(computer_hand[0])

                    if len(user_hand) == 0:

                        print('You ran out of cards!')

                        print('The cards in your card pile will be put into your hand and shuffled a random amount of '
                              'times.')

                        print()

                        for card in user_card_pile:

                            user_hand.append(card)

                        user_card_pile.clear()

                        shuffle_number = random.randint(1, 10)

                        print('Your new hand was shuffled {} time(s).'.format(shuffle_number))

                        while shuffle_number > 0:

                            random.shuffle(user_hand)

                            shuffle_number -= 1

                        print()

                        # input('Press enter to continue: ')

                        print()

                    if len(computer_hand) == 0:

                        print('The computer ran out of cards!')

                        print('The cards in the computer\'s card pile will be put into its hand and shuffled a random '
                              'amount of times.')

                        print()

                        for card in computer_card_pile:

                            computer_hand.append(card)

                        computer_card_pile.clear()

                        shuffle_number = random.randint(1, 10)

                        print('The computer\'s new hand was shuffled {} time(s).'.format(shuffle_number))

                        while shuffle_number > 0:

                            random.shuffle(computer_hand)

                            shuffle_number -= 1

                        print()

                        # input('Press enter to continue: ')

                        print()

                    if len(user_hand) < 4 and len(computer_hand) < 4:

                        print('You and the computer do not have enough cards for a WAR!')

                        print('So, I will determine who wins based on the number of cards in the hands.')

                        print()

                        if len(user_hand) < len(computer_hand):

                            print('The computer has more cards, so it wins automatically.')

                            print()

                            for card in user_hand:

                                computer_card_pile.append(card)

                            user_hand.clear()

                            for card in war_card_list:

                                computer_card_pile.append(card)

                            war_card_list.clear()

                            for card in computer_hand:

                                computer_card_pile.append(card)

                            computer_hand.clear()

                            break

                        elif len(user_hand) > len(computer_hand):

                            print('You have more cards than the computer, so you win automatically.')

                            print()

                            for card in computer_hand:

                                user_card_pile.append(card)

                            computer_hand.clear()

                            for card in war_card_list:

                                user_card_pile.append(card)

                            war_card_list.clear()

                            for card in user_hand:

                                user_card_pile.append(card)

                            user_hand.clear()

                            break

                        else:

                            print(
                                'You and the computer have the same amount of cards, so we will compare the last cards.')

                            print()

                            if card_value_dictionary[user_hand[-1]] > card_value_dictionary[computer_hand[-1]]:

                                print('Your last card has a higher value than the computer\'s, so you win the WAR!')

                                print()

                                for card in computer_hand:

                                    user_card_pile.append(card)

                                computer_hand.clear()

                                for card in war_card_list:

                                    user_card_pile.append(card)

                                war_card_list.clear()

                                for card in user_hand:

                                    user_card_pile.append(card)

                                user_hand.clear()

                                break

                            elif card_value_dictionary[user_hand[-1]] < card_value_dictionary[computer_hand[-1]]:

                                print('The computer\'s last card has a higher value, so it wins the WAR!')

                                print()

                                for card in user_hand:

                                    computer_card_pile.append(card)

                                user_hand.clear()

                                for card in war_card_list:

                                    computer_card_pile.append(card)

                                war_card_list.clear()

                                for card in computer_hand:

                                    computer_card_pile.append(card)

                                computer_hand.clear()

                                break

                            else:

                                print('Since the last cards also have the same value the cards will be shuffled and '
                                      'redistributed.')

                                print()

                                for card in user_hand:

                                    war_card_shuffle.append(card)

                                user_hand.clear()

                                for card in computer_hand:

                                    war_card_shuffle.append(card)

                                computer_hand.clear()

                                for card in war_card_list:

                                    war_card_shuffle.append(card)

                                war_card_list.clear()

                                war_shuffle = random.randint(1, 10)

                                print('The cards will be shuffled {} time(s).'.format(war_shuffle))

                                print()

                                while war_shuffle > 0:

                                    random.shuffle(war_card_shuffle)

                                    war_shuffle -= 1

                                user_hand = war_card_shuffle[0::2]

                                computer_hand = war_card_shuffle[1::2]

                                war_card_shuffle.clear()

                                break

                    elif len(user_hand) < 4:

                        print('You do not have enough cards for the war, so the computer wins automatically.')

                        print()

                        for card in user_hand:

                            computer_card_pile.append(card)

                        user_hand.clear()

                        for card in war_card_list:

                            computer_card_pile.append(card)

                        war_card_list.clear()

                        x = 3

                        while x > 0:

                            computer_card_pile.append(computer_hand[0])

                            computer_hand.pop(0)

                            x -= 1

                        break

                    elif len(computer_hand) < 4:

                        print('The computer does not have enough cards for the war, so you win automatically.')

                        print()

                        for card in computer_hand:

                            user_card_pile.append(card)

                        computer_hand.clear()

                        for card in war_card_list:

                            user_card_pile.append(card)

                        war_card_list.clear()

                        x = 3

                        while x > 0:

                            user_card_pile.append(user_hand[0])

                            user_hand.pop(0)

                            x -= 1

                        break

                    else:

                        while war_counter > 0:

                            war_card_list.append(user_hand[0])

                            user_hand.remove(user_hand[0])

                            war_card_list.append(computer_hand[0])

                            computer_hand.remove(computer_hand[0])

                            war_counter -= 1

                        print('User Current Card: {}'.format(user_hand[0]))

                        print('Computer Current Card: {}'.format(computer_hand[0]))

                        print()

                        if card_value_dictionary[computer_hand[0]] < card_value_dictionary[user_hand[0]]:

                            print('Your card has a higher value, so you win the WAR!')

                            print()

                            for card in war_card_list:

                                user_card_pile.append(card)

                            war_card_list.clear()

                            user_card_pile.append(user_hand[0])

                            user_hand.remove(user_hand[0])

                            user_card_pile.append(computer_hand[0])

                            computer_hand.remove(computer_hand[0])

                            break

                        elif card_value_dictionary[computer_hand[0]] > card_value_dictionary[user_hand[0]]:

                            print('The computer\'s card has a higher value, so it wins the WAR!')

                            print()

                            for card in war_card_list:

                                computer_card_pile.append(card)

                            war_card_list.clear()

                            computer_card_pile.append(user_hand[0])

                            user_hand.remove(user_hand[0])

                            computer_card_pile.append(computer_hand[0])

                            computer_hand.remove(computer_hand[0])

                            break

                        else:

                            print('You and the computer both have the same value card, so there is still a WAR!')

                            print()

                            print('The compared cards, along with three other cards from each player\'s hand, will be '
                                  'put into the war pile.')

                            print()

                turn += 1

                # input('Press enter to continue: ')

                print()

            if len(user_card_pile) + len(user_hand) == 54:

                print('You got all of the cards! You WIN!')

                print()

                war_score['User Wins'] += 1

                war_score['Games Played'] += 1

                break

            if len(computer_card_pile) + len(computer_hand) == 54:

                print('The computer got all of the cards! The computer WINS!')

                print()

                war_score['Computer Wins'] += 1

                war_score['Games Played'] += 1

                break

            if len(user_hand) == 0:

                print('You ran out of cards!')

                print('The cards in your card pile will be put into your hand and shuffled a random amount of times.')

                print()

                for card in user_card_pile:

                    user_hand.append(card)

                user_card_pile.clear()

                shuffle_number = random.randint(1, 10)

                print('Your new hand was shuffled {} time(s).'.format(shuffle_number))

                while shuffle_number > 0:

                    random.shuffle(user_hand)

                    shuffle_number -= 1

                print()

                # input('Press enter to continue: ')

                print()

            if len(computer_hand) == 0:

                print('The computer ran out of cards!')

                print('The cards in the computer\'s card pile will be put into its hand and shuffled a random amount '
                      'of times.')

                print()

                for card in computer_card_pile:

                    computer_hand.append(card)

                computer_card_pile.clear()

                shuffle_number = random.randint(1, 10)

                print('The computer\'s new hand was shuffled {} time(s).'.format(shuffle_number))

                while shuffle_number > 0:

                    random.shuffle(computer_hand)

                    shuffle_number -= 1

                print()

                # input('Press enter to continue: ')

                print()

    def war_replay():

        print('Here is the score: ')

        print(war_score)

        print()

        while True:

            replay = input('Would you like to play again? ("Yes"/"No"): ')

            if replay.upper() == 'YES':

                print('Okay, let\'s go again!')

                x = 60

                while x > 0:

                    print()

                    x -= 1

                break

            elif replay.upper() == 'NO':

                print('Okay, good game!')

                print()

                game_selector_hub()

                break

            else:

                print('Please type either "Yes" or "No".')

                print()

    war_rules()

    while True:

        total_deck = create_deck()

        shuffled_deck = deck_shuffler(total_deck)

        player_decks = deck_dealer(shuffled_deck)

        gameplay_function(player_decks[0], player_decks[1])

        war_replay()


game_selector_greeting()

game_selector_hub()
