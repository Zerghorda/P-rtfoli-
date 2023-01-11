class Pogyasz:
    def __init__(self, sor):
        daraboltSor = sor.split("#")
        self.a = int(daraboltSor[0])
        self.b = int(daraboltSor[1])
        self.c = int(daraboltSor[2])
        self.m = int(daraboltSor[3])

    def __str__(self):
        return "a:{},b{},c:{},d:{}".format(self.a, self.b, self.c, self.m)
