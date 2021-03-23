#Author Jojo Fynn Mensah
scorePercentage=0
questions = ["1. What is the missing number?\n 0,1,1,2,3,5,8,_,21,34",
             "2. Which identical three letter word, forms a new word, when placed in front of the following words?",
             "3. Choose the word that correctly completes the following sentence. Leave the rug ____ where it is",
             "4. Choose the word that correctly completes the following sentence. Have you ____ in the choir before? ",
             "5. Bruce likes 324 but not 325. He likes 2500 but not 2400. He like 121 but not 122. Which does he like?",
             "6. Counting from 1 to 100, how many 6s will you encounter?",
             "7. Choose best completes. Jimmy has been practicing his freethrows for months now. Despite his__efforts,Jimmy is still the worst free thrower on the team",
             "8. My successor's father is my father's son, and I do not have any brothers or sons. Who is my successor?",
             "9. Two people were walking in opposite directions. Both of them walked 6 miles forward then took right and walked 8 miles. How far is each from starting positions?",
             "10. When a number is multiplied by 13, it becomes greater to 105 by an amount with which it is lesser to 105 by now. What is the number?",]
answer_choices = ["a)10\nb)12\nc)13\nd)15\n:",
                  "FUSE,CLAIM,DUCT,CREATE,FIT,FOUND,LONG\n:",
                  "a.Laying b.Lying \nc.Lay \nd.Lie \nAnswer:",
                  "a.Sing \nb.Sung \nc.Sang \nd.Singed\n:",
                  "\na.900 \nb.800\n:",
                  "\na.10 \nb.11 \nc.18 \nd.19 \ne.20\n:",
                  "\na.Deplorable \nb.Coarse \nc.Hard-earned \nd.Valiant\n:",
                  "\na.Nephew \nb.niece \nc.Daughter \nd.Myself\n:",
                  "\na.14miles and 14 miles \nb.10miles and 10miles \nc.6 miles and 6 miles\n:",
                  "\na.15 \nb.18\n:"]
correct_choices = [["c","13"],
                   ["pro", "pro"],
                   ["b", "lying"],
                   ["c", "sang"],
                   ["a", "900"],
                   ["e", "20"],
                   ["d", "valiant"],
                   ["c", "daughter"],
                   ["b", "10miles and 10miles"],
                   ["a", "15"]]
answers = ["Correct answer is 13",
           "Correct answer is pro",
           "Correct answer is lying",
           "Correct answer is sang",
           "Correct answer is 900",
           "Correct answer is 20",
           "Correct answer is Valiant",
           "Correct answer is Daughter",
           "Correct answer is 10miles and 10miles",
           "Correct answer is 15"]
def IQquiz(qnum,answer):
    Score = 0
    if answer in correct_choices[qnum]:
        Score+=1
    scorePercentage = (Score / len(questions)) * 100
    
    return scorePercentage
        
        

