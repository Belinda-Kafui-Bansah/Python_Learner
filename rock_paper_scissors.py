import random, sys
print ('Rock, Paper, Scissors')

#variables for keeping track of achievements
wins = 0
losses = 0
ties = 0

#The main game

while True:
    print (f'{wins} Wins, {losses} Losses, {ties} Ties')
    print('Rock, Paper, Scissors  or Quit. Enter your move (r or p or s or q)')
    player_input = input()

    if player_input == 'q':
        sys.exit()            #Quit the game

#Player choice
    elif player_input == 'r':
        print ('ROCK versus...')
    elif player_input == 'p':
        print ('PAPER versus...')
    elif player_input == 's':
        print('SCISSORS versus...')

# Computer's choice
    random_number = random.randint(1,3)
    if random_number == 1:
        computer_move = 'r'
        print ('ROCK')
    elif random_number == 2:
        computer_move = 'p'
        print ('PAPER')
    elif random_number == 3:
        computer_move = 's'
        print ('SCISSORS')

#Display of record
    if player_input == computer_move:
        print ('It is a tie!')
        ties = ties + 1
    elif player_input == 'r' and computer_move == 's':
        print ('You win!')
        wins = wins + 1
    elif player_input == 'p' and computer_move == 'r':
        print('You win!')
        wins= wins + 1
    elif player_input == 's' and computer_move == 'p':
        print('You win!')
        wins= wins + 1
    elif player_input == 'r' and computer_move == 'p':
        print('You lose!')
        losses = losses + 1
    elif player_input == 'p' and computer_move == 's':
        print('You lose!')
        losses = losses + 1
    elif player_input == 's' and computer_move == 'r':
        print('You lose!')
        losses = losses + 1


   