from character_repr import Char_Repr
from picture import Picture

def main():
    for num in range(1,4):
        p = Picture("training_data/a" + str(num)+".png")
        c = Char_Repr(p)
        print(c.points)
        p.display()
        raw_input()
    for num in range(1,4):
        p = Picture("training_data/b" + str(num)+".png")
        c = Char_Repr(p)
        print(c.points)
        p.display()
        raw_input()
main()
