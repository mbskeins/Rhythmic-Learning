import syllables

class Word():
    def __init__(self, word):
        self.word = word
        self.sylabCount = syllables.estimate(word)