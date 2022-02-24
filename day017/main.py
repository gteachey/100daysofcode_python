from random import choice
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


def play_quiz():
    question_bank = []

    for question in question_data:
        new_question = Question(question['question'], question['correct_answer'])
        question_bank.append(new_question)

    quiz_brainner = QuizBrain(question_bank)

    while quiz_brainner.still_has_questions():
        quiz_brainner.next_question()

    quiz_brainner.end_quiz()


#  question = choice(data)
#  quest_model = question_model.QuestionModel(question['text'], question['answer'])
#  print(quest_model.text, quest_model.answer)


play_quiz()
