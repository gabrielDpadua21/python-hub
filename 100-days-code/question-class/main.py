from data import questions_mock
from model import Question
from quizz_brain import QuizzBrain
import requests

def question_bank_mock() -> list:
    questions = []
    for data in questions_mock:
        questions.append(Question(text=data["text"], answer=data["answer"]))
    return questions


def question_bank_request() -> list:
    questions = []
    response = requests.get('https://opentdb.com/api.php?amount=5&category=15&difficulty=hard&type=boolean')
    questions_data = response.json()
    for question in questions_data["results"]:
        questions.append(Question(text=question["question"], answer=question["correct_answer"]))
    return questions
    

if __name__ == "__main__":
    print("Quizz Class Game")
    quizz = QuizzBrain(question_bank_request())
    print("Lets Start the game!")
    quizz.next_question()
