"""This module contains the QuizBrain class."""

class Quizbrian:
    """This class is responsible for keeping track of the quiz and the score."""
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
        """This method will return True if there are still questions left in the quiz."""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """This method will get the next question from the list of questions."""
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        """This method will check the user's answer against the correct answer."""
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
