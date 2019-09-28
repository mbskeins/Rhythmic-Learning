from enums.RhythemPatternEnums import RhythemPatternEnums
from enums.NoteTimeEnums import NoteTimeEnums
from models.TtsInstance import TtsInstance


class RhythemPatternFactory():
    data = [['mo-ney', 'is', 'any', 'item', 'or', 've-ri-fia-ble', 're-cord', 'that', 'is', 'ge-ner-al-ly', 'ac-cep-ted', 'as', 'pay-ment', 'for', 'goods', 'and', 'ser-vi-ces', 'and', 're-pay-ment', 'of', 'debts', 'such', 'as', 'taxes', 'in', 'a', 'par-ti-cu-lar', 'coun-try', 'or', 'so-ci-oeco-no-mic', 'con-text'], ['the', 'main', 'func-ti-ons', 'of', 'mo-ney', 'are', 'dis-tin-guis-hed', 'as', 'a', 'me-di-um', 'of', 'ex-chan-ge', 'a', 'unit', 'of', 'ac-count', 'a', 'sto-re', 'of', 'va-lue', 'and', 'so-me-ti-mes', 'a', 'standard', 'of', 'de-fer-red', 'pay-ment'], ['any', 'item', 'or', 've-ri-fia-ble', 're-cord', 'that', 'ful-fils', 'the-se', 'func-ti-ons', 'can', 'be', 'con-si-de-red', 'as', 'mo-ney'], ['mo-ney', 'is', 'his-to-ri-cally', 'an', 'emer-gent', 'mar-ket', 'phe-no-me-non', 'es-ta-blis-hing', 'a', 'com-mo-di-ty', 'mo-ney', 'but', 'ne-ar-ly', 'all', 'con-tem-po-ra-ry', 'mo-ney', 'sys-tems', 'are', 'ba-sed', 'on', 'fi-at', 'mo-ney']]
    def __init__(self):
        pass
    
    def generate(self):
        ttsInstanceList = []
        for sentence in self.data: 
            ttsInstanceList.append(self.generateSentence(sentence))
        return ttsInstanceList

    def generateSentence(self, sentence):
        sylableList = []
        for word in sentence:
            sylabs = word.split('-')
            for sylab in sylabs:
                sylableList.append(sylab)
        return sylableList
    
    def generateRhythemForSentence(self, sylabList):
        for i in range(len(sylabList)):

        
'''
            results.append(.5)
            results.append(.5)
            results.append(.5)
            results.append(.5)
            results.append(.75)
            results.append(.75)
            results.append(.25)
'''