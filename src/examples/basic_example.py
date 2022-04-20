from src.tm.tm import TuringMachine, BLANK_SYMBOL, RIGHT
from src.tm.checker import check

tm = TuringMachine(
    ['q0', 'qa', 'qr'],
    ['a', 'b'],
    ['a', 'b', BLANK_SYMBOL],
    {
        'q0': {
            'a': ['qa', 'a', RIGHT],
            'b': ['qa', 'b', RIGHT]
        }
    },
    'q0',
    'qa',
    'qr'
)

check(tm, length = 4)