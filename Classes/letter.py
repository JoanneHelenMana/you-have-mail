class Letter:
    """ This is a letter."""
    def __init__(self, content=None, encrypted=False, read=False, dropped=False, addressed_to=None):
        self.content = content
        self.encrypted = encrypted
        self.read = read
        self.dropped = dropped
        self.addressed_to = addressed_to

    def __str__(self):
        return f'{self.content}'
