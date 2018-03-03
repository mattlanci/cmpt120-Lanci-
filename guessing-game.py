#Introduction to programming
#Matthew Lanci

animal = "lion"


def main():
    print ("What animal I am thinking of.")
    guess = input("What animal am I thinking of?" '')
    correct = False
    while not correct:
        if guess == 'q':
            quit(0)
        elif guess != 'lion':
            print("Incorrect... Try Again.")
            guess = input("What animal am I thinking of?" '')
            guess = guess.lower()
        else:
            print('Correct.  Well done!')
            next_question = input("Are you a fan of lions? ('y' or 'n') ")
            if next_question == "y":
                print ("I am too")
            else:
                print ("Guess I don't know you that well")
            return
        

main()
            
