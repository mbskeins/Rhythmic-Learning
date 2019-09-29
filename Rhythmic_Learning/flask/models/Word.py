import syllables

class Word():
    def __init__(self, word):
        self.word = word
        self.syllabCount = syllables.estimate(word)