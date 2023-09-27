from Classes.alice import Alice
from Classes.bob import Bob
from Classes.letterbox import Letterbox

bob = Person()
alice = Person()


def main():
    """Example interaction where Bob writes and delivers a letter to Alice,
    and Alice reads the letter and replies back to Bob, who in turn reads her letter."""

    print(f'Bob writes a letter: "{bob.write_letter("Hi Alice!")}"')
    if alice.letterbox.flag == 'down':
        print(bob.drop_letter(bob.letter, alice.letterbox))

    if alice.letterbox.flag == 'up':
        print(alice.pick_up_letter())
        print(alice.read_letter())
        print(f'Alice writes a letter: "{alice.write_letter("Hi Bob!")}"')

    if bob.letterbox.flag == 'down':
        print(alice.drop_letter(alice.letter, bob.letterbox))

    if bob.letterbox.flag == 'up':
        print(bob.pick_up_letter())
        print(bob.read_letter())

if __name__ == "__main__":
    main()
