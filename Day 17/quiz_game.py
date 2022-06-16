from html import unescape
from question_model import Question
from quiz_brain import QuizBrain
from data import question_data


def quiz():
    question_bank = [Question(unescape(x['question']), x['correct_answer'])
                     for x in question_data]
    quiz_brain = QuizBrain(question_bank)

    while quiz_brain.still_has_questions():
        quiz_brain.next_question()

    print("You have completed the quiz.")
    print(quiz_brain.final_score())


if __name__ == "__main__":
    quiz()
