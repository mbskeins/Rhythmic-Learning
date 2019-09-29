from enum import Enum

class Delay():
    def __init__(self, delay, shouldPlay):
        self.value = delay
        self.shouldPlay = shouldPlay

class NoteTimeEnums(Enum):
    #notes
    MEASURE_LENGTH = Delay(2, True)
    QUARTER_NOTE = Delay(.5, True)
    HALF_NOTE = Delay(1, True)
    SIXTEENTH_NOTE = Delay(.25, True)
    QUARTER_NOTE_TRIPLET = Delay(.75, True)
    ZERO_NOTE = Delay(0, True)

    #rests
    MEASURE_LENGTH_REST = Delay(2, False)
    QUARTER_NOTE_REST = Delay(.5, False)
    HALF_NOTE_REST = Delay(1, False)
    SIXTEENTH_NOTE_REST = Delay(.25, False)
    QUARTER_NOTE_TRIPLET_REST = Delay(.75, False)