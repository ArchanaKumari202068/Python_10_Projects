# a dictionary that stores question and answers
# have a variable that tracks the scores of the player
# loop through the dictionary using the key values pairs
# display each questions to the user and allow them to answer
# tell them if they are right or wrong
# show the final result when quiz is completed

quiz = {
    "question1": {
        "question":"what is the capital of France?",
        "answer":"Paris"

    },
    "question2":{
        "question":"What is capital of Germany?",
        "answer":"Berlin"
    },
        "question3":{
        "question":"What is capital of Italy?",
        "answer":"Rome"
    }, 
       "question4":{
        "question":"What is capital of Spain?",
        "answer":"Madrid"
    }, 
       "question5":{
        "question":"What is capital of Portugal?",
        "answer":"Lisbon"
    }, 
       "question6":{
        "question":"What is capital of Switzerland?",
        "answer":"Bern"
    },
        "question7":{
        "question":"What is capital of Austria?",
        "answer":"Vienna"
    },


}

score = 0

for key,value in quiz.items():
    print(value['question'])
    answer =input("Answer?")
     
     # check ans is correct or not
    # python is case sensitive 
    # so we use .lower ans =Ans is wrong
    if answer.lower() == value['answer'].lower():
        print('Correct')
        score = score + 1
        print("Your score is :"+str(score))
        print("")
        print("")

print("You got " + str(score) + "out of 7 questins correctly")
print("Your Percentage" + str(int(score/7 * 100)) + "%")
