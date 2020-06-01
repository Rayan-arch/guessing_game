import requests
import pprint
import json
import random
import html

#Created game for udemy exercises, link below.
#https://www.udemy.com/course/learn-python-programming-a-step-by-step-course-to-beginners/learn/lecture/13761308#overview
#The main thing to do in this game is to ask random generated questions and to get andsers
#I'm going to create multiple choice with one chance of guessing.
#Questions are generated automatic by webside: https://opentdb.com/api_config.php

print("Welcome to my game.\nGUESS IN FIRST SHOT")
guess = input("If you want quit,type 'quit', other whise press enter. ")
right = 0
wrong = 0

while guess.lower() != 'quit':
    invalid_guess = False
    url = "https://opentdb.com/api.php?amount=1&difficulty=easy&type=multiple"
    r = requests.get(url)
    questions=json.loads(r.text)
    category = questions['results'][0]['category']
    ask = questions['results'][0]['question']
    correct_answer = questions['results'][0]['correct_answer']
#Import all answers and suffleing them with correct answer.
    answers = questions['results'][0]['incorrect_answers'] + [correct_answer]
    random.shuffle(answers)
    number = 1
#Creating table with question and andswers
    print("#"*80)
    print("# ","Category: {:^64}".format(category)," #")
    print("#","-"*76,"#")
    print("#","{:76}".format("The question is:"),"#")
    print("#","{:^76}".format(html.unescape(ask)),"#")
    print("#","-"*76,"#")
    print("# {:75}".format("Posible andswers:")," #")
    print("#","-"*76,"#")
    for answer in answers:
        print("# {}. {:72}".format(number,html.unescape(answer))," #")
        number += 1
    print("#","-"*76,"#")
#Simple findout if user type number and not letter.
#I will try to do it right.
    while invalid_guess == False:
        guess = input("# ")
        try:
            user_guess = int(guess)
            if user_guess > len(answers) or user_guess <= 0:
                print("# {:76} #".format("# {:76} #".format("Incorect value.")))
            else:
                invalid_guess = True
        except:
            print("# {:76} #".format("Invalid andswer. Use only numbers!"))
            
    guess = answers[int(guess)-1]
    print("#","-"*76,"#")
#Final statment, check if answer is correct.   
    if guess == correct_answer:
        print("#{:78}#".format(" You are right!"))
        right += 1
    else:
        print("#{:78}#".format(" You are wrong!"))
        wrong += 1
        
    print("# {:76} #".format("If you want to play again press enter, other whise type 'quit'"))
    guess = input("# ")
    
        
        

print("#"*80)

#Get total score after ending the game
total_score = print("Your total score:\nRight answers: {}\nWrong answers: {}".format(right,wrong))
total_score2 = print("Total number of questions: {}".format(right+wrong))
print("Do you want to save your score to file?(Y/N)")
file_answer = input()
if file_answer.lower() == 'y':
    ys=open("YourScore.txt",'x')
    ys.write(total_score+"\n"+total_score2)
else:
    print("Goodbye!!!")
