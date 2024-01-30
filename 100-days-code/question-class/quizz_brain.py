class QuizzBrain:

    number: int
    question_list: list
    score: int

    def __init__(self, question_list) -> None:
        self.number = 0
        self.question_list = question_list
        self.score = 0


    def next_question(self) -> None:
        if self.number < len(self.question_list):
            current_question = self.question_list[self.number]
            self.number += 1
            user_answer = input(f'Q.{self.number} {current_question.text} ? True/False : ')
            self.check_answer(user_answer, current_question.answer)
            self.next_question()
        else:
            print("You've reached the end of the quiz") 
            self.final_score()
            

    
    def check_answer(self, user_answer, question_answer) -> None:
        if user_answer == question_answer:
            self.score += 1

    
    def final_score(self) -> None:
        print(f'Your final score is: {self.score}/{len(self.question_list)}')
        