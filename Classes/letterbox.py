from Classes.letter import Letter

class Letterbox:
    """This is a letterbox."""
    def __init__(self, letter=Letter, flag='down'):
        self.letter = letter
        self.flag = flag

    def flag_up(self):
        '''Sets the letterbox's flag up, indicating there's mail.'''
        self.flag = 'up'

    def flag_down(self):
        '''Sets the letterbox's flag down, indicating there's no mail.'''
        self.flag = 'down'
