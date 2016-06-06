from character_repr import Char_Repr
from picture import Picture
from sklearn.svm import LinearSVC
import numpy as np

def main():
    X = []
    y = []
    for num in range(1, 4):
        p = Picture("training_data/marker/a" + str(num)+".jpg")
        c = Char_Repr(p)
        X.append(c.points)

    for num in range(1, 4):
        p = Picture("training_data/marker/b" + str(num)+".jpg")
        c = Char_Repr(p)
        X.append(c.points)

    X = np.array(X)
    y.extend(["a"] * 3)
    y.extend(["b"] * 3)
    y = np.array(y)
    s = LinearSVC()
    s.fit(X, y)

    p = Picture("training_data/marker/a4.jpg")
    c = Char_Repr(p)
    print(s.predict([c.points]))
    p = Picture("training_data/marker/b4.jpg")
    c = Char_Repr(p)
    print(s.predict([c.points]))

main()
