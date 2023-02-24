"""This is the main file of the quiz game. 
It will be responsible for calling the classes and running the game.
"""
from question_model import Question
from data import question_data
from quiz_brain import Quizbrian

question_bank = []

for question in question_data:
    text = question["text"]
    answer = question["answer"]
    new_question = Question(text, answer)
    question_bank.append(new_question)

quiz = Quizbrian(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
