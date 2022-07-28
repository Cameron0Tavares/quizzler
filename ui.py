from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20)
        self.score_label = Label(text='Score : ')
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg='white')

        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text='Questionable Text Choice',
            fill=THEME_COLOR,
            font=('Arial', 20, 'italic')
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        truth_image = PhotoImage(file='images/true.png')
        lies_image = PhotoImage(file='images/false.png')
        self.truth_button = Button(image=truth_image, highlightthickness=0, command=self.true_pressed)
        self.lies_button = Button(image=lies_image, highlightthickness=0, command=self.false_pressed)
        self.truth_button.grid(row=2, column=0)
        self.lies_button.grid(row=2, column=1)
        # self.truth_button.on

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f'Score :   {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text='You have reached the end of the quiz.')
            self.truth_button.config(state='disabled')
            self.lies_button.config(state='disabled')

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer('True'))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer('False'))

    def give_feedback(self, is_right):
        if is_right:
            print('right')
            self.canvas.config(bg='green')
        else:
            print('wrong')
            self.canvas.config(bg='red')

        self.window.after(1000, self.get_next_question)
