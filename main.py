from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

questionbank = []

for q in question_data:
    temp = Question(q["text"],q["answer"])
    questionbank.append(temp)

quiz = QuizBrain(questionbank)

while quiz.still_has_question():
    quiz.next_question()
    quiz.check_answer()


