from src.tm.tm import TuringMachine, BLANK_SYMBOL, RIGHT, LEFT
from src.tm.checker import check

tm = TuringMachine(
    ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'qa', 'qr'],
    ['a', 'b'],
    ['a', 'b', BLANK_SYMBOL],
    {
        'q0': {
            'a': ['q1', BLANK_SYMBOL, RIGHT],
            'b': ['q4', BLANK_SYMBOL, RIGHT],
            BLANK_SYMBOL: ['qa', BLANK_SYMBOL, RIGHT]
        },

        ## a branch
        'q1': {
            'a': ['q1', 'a', RIGHT],
            'b': ['q1', 'b', RIGHT],
            BLANK_SYMBOL: ['q2', BLANK_SYMBOL, LEFT]
        },
        'q2': {
            'a': ['q3', BLANK_SYMBOL, LEFT]
        },
        'q3': {
            'a': ['q3', 'a', LEFT],
            'b': ['q3', 'b', LEFT],
            BLANK_SYMBOL: ['q0', BLANK_SYMBOL, RIGHT]
        },

        ## b branch
        'q4': {
            'a': ['q4', 'a', RIGHT],
            'b': ['q4', 'b', RIGHT],
            BLANK_SYMBOL: ['q5', BLANK_SYMBOL, LEFT]
        },
        'q5': {
            'b': ['q6', BLANK_SYMBOL, LEFT]
        },
        'q6': {
            'a': ['q6', 'a', LEFT],
            'b': ['q6', 'b', LEFT],
            BLANK_SYMBOL: ['q0', BLANK_SYMBOL, RIGHT]
        }
    },
    'q0',
    'qa',
    'qr'
)

check(tm, length = 3)