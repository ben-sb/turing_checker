from src.tm.tm import TuringMachine, BLANK_SYMBOL, RIGHT, LEFT
from src.tm.checker import check

tm = TuringMachine(
    ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'qa', 'qr'],
    ['a', 'b'],
    ['a', 'b', 'a*', 'X', 'Y', BLANK_SYMBOL],
    {
        'q0': {
            'a': ['q1', 'a*', RIGHT]
        },
        'q1': {
            'a': ['q1', 'a', RIGHT],
            'b': ['q2', 'b', RIGHT]
        },
        'q2': {
            'b': ['q2', 'b', RIGHT],
            BLANK_SYMBOL: ['q3', BLANK_SYMBOL, LEFT]
        },
        'q3': {
            'a': ['q3', 'a', LEFT],
            'b': ['q3', 'b', LEFT],
            'a*': ['q4', 'X', RIGHT]
        },
        'q4': {
            'a': ['q4', 'a', RIGHT],
            'Y': ['q4', 'Y', RIGHT],
            'b': ['q5', 'Y', RIGHT]
        },
        'q5': {
            'b': ['q6', 'Y', LEFT]
        },
        'q6': {
            'a': ['q6', 'a', LEFT],
            'Y': ['q6', 'Y', LEFT],
            'X': ['q7', 'X', RIGHT]
        },
        'q7': {
            'X': ['q7', 'X', RIGHT],
            'Y': ['q7', 'Y', RIGHT],
            'a': ['q4', 'X', RIGHT],
            BLANK_SYMBOL: ['qa', BLANK_SYMBOL, LEFT]
        }
    },
    'q0',
    'qa',
    'qr'
)

check(tm, length = 12)

# L = { a^n b^(2n): n >= 1 }