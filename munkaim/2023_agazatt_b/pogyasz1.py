import Pogyasz


def fel3():
    index = 0
    db = 0
    kiFajl = open("csomag.txt", "r", encoding="utf-8")
    kiFajl.readline()
    adatok = kiFajl.readlines()
    print("III/A,B:")
    while index < len(adatok):
        db += 1
        index += 1
    print("\tA pogyászok száma:{}".format(db))
    print("III/C:")
    print("Az 51 cm-es pogyászok átlag súlyértéke:{}")


def suly(Pogyasz):
    index = 0


