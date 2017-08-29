import datetime
import random

from questions import Add, Multiply

class Quiz:
    questions = []
    answers = []
    numberOfQuestions = None

    def __init__(self, **kwargs):
        self.numberOfQuestions = kwargs.get('numberOfQuestions', 10)
        questionTypes = (Add, Multiply)
        # generate 10 random questions with number from 1 to 10
        for _ in range(self.numberOfQuestions):
            a = random.randint(1,10)
            b = random.randint(1,10)
            question = random.choice(questionTypes)(a,b)
            self.questions.append(question)

    def takeQuiz(self):
        self.startTime = datetime.datetime.now()
        for question in self.questions:
            self.answers.append(self.ask(question))
        else:
            self.endTime = datetime.datetime.now()
        return self.summary()

    def ask(self, question):
        correct = False
        questionStart = datetime.datetime.now()
        answer = input(question.text + ' = ')
        if answer == str(question.answer):
            correct = True
        questionEnd = datetime.datetime.now()

        return correct, questionEnd - questionStart

    def totalCorrect(self):
        total = 0
        for answer in self.answers:
            if answer[0]:
                total += 1
        return total

    def summary(self):
        print("You got {} our of {} right".format(self.totalCorrect(), len(self.questions)))
        print("It took you {} seconds total.".format((self.endTime-self.startTime).seconds))

Quiz().takeQuiz()
