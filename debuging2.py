# Yeh rock paper scissors game ka program hai. Iss game ko aap 
# computer ke against kheloge. Iss game ke 3 rules hai

# Rock Paper se haar jata hai
# Paper Scissors se haar jaata hai
# Aur, Scissors Rock se.

# Appko pehle rock,paper ya scissors mei se chose karna hoga.
# Aur uske baad computer randomly inme se ek option chose karega. 
# Firr, upar diye gaye rules ke hisab se result aayega. Jaise:

# Agar aapne "Rock" chose kiya aur computer ne "Scissors"
# To aap jeet jaoge kyunki "Rock" "Scissors" ko hara deta hai. ( Rule 3 )
# Aap iss game ke rules iss

# se seekh sakte hai.

# Topics covered:

# semantic/syntactic problems in if/else

# semantic error in while conditions

# errors in variable naming

import random
while True:
    player_choice = input('What do you pick? (rock, paper, scissors):')
    moves = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(moves)
    print(f"\nYou chose {player_choice}, computer chose {computer_choice}.\n")
    if player_choice == computer_choice:
        print (f"Both players selected {player_choice}.Draw!")
    elif  player_choice== 'rock':
        if 'computer_choice' == 'scissors':
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")    
    elif  player_choice== 'paper':
        if 'computer_choice' == 'rock':
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")    
    elif player_choice == 'scissors':
        if 'computer_choice' == 'paper':
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")    
    again = input('Do you want to play again? (y or n):')
    if again.lower()!='y':
        print('Game...Over')
        break
