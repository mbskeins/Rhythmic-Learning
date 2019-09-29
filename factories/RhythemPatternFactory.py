from enums.RhythemPatternEnums import RhythemPatternEnums
from enums.NoteTimeEnums import NoteTimeEnums
from models.TtsInstance import TtsInstance
from models.Word import Word
import math

class RhythemPatternFactory():
    data = "Twinkle, twinkle, little star. How I wonder what you are. Up above the world so high."

    def __init__(self):
        pass
    
    def generate(self):
        return self.data

    def generateSentence(self, sentence):
        wordsInSentence = []
        for word in sentence:
            wordsInSentence.append(Word(word))
        return self.generateRhyme(wordsInSentence)

    def generateRhyme(self, wordsInSentence):
        ttsInstanceList = []
        prevDelay = 0
        prevSyllabCount = 0
        totalDelay = 0
        for i in range(len(wordsInSentence)):
            word = wordsInSentence[i]
            ttsInstanceList.append(TtsInstance(word.word, prevDelay))
            prevSyllabCount = word.syllabCount
            prevDelay = .5 if float(totalDelay).is_integer() else .75
            totalDelay += prevDelay
        if(totalDelay < self.round_up_to_even(totalDelay)):
            restTime = self.round_up_to_even(totalDelay) - totalDelay
            ttsInstanceList.append(TtsInstance("", restTime))
        return ttsInstanceList

    def round_up_to_even(self, num):
        return math.ceil(num / 2.) * 2


'''
            results.append(.5)
            results.append(.5)
            results.append(.5)
            results.append(.5)
            results.append(.75)
            results.append(.75)
            results.append(.25)
'''