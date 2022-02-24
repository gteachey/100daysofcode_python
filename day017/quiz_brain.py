class QuizBrain:
    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0

    def next_question(self):
        question_text = self.questions_list[self.question_number].text
        user_input = input(f"Q.{self.question_number + 1}: {question_text}: ").lower()
        answer = self.questions_list[self.question_number].answer.lower()

        self.check_answer(user_input, answer)
        self.question_number += 1

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def check_answer(self, user_input, answer):
        if user_input == answer:
            print("You got it right!")
            self.score += 1
        else:
            print("Sorry, that's wrong!")
        print("The correct answer was: {}".format(answer.title()))
        print("Your current score is: {} of {} questions correct.\n".format(self.score, self.question_number + 1))

    def end_quiz(self):
        print("You've completed the quiz")
        print("Your final score was {}/{}.".format(self.score, len(self.questions_list)))
