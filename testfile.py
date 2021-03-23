print("The quiz is comprised of ten questions including multiple choice.")
print("The questions print one at a time")
print("This is a standard IQ quiz. Please start answering to begin.")
print("Enter the letter beside your chosen answer when answering multiple choice Questions for example a or b(in small caps)")
print("For mathematical questions with no multiple choice just type the answer. It is normally always a number")
from projectfunctions import*
import turtle
jojo = turtle.Turtle()
def main():
    sPercentage=0
    qnum=-1
    for question, choices, correct_choice, answer in zip(questions, answer_choices, correct_choices, answers):
        qnum+=1
        print(question)
        user_answer = input(choices).lower()
        
        scorePercentage=IQquiz(qnum,user_answer)
        correct=user_answer in correct_choice
        if len(user_answer)> 9:
            print("Enter valid answers")
        sPercentage+= scorePercentage
        if correct:
            print("Correct", sPercentage)
        else:
            print("Incorrect",answer,sPercentage)
    print("Game over. Your score is",str(sPercentage)+"%")
    if sPercentage >= 0.0 and sPercentage <= 45.0:
        jojo.forward(50)
        jojo.backward(50)
        jojo.left(90)
        jojo.forward(50)
        jojo.backward(50)
        jojo.right(90)
        jojo.forward(10)
        jojo.color("red")
        jojo.left(45)
        jojo.forward(50)
        print("You failed.")
    else:
        jojo.forward(50)
        jojo.backward(50)
        jojo.left(90)
        jojo.forward(50)
        jojo.backward(50)
        jojo.right(90)
        jojo.forward(10)
        jojo.color("green")
        jojo.left(45)
        jojo.forward(50)
        print("You passed")
main()
