#final code- hangSNOMAN game Samin Charepoo

#these 4 lines of code imports the randomize function, opens the txt file with possible words for the game, reads it, splits the lines, and closes the file
import random
f=open("projectwords.txt")
word=f.read().splitlines()
f.close

def main():
#INPUT: none
#PROCESS: gets players names, starts F0PC, initializes different variabels, stores return values,checks conditions of guess, rotates between players and their turns, makes sure guess is valid, passes to next functions 
#extracredit included here- allows the player to repeat turn if they guess correctly
#OUTPUT: just prints different statements like validation of guess, says whos turn it is, etc.
    instructions()
    current_player=''
    player1=input("Player 1, enter your name:")
    player2=input('Player 2, enter your name:')
    players=[player1,player2]

    
    secret_word=random.choice(word).lower()
    blanks=['_']*len(secret_word)
    print (blanks) 
    wrong_guess_num=0
    guesses=[]
    (display(wrong_guess_num))
    initializeBlanks(secret_word)
    while wrong_guess_num<5  and '_' in blanks:
        if wrong_guess_num%2==0:
            current_player=player1
            print(player1, "it is your turn")
        else:
            current_player=player2
            print(player2, "it is your turn")

        guess=getGuess(guesses)
        if guess.isalpha():
            if guess in guesses:
                print ("You already guessed", guess,"- try again!")
            elif guess not in secret_word:
                print(guess, "is not in the word!")
                wrong_guess_num += 1
                guesses.append(guess)
            elif guess in secret_word:
                print(guess, "is is the word!")
                guesses.append(guess)
                fillInBlanks(secret_word,blanks,guess)


        else:
            print('This is not a valid guess. Pick a letter from the alphabet please!')

        statusReport(guesses,blanks, wrong_guess_num,secret_word,players)
        (display(wrong_guess_num))
    return guess
 

def instructions():
#INPUT: none
#PROCESS: print instructions
#OUTPUT: None
    print("Welcome to The Snowman game! Similar to the well known game of 'Hang Man', I will think of a word, and you will try to figure out the secret word by guessing letters or words! Each player will get one turn, if you guess a correct letter, you will go again. The winner is the player who finishes the word! Lets Begin!") 
          


def getGuess(guesses):
#INPUT: guesses
#PROCESS: prompts user to guess a letter, makes everything lower case
#OUTPUT: the letter guess
    guess=input("Guess a letter or word:").lower()
    print ('\n')
    return guess

def initializeBlanks(secret_word):
#INPUT: secret word
#PROCESS: create a list of blanks the correct length
#OUTPUT: the list of blanks
    blanks=['_']*len(secret_word)
    
def fillInBlanks(secret_word,blanks,guess):
#INPUT: secret word, blanks, guessed letter
#PROCESS: fill in list of blanks with guessed letter and acounts for muliple letters in a word
#OUTPUT: the new list of blanks and adjust the list as needed
    let=0
    for let in range(len(secret_word)):
                if secret_word[let]==guess:
                    blanks[let]=guess
    
                         
        
        
def statusReport(guesses,blanks, wrong_guess_num,secret_word,players):
#INPUT: guessed letter, blanks, wrong guess number, secret word, players
#PROCESS: report game status and lets the players knows where they stand, and in the end, who won/lost
#OUTPUT: None (just print statements so the client knows what’s up)
     print('letters guessed:', guesses)
     print(blanks) 
     if wrong_guess_num>=5:
         if '_' in blanks:
             print("You both lost! The secret word was",secret_word)
     elif '_' not in blanks:
         if wrong_guess_num%2==0:
             print(players[0], 'you have won! The secret word was',secret_word, "good job!")
         else:
             print(players[1], 'you have won! The secret word was',secret_word, "good job!")

def display(wrong_guess_num):
#INPUT: wrong Guess count
#PROCESS: print out the snowman-in-progress in between guesses, uses dictionary
#OUTPUT: None, just prints out the image
    image={
        0:"""

 

            ~~~
            """,
        1:"""
             
             
             O
            ~~~
            """,
        2:"""
             
             o
             O
            ~~~
            """,
        3:"""
             o
             o
             O
            ~~~
            """,
        4:"""
             o
             o \\
             O
            ~~~
            """,
        5:"""
             o
           / o \\
             O
            ~~~
            """}
    print (image[wrong_guess_num])

main()
