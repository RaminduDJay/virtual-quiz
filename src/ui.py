import pygame

class QuizUI:
    def __init__(self, quiz):
        pygame.init()
        self.quiz = quiz
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Virtual Quiz Game")
        self.running = True

    def update(self, gesture, frame):
        self.screen.fill((0, 0, 0))
        question = self.quiz.get_current_question()
        # Display question and options
        self.display_text(question['question'], 50, 50)
        for i, option in enumerate(question['options']):
            self.display_text(option, 100, 150 + i * 50)

        # Handle gestures
        if gesture['type'] == 'point':
            x, y = gesture['position']
            # Detect option selection
            if 150 <= y <= 200:  # Adjust based on option positions
                self.quiz.select_option(0)

        pygame.display.flip()

    def display_text(self, text, x, y):
        font = pygame.font.Font(None, 36)
        text_surface = font.render(text, True, (255, 255, 255))
        self.screen.blit(text_surface, (x, y))

    def show_results(self):
        score = self.quiz.calculate_score()
        print(f"Your score: {score}")
        pygame.quit()
