import random
lista = []


def fel2():
    index = 0
    print("II/A,B,C")
    print("\t", end="")
    while index < 12:
        szam = random.randint(-10, 1000)
        lista.append(szam)
        if index == 11:
            print("{}".format(lista[index]), end="")
        else:
            print("{}$".format(lista[index]), end="")
        index += 1
    print("")
    konzol_kiir()
    fajlba_kiir()


def paratlanok_szama():
    index = 0
    db = 0
    while index < len(lista):
        if lista[index] % 2 == 1:
            db += 1
        index += 1
    return db


def konzol_kiir():
    print("II/D,E:")
    print("\tA páratlanok száma:{}".format(paratlanok_szama()))


def fajlba_kiir():
    beFalj = open("eredmeny.txt", "w", encoding="utf-8")
    print("II/F", file=beFalj)
    print("\tA páratlanok száma:{}".format(paratlanok_szama()), file=beFalj)
    beFalj.close()
