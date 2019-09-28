from enums.RhythemPatternEnums import RhythemPatternEnums
from enums.NoteTimeEnums import NoteTimeEnums

class RhythemPatternFactory():
    def __init__(self):
        pass
    
    def test(self):
        results = []
        for x in range(10):
            results.append(.5)
            results.append(.5)
            results.append(.5)
            results.append(.5)
            results.append(.75)
            results.append(.75)
            results.append(.25)
        return results