class Letter:
    """ This is a letter."""
    def __init__(self, content=None, read=False, dropped=False):
        self.content = content
        self.read = read
        self.dropped = dropped

    def __str__(self):
        return f'{self.content}'
