from letter_state import Letter_state

class Wordle:

    MAX_ATTEMPTS = 6
    WORD_LENGTH = 6

    def __init__(self, secret: str):
        self.secret: str = secret.upper()
        self.attempts = []
        self.att =[]
        pass


    def attempt(self, word:str):
        word = word.upper()
        self.att.append(word)
    def guess(self, word:str):
        word= word.upper()
        result =[]

        def prGreen(col):  # print green
            result.append("\033[92m {}\033[00m".format(col))
        def prYellow(col):  # print yellow
            result.append("\033[93m {}\033[00m".format(col))



        for i in range(self.WORD_LENGTH):
            character = word[i]
            letter = Letter_state(word[i])
            letter.in_the_word = character in self.secret
            letter.in_the_position = character == self.secret[i]
            if letter.in_the_position:
                letter = prGreen(letter)
            elif letter.in_the_word:
                letter = prYellow(letter)
            else:
                result.append(f' {letter}')
        self.attempts.append(result)

        for attempt in self.attempts:
            print(*attempt)
        #print(self.att)


    def brd(self, word:str):
        for i in range(self.remaining_attempts):
            print("_" * Wordle.WORD_LENGTH)
    @property
    def is_solved(self):
        return len(self.att) > 0 and self.att[-1] == self.secret

    @property
    def remaining_attempts(self) -> int:
        return self.MAX_ATTEMPTS - len(self.attempts)
    @property
    def can_atttempt(self):
        return self.remaining_attempts > 0 and not self.is_solved