from __future__ import print_function
import random
import time

def hangman():
    """
    Packages all the code into the function to make the code in a singular area 
    and have the code present only needing to call hangman() in order to play 
    and calling the other functons inside the hangman code making it or organized
    and consisting of many functions for the game 
    """
    def welcomeScreen():
        """
        Packages the code that will initialize the game and the introduces the 
        game with the rules and the question, using time function and a name 
        variable
        """
        print("WELCOME TO YOUR FAVORITE GAME")
        time.sleep(1)
        print("SAT PREP")
        print(
            "THIS IS A FUN GAME TO HELP SIMULATE THE SAT AND GET YOU A GOOD",
        "GRADE",
        )
        
        name = raw_input("ENTER YOUR NAME:")
        
        if name == "Sragvi" or name == "Adam Brown" or name == "Mr.Brown":
            print("YOU WON THE GAME! A SMART PERSON IS NAMED SRAGVI SO YOU ", 
            "DON\'T NEED TO PLAY! (or if your the teacher :)",)
            second_chance = raw_input("YOU CAN PLAY IF YOU WANT?(yes/no)")
            if second_chance == "yes": #adding a fun spin to the game
                print("WELCOME", name.upper(), "TO MY SMALL GAME!")
                print("#######################################################")
                time.sleep(0.5)
                print("NO UPPERCASES!!!!!!!!!!!")
                print("ONLY TYPE A LETTER UNLESS ....")
                print("NOW LETS BEGIN:")
                
            else:
                print("IT IS OKAY TO NOT PLAY v__v")
                return
        else:
            print("WELCOME", name.upper(), "TO MY SMALL GAME!")
            print("################################################################")
            time.sleep(0.5)
            print("NO UPPERCASES!!!!!!!!!!!")
            print("ONLY TYPE A LETTER UNLESS .....")
            print("NOW LETS BEGIN:")
            
        game_code() #Calling the gamecode

        
###############################################################################
#          Hints values that hold definitions                                 #
###############################################################################
    Polka = "a lively dance of Bohemian origin in duple time"
    Quad = "a type-metal space that is one en or more in width"
    Quip = "a clever usually taunting remark"
    Abnegation = "the denial and rejection of a doctrine or belief"
    Numbskull = "a stupid or foolish person"
    Sphinx = "mythical creature with the head of a human and the", 
    " body of  an animal",
    Squawk = "make a loud, harsh noise"
    Swivel = "a coupling between two parts enabling one to revolve without", 
    " turning the other"
    Assiduous = "showing great care and perseverance"
    Klutz = "a clumsy, awkward, or foolish person"
    Memento = "an object kept as a reminder or souvenir of a person or event" 
    Waxy = "resembling wax in consistency or appearance"
    Wildebeest = "another term for gnu"
    Yacht = "a medium-sized sailboat equipped for cruising or racing"
    Zealous = "fervent, filled with eagerness in pursuit of something"
    Crypt = "an underground room or vault beneath a church, used as a chapel or",
    " burial place",
    Zippy = "bright, fresh, or lively"
    Cajole = "to urge, coax"
    Bombastic = "high-sounding but with little meaning; inflated"
    Inchoate = "just begun and so not fully formed or developed; rudimentary"
