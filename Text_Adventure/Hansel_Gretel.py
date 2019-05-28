""" Text Adventure """
from __future__ import print_function
import time
import sys
import random

class Story():
    """
    Class that will package the complete story
    """
    def __init__(self):
        self.name = "" #Makes it possible to have a different output 
                       #based on the name of the character
    def scene_1(self):
        """
        Function will package scene 1 and will allow it to be called multiple 
        times
        """
        response = raw_input("Do you want the instructions? (Yes/No) \n").lower()
        if response == "yes":
            print( 
                "Great, This game is based on the responses you input.",
                "Please write your answer the same way that it is written",
                "on the scene. However, captalization does not matter",
                sep="\n",
            )
        elif response == "no":
            print("Ok, continuing!")
        else:
            print("Please enter either a Yes or a No")
            self.scene_1()
    
    
    def scene_2(self):
        """
        Function will package scene 2 and hold all the story line and scene
        for the game, also allowing it to be called if needed
        """
        time.sleep(2)
        print(
            "\nNEWS REPORT: Two Kids are missing Baltic forest. With the ",
            "canabalistic witch lurking around, the only thing that we can do", 
            "for the kids is pray. They are a brother and sister, calling by",
            "the names Hansel and Gretel!",
            sep="\n",
        )
        response = raw_input("Do you want to be Hansel or Gretel? \n").lower()
        # import pdb; pdb.set_trace()
        if response == "hansel":
            print("Welcome Hansel! \n")
            self.name = "Hansel"
        elif response == "gretel":
            print("Ok, you are Gretel \n")
            self.name = "Gretel"
        else:
            print("Please enter a name \n")
            self.scene_2()
    
    
    def scene_3(self):
        """
        Function holds and packages scene 3 in order to be called when needed
        using raw_input and if then statments
        """
        response = raw_input(
            "We need to leave this forest. How do you think\n" + 
            "we will leave it. I don't know if I should go \nStraight \nLeft " + 
            "\nRight\n"
        ).lower()
        if response == "straight":
            print("You walked straight:")
            time.sleep(1)
            print("Look! There is a dragon, we need to ru..")
            time.sleep(1)
            print("The dragon had dinner today!")
            leave = raw_input("Do you want to leave? (Yes/No) \n")
            if leave == "yes":
                print ("Thank you for being the dragons lunch today")
                sys.exit()
            else:
                print("Restarting the game! \n")
                self.play_story()
        elif response == "left":
            print("You walked left:")
            time.sleep(1)
            print("where are we, it looks dark. Help us! Help ... (Crack)")
            time.sleep(1)
            print("The siblings were never seen again")
            leave = raw_input("Do you want to leave? (Yes/No) \n")
            if leave == "yes":
                print ("Thank you for being the dragons lunch today")
                sys.exit()
            else:
                print("Restarting the game! \n")
                self.play_story()
        elif response == "right":
            print("You walked right:")
            time.sleep(1)
            print(
                "Look! A candy house is up yonder. Let us see if we can get",
                "some food! Should we go? \n"
            )
        else:
            print("Please enter a direction!")
            self.scene_3()
    
    
    def scene_4(self):
        """
        Function packages code for scene 4 in order to it to be called and 
        hold the raw_inputs and responses of the game
        """
        response = raw_input("Do you want to go to the candy house (Yes/No) \
        \n").lower()
        if response == "yes":
            print("Great, lets go to the candy house")
            time.sleep(1)
        elif response == "no":
            leave = raw_input("Do you want to leave? (Yes/No) \n").lower()
            print("You sure about that! But, we won't have shelter. Okay, fine!")
            time.sleep(1)
            print("A few months later...")
            time.sleep(2)
            print(
                "Hansel! Brother Hansel! Wake up! We need to get food!", 
                "Brother get up. Brother, brother!!", 
                sep="\n", 
            )
            time.sleep(1)
            if leave != "no":
                print("I need to leave this place! Help me! Help me!")
                time.sleep(1)
                sys.exit()
            else:
                print(
                    "Okay. Look, there is a time machine. I must go back in",
                    "time to help save my brother! I hope it works! I\'m " +
                    "coming brotherrrr!", sep="\n"
                )
                self.scene_4()
        else:
            print("Please enter either a Yes or a No")
            self.scene_4()
    
    
    def scene_5(self):
        """
        Function holds and packages code of scene 5 that holds the code and 
        story using raw_inputs, if then statments and using a variable response
        """
        print(
            "I am hungry, can we have some candy. I believe that we need", 
            "food!", 
            sep="\n",
        )
        response = raw_input("Do you want to eat the candy? (Yes/No) \n").lower()
        if response == "yes":
            print("Great, lets have some candy!")
            return False
        elif response == "no":
            leave = raw_input("Do you want to leave? (Yes/No) \n")
            if leave != "No":
                print(
                    "I do not believe that eating is the good answer. I say", 
                    "that we leave this tisby land and find our way home. ", 
                    sep="\n", 
                )
                time.sleep(1)
                sys.exit()
            else:
                print("Okay...")
                self.scene_5()
        else:
            print("Please enter either a Yes or a No")
            self.scene_5()
    
    
    def scene_6(self):
        """
        Function holds the code and packages it since it is using print, if then 
        statements and also raw_imputs, creating leave and response variables
        """
        print(" \nWe ate too much candy. I can't move. \n")
        time.sleep(1)
        print("Enter the witch \n")
        time.sleep(0.5)
        print("Welcome children! Are you enjoying my house. Wuah Wuah Wuah!")
        time.sleep(0.5)
        print("Someone help us! Gretel run for your life!")
        time.sleep(0.5)
        print("Witch: I can\'t let that happen")
        time.sleep(1)
        print("Gretel, save me! The witch captured me!")
        if self.name == "Hansel":
            print("You were locked up in the dungeon, getting ready to be eaten")
        elif self.name == "Gretel":
            response = raw_input("Do you want to save Hansel!? (Yes/No) \n").lower()
            if response == "yes":
                print("You are a valued girl. Worthy to be a knight! Go quick! \n")
                time.sleep(1)
                print("Gretel ran back into the house, ready for the battle! \n")
            elif response == "no":
                print(
                    "You ran away from the house, leaving your brother",  
                    "behind and allowing him to burn alive",
                    sep="\n",
                )
                sys.exit()
            else:
                print("You didn't answer in time, killing your brother!")
                sys.exit()

    def scene_7(self):
        """
        Function packages the code of scene 7 in order for it to be called by
        and uses the variable name and it will create different situations based 
        on the character
        """
        response = raw_input("Do you want to talk to the witch? (Yes/No) \n"
            ).lower()
        if self.name == "Hansel":
            if response == "yes":
                print(  
                    "Ms.Witch, please don't eat me. I am small and scrawny,", 
                    "weak and bony, not got enough for you to eat. Give me a", 
                    "chance to survive, or I will be your feast.", 
                    sep="\n", 
                )
                time.sleep(0.7)
                print(
                    "Little boy, I will give you a chance to survive if you",
                    "answer a riddle, do you wan to do it?",  
                    sep="\n",
                )
            elif response == "no":
                print(
                    "Why don't you want to talk to me! Well, you won't be able", 
                    "to talk soon. Bye, bye boy!"
                )
                sys.exit()
            else:
                print("Boy! You have no options. You will die in my pot. ", 
                    "You will be a great pie for me.",
                    sep="\n",
                )
                sys.exit()
        else:
            if response == "yes":
                print(
                    "Ms.Witch, please don't eat my brother. He is small and", 
                    "scrawny, weak and bony, not got enough for you to eat.", 
                    "Give him a chance to survive, or we will be your feast.",
                    sep="\n",
                )
                time.sleep(0.7)
                print("Little girl, I will give you a chance to survive if you", 
                    "answer a riddle, do you wan to do it",
                    sep="\n",
                )
            elif response == "no":
                print("You enter the room:")
                time.sleep(1)
                print(
                    "You came to the oven, seeing Hansel ", 
                    "\"I\'m here brother! I here to save you\"",
                    sep="\n"
                )
                time.sleep(0.7)
                print(
                    "The witch saw you! \n \" Why hello girl! You can also" , 
                    "be a beautiful pie. Be with your brother!", 
                sep="\n",
                )
                time.sleep(0.7)
                print(
                    "You look at Hansel, but the witch swiftly goes and ", 
                    "captured you. You joined Hansel in the pot. You plan FAILED", 
                    sep="\n"
                )
            else:
                print("You were thinking too long, letting the Witch boil Hansel!")
                sys.exit()
    
    def scene_8(self):
        """
        Function holds and packages code of the riddle in order to create the 
        ending of the game using the riddle answers. This is using a raw_input 
        and having multiple riddles
        """
        print("Here is the riddle: \n")
        riddle_1 = "My first is often at the front door.\n" \
                    "My second is found in the cereal family.\n" \
                    "My third is what most people want. \n" \
                    "My whole is one of the United States. \n" \
                
        riddle_2 = "My life can be measured in hours, \n" \
                    "I serve by being devoured. \n" \
                    "Thin, I am quick \n" \
                    "Fat, I am slow \n" \
                    "Wind is my foe."
        riddle_3 = "It is greater than God and more evil than the devil.\n" \
                    "The poor have it, the rich need it and if you eat it" \
                    "you will die.\n" \
                    "What is it? \n"
        riddle_4 = "What always runs but never walks, often murmurs, never \n" \
                    "talks, has a bed but never sleeps, has a mouth but never" \
                    "eats?"
        riddle_5 = "What begins and has no end?" \
                    "What is the ending of all that begins?"
        riddle_list = [
            riddle_1, 
            riddle_2, 
            riddle_3, 
            riddle_4, 
            riddle_5
        ]
        riddle_ans = [
            "matrimony", 
            "candle" , 
            "nothing" , 
            "river", 
            "death"
        ]
        riddle = random.choice(riddle_list)
        riddle_num = riddle_list.index(riddle)
        print(riddle)
        response = raw_input("Answer:").lower()
        
        if response == riddle_ans[riddle_num]:
            print(
                "Congratulation! You got the right answer! However, I ",
                "am going to eat you! You kids will be stuck here ", 
                "forever.You will never win. That is why I am a bad witch! ", 
                sep="\n"
            )
            print(
                "Crash! The door breaks! Comes in is a voracious dragon. ", 
                "Fire coming everywhere. It came to save you, since you ", 
                "didn\'t wake it up when it was sleeping in his cave!",
                sep="\n",
            )
            sys.exit()
        else:
            print("Sorry! That is Wrong. Bye, Bye!!!!")
            time.sleep(1)
            print("HELP! SOMEBODY! HEL.....!")
            sys.exit()
    def introduction(self):
        """
        Function packages and code for the instruction of the game, giving the background 
        information
        """
        print( 
            "It wasn't a dark and stormy night, but a nice and beautiful day.", 
            "Two kids are walking with their father, walking into the woods.",
            "But then, due to their idiotic father, they got lost in the forest by", 
            "themselves. Scared, they need your help!!",
            sep="\n",
        )
        time.sleep(2)
        print("This is created by Sragvi Vadali and Tanish Baranwal \n\n\n\n")


    def play_story(self):
        """
            Function that runs all scene functions
        """
        self.introduction()
        self.scene_1()
        self.scene_2()
        self.scene_3()
        self.scene_4()
        self.scene_5()
        self.scene_6()
        self.scene_7()
        self.scene_8()

story = Story()
story.play_story()