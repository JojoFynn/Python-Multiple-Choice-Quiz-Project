# Python-Multiple-Choice-Quiz-Project
This code was created by me in my first year using Python Programming. Its a multiple choice quiz application. Turtle graphics was implemented into the application.
The project functions file contains all the questions needed for the quiz application and the test file is where all print statements can be found. It is also a place where the file is actually run from.
INTRODUCTION OF PROJECT TOPIC:
My project is an Intelligence Quotient (IQ) quiz that tests the thinking ability of a user. It takes 
in the input from the user, that is, the user’s answer and compares it with the correct and in the 
program. If it is correct, the user gets 10 points. Aa t the end of the game, the user sees his/her 
total score, and turtle graphics draws a diagram interpreting the user’s performance. If the 
arrow’s colour is green in the turtle graphics, it means the user had a good score probably above 
50%. If the user had a bad score, then the colour of the turtle will be red. There are different 
types of IQ quizzes. I picked my questions from different Standardized IQ quizzes.
Application of Knowledge:
There are two files in my project the function file and invocator file. In the functions file, the 
questions, answers, answer_choices and correct choices were stored inside a list. This concept 
is found in chapter four of Python programming in context. In the same functions file, a 
function definition was written passing two parameters in it, that is the question number and 
answer. Also, the score of the user used the idea of accumulator pattern, that is, every time the 
user answers a question the score adds up. The concept of a function definition is found in 
chapter one of python programming in context. Also, the idea of the accumulator pattern is 
found in chapter two of the same book. Also, after the function definition an if statement was 
used, in that if the user's answer is correct, he or she receives a point. The if statement is found
in chapter 2.6 of the book. Also, a function was written in the same file to convert the score 
into a percentage, and the return command was used to return its value. In the lists all the data 
was stored as a string, a concept found in chapter 4 of python programming in context.
In the invocator file, several print statements were used to tell the user a message before starting 
the quiz. After those print statements, I imported the function file into the file. A for loop was 
used to read the content of the lists in the function file and compare the answers with the 
answers the user gives. The for loop made use of zip, a function that iterates over these lists at 
the same time and does the actual game. The concept of for loop is found in chapter 1.5 of the 
Python book. Also, in this file, an input statement was created for the user’s answer, e.g. input(). 
In the for loop if the user gets an answer right, a statement prints out “Correct” and print out a 
score of 10. It is in this file where the percentage function is called and used from the functions 
file. Another accumulator was used to add up the score in the percentage function in this file. 
Also, if the user gets an answer wrong a statement print out as “Incorrect”, the correct answer 
is printed out, and the user receives no point. IQ quizzes don’t normally give you answers after 
the you take them, but I designed mine to do so. Also, I created an if statement such that if the 
user enters an answer more than 9 characters a statement should that the user should enter a 
valid answer. This is because the user might enter his or her name accidentally when answering 
or maybe something else. After the user is done with the game a statement prints out as ‘Game 
Over’ and the total score is printed out to the user. The statement which is printed out to the 
user is in string form. After the user has completed the game, depending on the score, the turtle
will draw a graph with a diagonal line in the middle of it. An if statement was written, in that 
if the user had a score below 45% turtle draws a graph and the colour of the diagonal line will 
be red, or the else statement will take hold that is the line will turn green if the user had a score 
above 45%. The concept of turtle can be found in chapter one of python programming in 
context
