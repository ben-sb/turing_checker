BLANK_SYMBOL = ''
LEFT = 'L'
RIGHT = 'R'

class TuringMachine():
    def __init__(self, states, input_alphabet, tape_alphabet, transitions, start_state, accept_state, reject_state):
        self.states = states
        self.input_alphabet = input_alphabet
        self.tape_alphabet = tape_alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.accept_state = accept_state
        self.reject_state = reject_state
        self.tape = {}
        self.position = 0

    def generate_tape(self, input):
        tape = {}

        for i in range(0, len(input)):
            tape[i] = input[i]

        return tape

    def get_symbol(self):
        if self.position not in self.tape:
            return BLANK_SYMBOL
        else:
            return self.tape[self.position]

    def write_symbol(self, symbol):
        self.tape[self.position] = symbol

    def move(self, direction):
        self.position += 1 if direction == RIGHT else -1

    def run(self, input):
        self.tape = self.generate_tape(input)
        self.position = 0
        self.state = self.start_state

        while self.state != self.accept_state and self.state != self.reject_state:
            symbol = self.get_symbol()

            if self.state not in self.transitions:
                raise ValueError(f'Transitions missing for state {self.state}')
            transitions = self.transitions[self.state]

            ## don't reject unknown symbols (for simplicity)
            #if symbol not in transitions:
                #raise ValueError(f'Symbol {symbol} missing for state {self.state}')

            ## treat unknown symbols as rejection instead
            if symbol not in transitions:
                self.state = self.reject_state
                break

            next_state, new_symbol, direction = transitions[symbol]
            self.state = next_state
            self.write_symbol(new_symbol)
            self.move(direction)

        return self.state == self.accept_state
