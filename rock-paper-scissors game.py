import random

def game():
    
    user_points = int()
    computer_points = int()
        
    options = ['rock', 'paper', 'scissors']

    while True:

        computer_pick = random.choice(options)

        user = input('Enter rock, paper or scissors: ').lower()
        
        if user == 'q':
            break

        if user not in options:
            print('-Invalid choice!\n')
            continue
        

        elif user == 'rock' and computer_pick == 'scissors':
            user_points += 1
            print(f'-The computer picked {computer_pick}. \nYou won!\n')
            
        elif user == 'paper' and computer_pick == 'rock':
            user_points += 1
            print(f'-The computer picked {computer_pick}. \nYou won!\n')
            
        elif user == 'scissors' and computer_pick == 'paper':
            user_points += 1
            print(f'-The computer picked {computer_pick}. \nYou won!\n')
            
        elif user == computer_pick:
            user_points += 0
            computer_points += 0
            print (f'-The computer picked {computer_pick}. \nIts a draw!\n')
                
        else:
            computer_points += 1
            print(f'-The computer picked {computer_pick}. \nThe computer won!\n')
            
    print(f'\n-You won {user_points} times. \n-The computer won {computer_points} times. \n-Goodbye! \n')
    
game()