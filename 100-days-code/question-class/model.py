class Question:

    text: str
    answer: str

    def __init__(self, text, answer) -> None:
        self.text = text
        self.answer = answer