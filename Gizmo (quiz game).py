#python quiz

questions=("how many elements are in the periodic table?:",
           "which animals lay the largest eggs?:",
           "what is the most abundant gas in the atmosphere?:",
           "How many bones are in the human body?:",
           "Which planet in the solar system is the hottest?:")


options=(("A 116","B117","C118","D119"),
         ("A whale","B crocodile","C elephant","D Ostrich"),
         ("A Nitrogen","B Oxygen","C Carbon-dioxide","D Hydrogen"),
         ("A  206","B 207","C 208","D 209"),
         ("A Mercury","B Venus","C Earth","D Mars"))

answers=("C", "D","A","A","B")
guesses=[]
score=0

questions_num=0


for question in questions:
    print("-------------")
    print(question)
    for  option in options[questions_num]:
        print(option)

    guess=input("Enter (A,B,C,D):").upper()
    guesses.append(guess)
    if  guess==answers[questions_num]:
        score+=1
        print("Correct")
    else:
        print('Incorrect')
        print(f"{answers[questions_num]} is the correct answer")
    questions_num +=1

print(" answers:", end=" ")

for answer in answers:
    print(answer, end=" ")

print(" answers:", end=" ")

for guess in guesses:
    print(guess, end=" ")

score= int(score/ len(questions)* 100)
print(f"Your score is {score}")