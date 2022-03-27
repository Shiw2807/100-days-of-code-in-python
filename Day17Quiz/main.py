from question_model import question
from data import original_question_data
from quiz_brain import QuizBrain

question_bank=[]
for i in original_question_data:
    question_text=i["text"]
    question_answer=i["answer"]
    new_question=question(question_text,question_answer)
    question_bank.append(new_question)

quiz=QuizBrain(question_bank)
quiz.next_question()

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the game")
print(f"Your final score is: {quiz.score}/{quiz.question_number}.")