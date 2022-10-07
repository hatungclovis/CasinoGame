# Welcome to Casino game designed by Clovis H.
import sys
from random import randrange
from math import ceil

totalmoney=10       # You have $10 to start with for this game
trials=3            # You have 3 times to lose all the $10 before game over.

# defining functions that will take care of some specific tasks in our program.
# This function simply displays the welcome menu of the game.
def welcome():

    print ('Welcome to the Casino game designed by CLOVIS HATUNGIMANA.')
    print('You have ${} to play this game.'.format(totalmoney))
    print ('You can quit at any time by pressing x.')
    return

# after losing the $10, this function displays how many times you are can replay the game.
def trial():
    print('You have {} imes to replay the game.'.format(trials))
    return

#this function takes the user input and checks if it is in numbers.
def get_user_number():
    
    a=True             #this is a place holder for our "while" loop.
    while a==True:
        
        user_number=input('Type your lucky number from 1 to 50:')
        if user_number=='x':
            sys.exit('You quit the game.')
        
        else:
            try:
                user_number=int(user_number)
                
                if user_number in range(1,51):
                    
                    if user_number%2==0:
                        colour='black colour'
                    
                    elif user_number%2!=0:
                        colour='red colour'
                    print ('Your lucky number is {}. It is of {}.'.format(user_number,colour))
                    return user_number
                else:
                    print('Your number is not between 1 to 50. Try again.')
            
            except:
                print('Your input is not a number. Try again.')

# A function for getting and checking the money for betting
def get_user_bet_amount():
    
    b=True          
    while b==True:
        
        amountbet=input('In integers, write the amount of money you want to bet:')
        if amountbet=='x':
            sys.exit('You quit the game.')                
        else: 
            try:
                amountbet=int(amountbet)
                
                if amountbet <= totalmoney and amountbet>0:
                    
                    print('Wait for the lucky number to be revealed.')
                
                    return amountbet
        
                elif amountbet>totalmoney:
                    print('You cannot exceed ${}.'.format(totalmoney))
                elif amountbet<0:
                    print('You cannot input negative numbers.')
                elif amountbet==0:
                    print('You cannot bet on zero $. Try again.')
            except:
                print('Please, write your money in digits.')

# defining a function that will generate a true luky number

def lucky_number():
    return randrange(1,51)

# A function that gets userbet and luky number and calculates gains or losses
def gain_calculation(user_bet, user_lucky_number,luckynumber, total_money):
    
    if user_lucky_number==luckynumber:

        user_bet = user_bet * 3
        print('Your lucky number is the winner.')
        print('You earned ${}.'.format(user_bet))
        total_money +=user_bet
        
        
    elif user_lucky_number %2== luckynumber%2 and user_lucky_number != luckynumber:
                                            
        user_bet= ceil(user_bet * 0.5)
        print('You got right only the color of the lucky number.')
        print('You earned ${}.'.format(user_bet))
        total_money +=user_bet
        
                                    
    else:
        
        total_money =total_money - user_bet
        if total_money==0:
           
            print('You lost this round.')
            
    print('Now, your total is:',total_money)        
    return total_money

#defining a function that allows the user to continue or quit the game after each round.

def continu():
    
    d=True
    while d==True:
        choice=input ('Press y to continue. Press x to quit the game.')
    
        if choice=="y":
            
            d=False
        elif choice=='x':
            sys.exit('You quit the game.')
        else:
            print('Incorrect input. Try again!')
    return
# Main body of our code

welcome()

while trials>0:
    
    #retrieving values of the lucky number and user input from our defined functions
    number = get_user_number()
    amountbet = get_user_bet_amount()
    luckynumber = lucky_number()
    
    print()       #empty line for a better display (spaced display) of the output
    print('The lucky number is:',luckynumber)
    
    #calculating the amount the user will now have after the lucky number has been revealed
    totalmoney = gain_calculation(amountbet, number,luckynumber,totalmoney)
        
    if totalmoney == 0:
        trials -=1
        
        print ('You remain with {} trials.'.format(trials))
        
        if trials==0:
            print ('Sorry. Game over!')
         
        else:
           totalmoney=10
           print('Now, you have',totalmoney) 
           continu()    # continu() is the function that allows the user to continue or quit after each round.
        
    else:
        continu()
         
    
        
    
    







    