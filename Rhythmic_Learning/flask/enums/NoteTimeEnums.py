from enum import Enum

class Delay():
    def __init__(self, delay, shouldPlay):
        self.delay = delay
        self.shouldPlay = shouldPlay

class NoteTimeEnums(Enum):
    MEASURE_LENGTH = 2

    #notes
    QUARTER_NOTE = Delay(.5, True)
    HALF_NOTE = Delay(1, True)
    SIXTEENTH_NOTE = Delay(.25, True)
    QUARTER_NOTE_TRIPLET = Delay(.75, True)
    ZERO_NOTE = Delay(0, True)

    #rests
    QUARTER_NOTE_REST = Delay(.5, False)
    HALF_NOTE_REST = Delay(1, False)
    SIXTEENTH_NOTE_REST = Delay(.25, False)
    QUARTER_NOTE_TRIPLET_REST = Delay(.75, False)