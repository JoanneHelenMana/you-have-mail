from Classes.letter import Letter
from Classes.letterbox import Letterbox


class Person:
    def __init__(self, letterbox=None, letter=None):
        letterbox = Letterbox()
        self.letterbox = letterbox
        self.letter = letter

    def write_letter(self, content, addressee):
        self.letter = Letter()
        self.letter.content = content
        self.letter.encrypted = true
        self.letter.addressed_to = addressee
        return f"{self.letter.content}"

    def drop_letter(self, letter, letterbox):
        if letterbox.letter == None:
            letterbox.letter = letter
            letterbox.flag = 'up'
            self.letter.dropped = True
            return "Alice has dropped a letter."

    def pick_up_letter(self):
        if self.letterbox.letter != None:
            self.letterbox.flag = 'down'
            self.letterbox.letter == None
            return "Alice has picked up a letter."

    def read_letter(self):
        if self.letterbox.letter.read == False:
            self.letterbox.letter.read = True
            return f'Alice has read this letter: "{self.letterbox.letter.content}"'
