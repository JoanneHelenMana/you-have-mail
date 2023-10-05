from Classes.post_office import PostOffice
from Classes.letter import Letter
from Classes.person import Person
from Classes.letterbox import Letterbox

class Postie(Person, Letterbox, PostOffice, Letter):
    '''The Postie checks whether there is mail at the Post Office and delivers that mail to the appropriate addressee.'''
    def __init__(self, letter_to_deliver=Letter):
        self.letter_to_deliver = letter_to_deliver

    def check_mail(self, post_office=PostOffice):
        '''The Postie checks whether there's mail at the post office to be delivered.'''
        if post_office.is_there_mail() is True:
            self.letter_to_deliver = post_office.letter
            print("There's mail at the post office.")
            return True
        else:
            print("There's no mail at the post office.")
            return False

    def get_addressee(self):
        '''The Postie gets the addressee who to deliver the letter.'''
        addressee = self.letter_to_deliver.return_addressee()
        print(f'Mail addressed to {addressee}.')
        return addressee

    def deliver_letter(self, addressee=Person):
        '''The Postie delivers the letter to the addressee's letterbox.'''
        addressee.letterbox.letter = self.letter_to_deliver
        addressee.letterbox.flag_up()
        print(f"A letter has been delivered to {addressee} by Postie.")
