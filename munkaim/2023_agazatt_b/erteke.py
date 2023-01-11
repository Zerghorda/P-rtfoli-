def fel1():
    print("I/A,B:")
    neve = input("\tÉtel neve:")
    rendelo = input("\tÉtel rendelőjének neve:")
    ertek = int(input("\tÉrtékelés(1-5):"))
    print("I/C:")
    if ertek < 0:
        print("\tAz értékelés nem lehet negatív!")
    elif ertek > 5:
        print("\t5 pont feletti értékelés nem elfogadható!")
    else:
        print("\tKöszönjük az értékelést!")



