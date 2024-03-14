class QuizBrain:
    def __init__(self,questions_list):
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True / False): ") 
        self.check_score(user_answer, current_question.answer)   

    def still_has_questions(self):
        if self.question_number == len(self.questions_list):
            return False
        else:
            return True    
        
    def check_score(self,user_answer,correct_answer):
            if user_answer.lower() == correct_answer.lower() :
                 print("Your answer is correct")
                 self.score += 1
            else:
                 print("Your answer is wrong") 
            print(f"The Right answer is {correct_answer}")   
            print(f"Your score is {self.score}/{self.question_number}") 
            print("\n")
