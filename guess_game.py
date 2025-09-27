# Let's play a game where you guess a number I have in mind

import random

print ('Hi, I have a number in mind, can you guess it?')
print ('You have 5 guesses!')

for num in range(6):
     guess=int(input())
     correct_guess=random.randint(1,10)
   
     if guess < correct_guess:
        print ('Your guess is lower than the number.')

     elif guess > correct_guess:
        print ('Your guess is higher than the number.')
     else:
      break
     


if guess == correct_guess:
        print ('You won in ' + str(num) +' guesses')
else:
    print ('You lost, the number I was thinking of is ' + str(correct_guess))

