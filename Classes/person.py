from Classes.letter import Letter
from Classes.letterbox import Letterbox
from Classes.post_office import PostOffice

class Person:
    '''The person has a letterbox, and can write, receive, send, read, encrypt and decrypt letters.'''
    def __init__(self, name, letterbox=Letterbox, letter=Letter, letter_received=Letter):
        letterbox = Letterbox()

        self.name = name
        self.letterbox = letterbox
        self.letter = letter
        self.letter_received = letter_received

    def __str__(self):
        return f'{self.name}'


    def write_letter(self, content, addressee):
        '''The person writes a letter with a defined content and addressee.'''
        self.letter = Letter()
        self.letter.content = content
        self.letter.addressed_to = addressee
        return f"{self.letter.content}"

    def encrypt_letter(self):
        '''The person encrypts the letter.'''
        if self.letter != None:
            self.letter.encrypted = True
            return "Letter has been encrypted."

    def drop_letter(self, post_office=PostOffice):
        '''The person drops the letter at the post office.'''
        if self.letter.encrypted is True:
            self.letter.dropped = True
            post_office.letter = self.letter
            return "Sender has dropped a letter in the Post Office."

    def pick_up_letter(self):
        '''The person picks up a letter from their letterbox.'''
        if self.letterbox.letter is not None:
            self.letter_received = self.letterbox.letter
            self.letterbox.letter = None
            self.letterbox.flag_down()
            return "Receiver has picked up a letter from their letterbox."

    def decrypt_letter(self):
        '''The person decrypts a received letter.'''
        if self.letter_received is not None:
            self.letter_received.decrypt()
            return "Letter has been decrypted."

    def read_letter(self):
        '''The person reads a received letter.'''
        if self.letter_received is not None and self.letter_received.get_encryption_status() is not True:
            self.letter_received.has_been_read()
            return f'Receiver has read this letter: "{self.letter_received}"'
