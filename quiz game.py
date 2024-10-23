questions = ("what is your district name?: ",
           " which animal lays the largest eggs? :")
options =(("A. Bagherhat", "B. Jhalakathi", "C.Dhaka", "D.Ctg"), 
         ("A. Whale", "B.Crocodile", "C.ELephant", "D.Ostrich"))


answers =("B","D")
guesses = []
score = 0
question_num =0
 

for question in questions:
    print (" --------------")
    print (question)
    for option in options[question_num]:
     print(option)

    guess = input("Enter (A,B,C,D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
       score += 1
       print("Correct")
    else: 
       print("Incorrect")
       print(f"{answers[question_num]} is the correct answer: ")
    question_num += 1

print("    Result    ")

print ("answers: ",end="")
for answer in answers:
   print(answer ,end =" ")
print()

print("guesses: ",end ="")
for guess in guesses:
   print(guess ,end =" ")
print()

score = int(score /len(questions)* 100)
print(f"your score is :{score}%")