class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def still_has_questions(self):
        return not self.question_list == []

    def next_question(self):
        question = self.question_list.pop()
        self.question_number += 1
        answer = input(
            f"Q.{self.question_number}: {question.text} ?: ")
        self.check_answer(answer, question.answer)

    def check_answer(self, answer, correct_answer):
        if answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")

        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}\n")

    def final_score(self):
        return f"Your final score was: {self.score}/{self.question_number}"
