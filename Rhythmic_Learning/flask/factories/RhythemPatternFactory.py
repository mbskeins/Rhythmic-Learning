class RhythemPatternFactory():
    def __init__(self):
        self.quarterNote = .5
        self.halfNote = 1
        self.quarterTripletNote = .75
    
    def test(self):
        results = []
        for x in range(10):
            results.append(self.quarterNote)
            results.append(self.quarterNote)
            results.append(self.quarterNote)
            results.append(self.quarterNote)
            results.append(self.quarterTripletNote)
            results.append(self.quarterTripletNote)
            results.append(self.quarterTripletNote)
            results.append(self.halfNote)
        return results