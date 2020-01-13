class Hangman:
    def __init__(self, word):
        if word.__contains__('_'):
            print("Invalid character in word")
        else:
            self.word = word.lower()
            self.MAX_GUESSES = 6
            self.lettersTried = []
            self.incorrectGuesses = 0
            self.LOSE = "LOSER - HAHHAHAHA"
            self.WIN = "WINNER"

    def getWord(self):
        mask = ""
        for char in self.word:
            if char in self.lettersTried:
                mask += char + " "
            else:
                mask += "_ "
        return "\nWord: " + mask + "\n"
    def changeWord(self, word):
        if word.__contains__('_'):
            print("Invalid character in word")
        else:
            self.word = word
    def guess(self, letter):
        if self.incorrectGuesses < self.MAX_GUESSES:
            letter = letter.lower()
            if letter in self.lettersTried:
                return "The letter " + letter +  " has already been tried. Try another letter"
            else:
                prior = self.getWord()
                self.lettersTried += letter
                if prior == self.getWord():
                    self.incorrectGuesses += 1
                    return self.drawHangman()
            return self.getWord()
        else:
            return self.LOSE

    def displayLettersTried(self):
        print("Letters Tried: \n" + ', '.join(self.lettersTried))
    def drawHangman(self):
        lines = "\n"+ "="*20 + "\n"
        firstGuess = '''
        ____|____     
        '''
        secondGuess = '''
            |
            |
            |
            |
            |
            |
        ____|____        
        '''
        thirdGuess = '''
             __________
            |/        |
            |
            |
            |
            |
            |
            |
        ____|____
        '''
        fourthGuess = '''
             __________
            |/        |
            |         0
            |        |||
            |
            |
            |
            |
        ____|____
        '''
        fifthGuess = '''
            ___________
            |/        |
            |         0
            |        |||
            |        | |
            |
            |
            |
        ____|____
        '''
        sixthGuess = self.LOSE
        if self.incorrectGuesses == 1:
            return lines + firstGuess + lines + self.getWord()
        if self.incorrectGuesses == 2:
            return lines + secondGuess + lines + self.getWord()
        if self.incorrectGuesses == 3:
            return lines + thirdGuess + lines + self.getWord()
        if self.incorrectGuesses == 4:
            return lines + fourthGuess + lines + self.getWord()
        if self.incorrectGuesses == 5:
            return lines + fifthGuess + lines + self.getWord()
        if self.incorrectGuesses == 6:
            return lines + sixthGuess + lines + self.getWord()