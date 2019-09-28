from models.TtsInstance import TtsInstance
from enums.RhythemPatternEnums import RhythemPatternEnums
from enums.NoteTimeEnums import NoteTimeEnums

class RhythemPatternMapper:
    def ToQuarterNoteTtsInstance(self, groupOfFourSylabs):
        totalTime = 0
        ttsInstances = []
        patternList = RhythemPatternEnums.MEASURE_OF_QUARTERS.value
        for i in range(len(groupOfFourSylabs)):
            delayObj = patternList[i]
            totalTime += delayObj.delay
            ttsInstances.append(TtsInstance(groupOfFourSylabs[i], delayObj.delay))
        if (totalTime < NoteTimeEnums.MEASURE_LENGTH.value):
            timeLeft = NoteTimeEnums.MEASURE_LENGTH.value - totalTime
            ttsInstances.append(TtsInstance("", timeLeft))
        return ttsInstances