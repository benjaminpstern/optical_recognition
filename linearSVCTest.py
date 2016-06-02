from character_repr import Char_Repr
from picture import Picture
from sklearn.svm import LinearSVC
import numpy as np

def main():
    X = []
    y = []
    for num in range(1, 3):
        p = Picture("training_data/a" + str(num)+".png")
        c = Char_Repr(p)
        X.append(c.points)

    for num in range(1, 3):
        p = Picture("training_data/b" + str(num)+".png")
        c = Char_Repr(p)
        X.append(c.points)

    X = np.array(X)
    y.extend(["a"] * 2)
    y.extend(["b"] * 2)
    y = np.array(y)
    s = LinearSVC()
    s.fit(X, y)

    p = Picture("training_data/a7.png")
    c = Char_Repr(p)
    print(s.predict([c.points]))
    p = Picture("training_data/b3.png")
    c = Char_Repr(p)
    print(s.predict([c.points]))
    c.pic.display()
    raw_input()

main()
