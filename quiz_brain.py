class QuizBrain:

    def __init__(self,question_list):
        self.question_number = 0
        self.question_list = question_list
        self.good_ans = 0

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        self.guess = input(f"Q.{self.question_number}: {self.current_question.text}. (True/False)? ")

    def still_has_question(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def check_answer(self):

        self.max_point = len(self.question_list)

        if self.guess == self.current_question.answer:
            self.good_ans += 1

        print(f"You have {self.good_ans}/{self.max_point} points")
