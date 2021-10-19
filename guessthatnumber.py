import random

# determine if the number you have is too high perfect or too low.
def determine_number(num, random_num):
    if (num > int(random_num)):
        return print("Number is too high")
    elif (num < int(random_num)):
        return print("Number is too low")
    elif (num == int(random_num)):
        playagain = True
        return print("YOU GOT IT RIGHT!!!!!!"), playagain

def guess_number():
    
    print("Welcome to Guess that number!! \nTo Play Simply Enter a number between 1 and 10!\n")
    print("To Kill the program, type q, quit or Quit")
    random_inputs = random.randint(1,10)
    while True:
        inputs = input("Enter a number: ")
        if (inputs.lower() == "q" or inputs.lower() =="quit"):
            return print("Have a nice day!")

        #  Do not trust the user, convert input string to an int if its not a number  
        try:
            inputs = int(inputs)
            playagain = False
            playagain = determine_number(inputs, random_inputs)

            # You won you can play again if you want
            while playagain:
                if (playagain):
                    print("Do You want to play again?")
                    go_one_more_time = input("If YES type y or yes \nIf NO type q or quit: \n\n")
                    if (go_one_more_time.lower() == "y" or go_one_more_time.lower() == "yes"):    
                        guess_number()
                    elif (go_one_more_time.lower() == "q" or go_one_more_time.lower() =="quit"):
                        return print("Have a nice day!")
                    else: 
                        print("I do not understand what you mean, try again")

        except ValueError as e:
                print (e)
                print("IMPORTANT: Please only enter a number!!")
        
        

guess_number()