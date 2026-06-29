class QuizBrain:
    
    def __init__(self, q_list):
        import random
        self.total_ques = 0
        self.question_list = q_list
        self.question_num = random.randrange(0, len(self.question_list)-9)
        self.score = 0

    def still_go(self):
        return self.total_ques < 10

    def next_question(self):
        current = self.question_list[self.question_num]
        self.question_num +=1
        self.total_ques +=1
        ans = input(f"Q.{self.total_ques} {current.text} (True/False): ")
        self.check_ans(ans, current.answer)

    def check_ans(self, ans, correct_answer):
        if ans.lower() == correct_answer.lower():
            print("You are right!")
            self.score += 1
            print(f"Your score is: {self.score}/{self.total_ques} \n")
        else:
            print("You are wrong!")
            print(f"The right answer was: {correct_answer}")
            print(f"Your score is: {self.score}/{self.total_ques} \n")
        



    
