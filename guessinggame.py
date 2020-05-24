import requests
import pprint
import json
import random
import time as t
#Created game for udemy exercises, link below.
#https://www.udemy.com/course/learn-python-programming-a-step-by-step-course-to-beginners/learn/lecture/13761308#overview
#The main thing to do in this game is to ask random generated questions and to get andsers
#I'm going to create multiple choice with one chance of guessing.
#Questions are generated automatic by webside: https://opentdb.com/api_config.php

r = requests.get("https://opentdb.com/api.php?amount=10&type=multiple")
questions=json.loads(r.text)
print("Welcome to my game.\nGUESS IN FIRST SHOT")
guess = input("If you want quit,type 'quit', other whise press enter. ")
right = 0
wrong = 0


while guess.lower() != 'quit':
    t.sleep(2)
    number = random.randint(0,9)
    category = questions['results'][number]['category'].replace("&quot;","'").replace("&#039;","'")
    ask = questions['results'][number]['question'].replace("&quot;","'").replace("&#039;","'")
    correct_answer = questions['results'][number]['correct_answer'].replace("&quot;","'").replace("&#039;","'")
    incorrect_answers = questions['results'][number]['incorrect_answers'] + [correct_answer]
    random.shuffle(incorrect_answers)
    print("#"*80)
    print("# ","Category: {:^64}".format(category)," #")
    print("#","-"*76,"#")
    print("#","{:76}".format("The question is:"),"#")
    print("#","{:^76}".format(ask),"#")
    print("#","-"*76,"#")
    print("# {:75}".format("Posible andswers:")," #")
    print("# {:75}".format(incorrect_answers[0])," #")
    print("# {:75}".format(incorrect_answers[1])," #")
    print("# {:75}".format(incorrect_answers[2])," #")
    print("# {:75}".format(incorrect_answers[3])," #")
    guess = input("# ")
    print("#","-"*76,"#")
    
    if guess == correct_answer:
        guess = input("#{:78}#\n#{:78}#".format(" You are right!","Wana play again?"))
        right += 1
    elif guess.lower() == 'quit':
        break
    else:
        print("#{:78}#\n#{:78}#".format(" You are wrong!","Wana play again?"))
        guess = input("# ")
        wrong += 1
        

print("#"*80)

#Get total score after ending the game
print("Your total score:\nRight answers: {}\nWrong answers: {}".format(right,wrong))
print("Total number of questions: {}".format(right+wrong))
