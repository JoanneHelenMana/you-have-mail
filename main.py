from Classes.person import Person
from Classes.postie import Postie
from Classes.post_office import PostOffice

bob = Person("Bob")
alice = Person("Alice")
postie = Postie()
post_office = PostOffice()

def main():
    """Example interaction where Bob writes an encrypted letter to Alice, drops the letter at the post office,
    Postie picks it up and delivers to Alice's letterbox, when in turn she picks up, decrypts, and reads the letter."""


    print(f'Bob writes the letter: "{bob.write_letter("Hi Alice!", alice)}"')
    print(f'{bob.encrypt_letter()}')
    print(f'{bob.drop_letter(post_office)}')

    if postie.check_mail(post_office) is True:
        addressee = postie.get_addressee()
        postie.deliver_letter(addressee)

    if alice.letterbox.flag == 'up':
        print(alice.pick_up_letter())
        print(alice.decrypt_letter())
        print(alice.read_letter())


if __name__ == "__main__":
    main()
