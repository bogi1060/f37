import random
import numpy as np

def sziget(x):
    b = np.full((100, 100), "~")
    k = []
    t = []
    a = random.randrange(2, 97, 4)
    c = random.randrange(2, 97, 4)

    for i in range(x):

        while a in k:
            a = random.randrange(2, 97, 4)

        k.append(a)
        while c in t:
            c = random.randrange(2, 97, 4)
        t.append(c)

        print(k)
        print(t)
        b[a][c] = "O"
        b[a - 1][c - 1] = "O"
        b[a][c - 1] = "O"
        b[a - 1][c] = "O"
        b[a + 1][c] = "O"
        b[a + 1][c - 1] = "O"
        b[a + 1][c + 1] = "O"
        b[a][c + 1] = "O"
        b[a - 1][c + 1] = "O"

    print(b)


try:

    sziget(8)

except TypeError:
    print("Nem megfelelő input.")

np.set_printoptions(threshold=np.inf)