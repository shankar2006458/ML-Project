import tkinter as tk
from tkinter import messagebox
import random

QUESTIONS = [
    {
        "question": "What is the capital of France?",
        "choices": ["Berlin", "Madrid", "Paris", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "choices": ["Earth", "Mars", "Jupiter", "Venus"],
        "answer": "Mars"
    },
    {
        "question": "What is the largest mammal?",
        "choices": ["Elephant", "Blue Whale", "Giraffe", "Great White Shark"],
        "answer": "Blue Whale"
    },
    {
        "question": "How many continents are there on Earth?",
        "choices": ["5", "6", "7", "8"],
        "answer": "7"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "choices": ["Charles Dickens", "William Shakespeare", "Mark Twain", "Jane Austen"],
        "answer": "William Shakespeare"
    }
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.root.geometry("600x400")
        self.root.resizable(False, False)

        self.questions = random.sample(QUESTIONS, len(QUESTIONS))
        self.current_index = 0
        self.score = 0
        self.selected = False

        self.question_label = tk.Label(
            root, text="", font=("Arial", 16, "bold"), wraplength=500, justify="center"
        )
        self.question_label.pack(pady=20)

        self.buttons_frame = tk.Frame(root)
        self.buttons_frame.pack(pady=10)

        self.answer_buttons = []
        for i in range(4):
            btn = tk.Button(
                self.buttons_frame,
                text="",
                font=("Arial", 12),
                width=30,
                height=2,
                command=lambda idx=i: self.check_answer(idx)
            )
            btn.grid(row=i // 2, column=i % 2, padx=10, pady=5)
            self.answer_buttons.append(btn)

        self.feedback_label = tk.Label(root, text="", font=("Arial", 12))
        self.feedback_label.pack(pady=10)

        self.next_button = tk.Button(
            root, text="Next", font=("Arial", 12), state=tk.DISABLED, command=self.next_question
        )
        self.next_button.pack(pady=5)

        self.score_label = tk.Label(root, text="Score: 0", font=("Arial", 12, "bold"))
        self.score_label.pack(pady=5)

        self.load_question()

    def load_question(self):
        """Display the current question and its choices."""
        if self.current_index < len(self.questions):
            q = self.questions[self.current_index]
            self.question_label.config(text=f"Question {self.current_index + 1}: {q['question']}")

            for i, choice in enumerate(q["choices"]):
                self.answer_buttons[i].config(text=choice, bg="SystemButtonFace", state=tk.NORMAL)

            self.feedback_label.config(text="")
            self.next_button.config(state=tk.DISABLED)
            self.selected = False
        else:
            self.show_final_score()

    def check_answer(self, idx):
        """Handle answer selection, give feedback, and update score."""
        if self.selected:
            return

        q = self.questions[self.current_index]
        selected_choice = q["choices"][idx]
        correct_answer = q["answer"]

        for btn in self.answer_buttons:
            btn.config(state=tk.DISABLED)

        for i, choice in enumerate(q["choices"]):
            if choice == correct_answer:
                self.answer_buttons[i].config(bg="light green")
            elif i == idx:
                self.answer_buttons[i].config(bg="red")

        if selected_choice == correct_answer:
            self.feedback_label.config(text="Correct! ✅", fg="green")
            self.score += 1
        else:
            self.feedback_label.config(text=f"Wrong! The correct answer was: {correct_answer}", fg="red")

        self.score_label.config(text=f"Score: {self.score}")
        self.next_button.config(state=tk.NORMAL)
        self.selected = True

    def next_question(self):
        """Move to the next question or show final results."""
        self.current_index += 1
        self.load_question()

    def show_final_score(self):
        """Display final score and offer restart."""
        total = len(self.questions)
        percentage = (self.score / total) * 100

        for widget in self.root.winfo_children():
            widget.destroy()

        final_label = tk.Label(
            self.root,
            text=f"Quiz Completed!\n\nYour Score: {self.score}/{total}\nPercentage: {percentage:.1f}%",
            font=("Arial", 18, "bold"),
            justify="center"
        )
        final_label.pack(pady=40)

        if percentage == 100:
            msg = "Perfect score! You're a genius! 🎉"
        elif percentage >= 70:
            msg = "Great job! You know a lot! 👏"
        elif percentage >= 40:
            msg = "Not bad, but there's room for improvement. 👍"
        else:
            msg = "Keep learning and try again! 💪"

        feedback = tk.Label(self.root, text=msg, font=("Arial", 14))
        feedback.pack(pady=10)

        restart_btn = tk.Button(
            self.root,
            text="Play Again",
            font=("Arial", 14),
            command=self.restart_quiz
        )
        restart_btn.pack(pady=20)

    def restart_quiz(self):
        """Reset the quiz and start over."""
        self.questions = random.sample(QUESTIONS, len(QUESTIONS))
        self.current_index = 0
        self.score = 0
        self.selected = False

        for widget in self.root.winfo_children():
            widget.destroy()

        self.__init__(self.root)

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()