#!/usr/sbin/python3

'''
 A quiz show program

'''


#show the banner for the game
def showBanner():
    print("********** Welcome to 'Whose the Best Techie Ever?' **********")
    print("**************************************************************")

#Display a list of choices
def printChoices():
    print("A - Steve Jobs\n")
    print("B - Zach Feeser\n")
    print("C - Linus Torvalds\n")


def main():
    showBanner() # print the banner

    # get the player's name
    contestant = input("Contestant what's your name? ") 


    # Dipsplay choices
    printChoices()

    # Ask the question
    instrChoice = input("Which of these instructors is the best of all time? ") 

    # Check the answer. If correct then congratulate else say bye-bye
    if instrChoice.upper() == 'B':
        print("That's correct! Jim tell our contestant what they won today!")
    else:
        print("\nI'm sorry that's not correct, but thanks for playing.\n")






if __name__ == "__main__":
    main()
