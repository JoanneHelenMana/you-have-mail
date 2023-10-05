class Letter:
    """ This class creates a letter."""
    def __init__(self, content=None, encrypted=False, read=False, dropped=False, picked_up=False, addressed_to=None):
        self.content = content
        self.encrypted = encrypted
        self.read = read
        self.dropped = dropped
        self.picked_up = picked_up
        self.addressed_to = addressed_to

    def __str__(self):
        return f'{self.content}'

    def return_addressee(self):
        '''Returns addressee as a Person object.'''
        return self.addressed_to

    def decrypt(self):
        '''Letter's encryption status is set as decrypted (False).'''
        self.encrypted = False
        return False

    def has_been_read(self):
        '''Letter's read status is set as read (True).'''
        self.read = True
        return True

    def get_encryption_status(self):
        '''Returns the letter's encryption status.'''
        return self.encrypted