###############################################################################
#                       To generate a secret and hint                         #
###############################################################################
    """Start of the game and the secrets and hints of the game"""
    words = ["Polka", "Quad","Quip","Abnegation","Numbskull","Sphinx",
    "Squawk", "Swivel","Assiduous","Klutz","Memento","Waxy","Wildebeest","Yacht",
    "Zealous","Crypt","Zippy","Cajole ", "Bombastic", "Inchoate"]
    hints = [Polka, Quad, Quip, Abnegation, Numbskull, Sphinx, Squawk, Swivel, 
    Assiduous, Klutz, Memento, Waxy, Wildebeest, Yacht, Zealous, Crypt, Zippy,
    Cajole, Bombastic, Inchoate]
    
    secret = random.choice(words)
    
    hint_number = words.index(secret)
    
    def make_global():
        """
        This packages code that globalizes vaiables to itcan be used in other 
        functions and not just the function it is in. 
        """
        global validLetters
        validLetters = "abcdefghijklmnopqrstuvwxyz"
        
        
        global secret
        
        secret = random.choice(words)
        
        global hint_number
        
        hint_number = words.index(secret)
        
    def game_code():
        """
        This code packages all the coding for the game such as the secret word 
        and the hint and finally what letter you can use so no uppercase or any
        random number. Also holding a simulated ASKER that will simulated a 
        hangman with only print functions
        """
        make_global()
        
        validLetters= "abcdefghijklmnopqrstuvwxyz"
        
        turns = 10
        
        guessed = ""
        
        
        while turns > 0:
            msg = ""
            missed = 0
            print(secret)
            for letter in secret:
                if letter in guessed:
                    msg = msg + letter
                else:
                    msg = msg + "_" + " "
                    missed += 1
            if msg == secret:
                print(msg)
                print("YOU ARE CORRECT, THE WORD WAS: ", secret)
                break
            print(msg)
            guess = raw_input("GUESS THE WORD: ")
            
            if guess in validLetters:
                guessed = guessed + guess
                print("YOU HAVE ", turns, "LEFT!")
            elif guess == "hint":
                print(hints[hint_number])
            elif guess == "math":
                math_problems = ["10 * 14", "(76+79)^(45646-((5705*8)+6)", 
                "50*(58818614681861861818-58818614681861861817)"]
                math_ans = ["140", "1", "50"]
                math = random.choice(math_problems)
                ans_num = math_problems.index(math)
                print(math)
                guess_num = raw_input("Please solve the problem:")
                if guess_num == math_ans[ans_num]:
                    print("Congratulation, you solved the problem! You get two", 
                    " more guesses!")
                    turns += 2
                    print("YOU HAVE", turns, "LEFT!")
                else:
                    print("You lost two guesses!")
                    turns -= 2
                    print("YOU HAVE", turns, " GUESSES LEFT!")
                game_code()
            elif guess == "break":
                return "Thank you for playing!!"
            elif guess.lower() == secret.lower():
                print("CONGRATULATION, YOU ACTUALLY GOT THE ANSWER CORRECT! ",
                "YOU CAN GET A 1600 IN THE SAT!"
                )
                restart_button()
            else:
                print("ENTER A VALID LETTER")
                print(msg)
                guess = raw_input("GUESS THE WORD: ")
            
            if guess not in secret: #Code that simulates ASKER for the game
                turns -= 1
                if turns == 9:
                    print("  o")
                if turns == 8:
                    print("  o")
                    print("  |")
                if turns == 7:
                    print("  o")
                    print("  |")
                    print("  \ ")
                if turns == 6:
                    print("  o")
                    print("  |")
                    print(" / ")
                if turns == 5:
                    print("  o")
                    print("  |")
                    print(" / \ ")
                if turns == 4:
                    print("  o")
                    print("  |")
                    print("_/ \_ ")
                if turns == 3:
                    print("  o")
                    print("  |-")
                    print("_/ \_ ")
                if turns == 2:
                    print("  o")
                    print(" -|-")
                    print("_/ \_ ")
                if turns == 1:
                    print("YOU HAVE FAILED TO GUESS THE WORD:", secret)
                    print("YOU WILL NEVER GET 100% WITHOUT A CURVE!")
                    print("YOU DIED FROM STRESS, LEADING THERE TO BE NO RESTART")
                    time.sleep(1)
                    turns -= 2
                    restart_button() #Calling the function below
            def hangman_display():
                """
                Function packages code using no functions and will simulate a game to 
                check if a letter is in the secret and showing the display_word variable
                to display the word snd the numbe of letters in the secret code to 
                create a hangman game code.  
                """
                display = ""
                
                for char in secret:
                    if char in guess:
                        display += char
                    elif char == " ":
                        display += char
                    else:
                        display += "-"
    def restart_button():
        """
        Using no aurguments, thsi function is creating a restart button for the 
        game using the variable restart that is holding a raw_input and using if
        then statments to create variation for the answer
        """
        restart = raw_input("\nWOULD YOU LIKE TO RESTART(yes/no)? \n")
        if restart == "yes":
            print("OKAY LET US BEGIN ....")
            time.sleep(1.3)
            welcomeScreen()
        else:
            print("YOU DID THE SMART THING GOING OUT OF THE LOOP!")
            end_scene()
    def end_scene():
        print("THANK YOU FOR PLAYING MY GAME")
        time.sleep(1)
        print("CREATED BY SRAGVI VADALI")
        break_code()
    def break_code():
        """
        This code will stop the other code from runing the loop and will end 
        the game_code
        """
        print("THANK YOU FOR BREAKING THE CODE")
        break_code()
    welcomeScreen()
       
hangman()