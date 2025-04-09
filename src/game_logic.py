import json

class QuizGame:
    def __init__(self, questions_file):
        with open(questions_file) as f:
            self.questions = json.load(f)
        self.current_question_index = 0
        self.score = 0

    def next_question(self):
        self.current_question_index += 1

    def check_answer(self, selected_answer):
        correct_answer = self.questions[self.current_question_index]['correct_answer']
        if selected_answer == correct_answer:
            self.score += 1

    def get_current_question(self):
        return self.questions[self.current_question_index]

    def is_game_over(self):
        return self.current_question_index >= len(self.questions)
