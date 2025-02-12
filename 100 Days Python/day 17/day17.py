from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:

    statement = question ["text"]
    answer = question ["answer"]
    new_question = Question(statement, answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"Thanks for completing that!\nYour final score is: {quiz.score}/{quiz.question_number}")