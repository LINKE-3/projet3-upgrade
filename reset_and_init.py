from pickle import dump


def defineva():
    f = open("db.py", "wb")
    first = 0
    second = 0
    third = 0
    dump(first, f)
    dump(second, f)
    dump(third, f)
    f.close()


defineva()
