print("Welcome to my Quizz Game")
play = input("do you wanna play?")
if play.lower() != "yes":
    quit()
print("less play :)")
score = 0 

answer = input("1. what is the stand of CPU? ")
if answer.lower() == "central processing unit":
    print("correct")
    score += 1
else:
    print("sorry! incorrect")

answer = input("2. what is the stand of RAM? ")
if answer.lower() == "random access memory":
    print("correct")
    score += 1
else:
    print("sorry! incorrect")


answer = input("3 what is the stand of GPU? ")
if answer.lower() == "graphics processing unit":
    print("correct")
    score += 1
else:
    print("sorry! incorrect")

print("You got" +  str(score) + "questions correct")
print ("Your score is" + str((score/3) * 100) + "%" )
print("You got " + str((score / 3) * 100) + "%.")
print ("THANK YOU")