from data import question_data
from question import Question
from brain import QuizBrain

question_bank = []
for i in range(len(question_data)): #takes the "length" of the list
    question_bank.append(Question(question_data[i]["text"], question_data[i]["answer"]))
    # append adds the question to the end of the list,
    # Question class is calling 2 things from the bank and assigning it to "text" and "answer",
    # 1st one is bank name followed by the N th itme in the list (which is a dictionary) followed by key to find the value and assign that value to the list. 
    
quiz = QuizBrain(question_bank)

while quiz.still_go():
    quiz.next_question()

print("Congratulations! You have completed the quiz!")
print(f"Your final score is: {quiz.score}/{quiz.total_ques}")