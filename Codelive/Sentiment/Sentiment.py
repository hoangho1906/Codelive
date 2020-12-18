
class HighScoringWords:
    CHART_LENGTH = 100
    MIN_WORD_LENGTH = 3
    letter_values = {}

        def __init__(self, validwords='wordlist.txt', lettervalues='letterValues.txt'):

        self.leaderboard = []
        self.word_scores = {}
        with open(validwords) as file:
            self.valid_words = file.read().splitlines()

        with open(lettervalues) as file:
            for line in file:
                key, val = line.split(':')
                self.letter_values[str(key).strip().lower()] = int(val)



