class Bet:
    def __init__(self, number=0, title='', mapOfAllBets={}):
        self.number = number
        self.title = title
        self.mapOfAllBets = mapOfAllBets

    number = 0
    title = ''
    mapOfAllBets = {}

    def __str__(self):
        v = self.title
        for x, y in self.mapOfAllBets.items():
            v = v + "," + x + "," + y
        return v

    def __repr__(self):
        return self.title.__repr__() + self.mapOfAllBets.__repr__()

    def getBetsWithLowCaf(self):
        lowCaf = {}
        for type, caf in self.mapOfAllBets.items():
            if caf < 1.5:
                lowCaf.append(type, caf)
        return lowCaf
