class PostOffice:
    '''This creates a post office.'''
    def __init__(self, letter=None):
        self.letter = letter

    def is_there_mail(self):
        '''Checks whether there's mail at the post office.'''
        if self.letter is None:
            return False
        elif self.letter is not None:
            return True
