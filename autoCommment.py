#importing pyautogui lib for using the function who can write a comment 
import pyautogui
#importing time lib for using the stop function to make a delay 
import time
#importing random lib for using the randing function to generate random integer values
import random


#Generate Commenets list 
comments = ["Hi", 
            "Just commenting for fun",
            "Checking my python comment bot",
            "Just for fun",
            "I am just checking my python skill",
            "python is awesome", 
            "I am a messy programmer",
            "i love rock and roll music ", 
            "visca barca",
            "messi is the goat",
            "i love you baby", 
            "i support you",
            "thank god",
            "lovly!",
            "hey you",
            "listen to me", 
            "i love Panda bear",
            "do not talk to me like that",
            "Finally weekend",
            "dady is home",
            "watch it",
            "hey",
            "good morning",
            "good evening", 
            "morning", 
            "evening",
            "hi",
            "whatsup",
            "hola",
            "hey hey hows you?hows you?",
            "*nods*", 
            "hello, how you doing",
            "hello",
            "Welcome, I am good and you",
            "go to hell"]

#generate check integer variable to control the loop
check = int(0)
#generate target integer variable to define the end of the loop
target = int(1000)
#using sleep for waiting the user puting the cursor in comment field
#you should use this time as possible you can put the cursor in comment field
time.sleep(30)

# the main loop bassed on check and target
while check != target:
    # for loop every 10 times 
    for i in range(10):
        # make i as a random number between i and 35
        i = random.randint(i, 35)
        #generate random delay time between 5s and 120s 
        delay = random.randint(5,120)
        #writing a comment 
        pyautogui.typewrite(comments[i % 35])
        #pressing Enter 
        pyautogui.typewrite("\n")
        #making a delay randomised 
        time.sleep(delay)
    #updating check value    
    check += 10