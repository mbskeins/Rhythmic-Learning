from enum import Enum
from .NoteTimeEnums import NoteTimeEnums

class RhythemPatternEnums(Enum):
    MEASURE_OF_QUARTERS = [NoteTimeEnums.QUARTER_NOTE.value, NoteTimeEnums.QUARTER_NOTE.value, NoteTimeEnums.QUARTER_NOTE.value, NoteTimeEnums.QUARTER_NOTE.value]
    MEASURE_OF_TRIPLETS = [NoteTimeEnums.SIXTEENTH_NOTE.value, NoteTimeEnums.QUARTER_NOTE.value, NoteTimeEnums.QUARTER_NOTE.value]
    STEADY_HALF_NOTE = [NoteTimeEnums.HALF_NOTE.value, NoteTimeEnums.HALF_NOTE.value]