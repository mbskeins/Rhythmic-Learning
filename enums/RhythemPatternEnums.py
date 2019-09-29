from enum import Enum
from .NoteTimeEnums import NoteTimeEnums

class RhythemPatternEnums(Enum):
    MEASURE_OF_QUARTERS = [NoteTimeEnums.ZERO_NOTE.value, NoteTimeEnums.QUARTER_NOTE.value, NoteTimeEnums.QUARTER_NOTE.value, NoteTimeEnums.QUARTER_NOTE.value]
    MEASURE_OF_TRIPLETS = [NoteTimeEnums.SIXTEENTH_NOTE.value, NoteTimeEnums.QUARTER_NOTE.value, NoteTimeEnums.QUARTER_NOTE.value, NoteTimeEnums.SIXTEENTH_NOTE_REST.value]
    STEADY_HALF_NOTE = [NoteTimeEnums.ZERO_NOTE.value, NoteTimeEnums.HALF_NOTE.value]