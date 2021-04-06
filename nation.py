class Nation:
    name = ''
    continent = ''
    population = 0
    landArea = 0
    dict = {}

    def __init__(self):
        self.name = ''
        self.continent = ''
        self.population = 0
        self.landArea = 0
        self.dict.clear()

    def insertCountry(self, name, continent, population, landArea):
        self.name = name
        self.continent = continent
        self.population = population
        self.landArea = landArea
        self.dict[name] = {"name" : name, "cont" : continent, "popl" : population, "area" : landArea}

    def getName(self, name):
        return self.dict[name]["name"]

    def getContinent(self, name):
        return self.dict[name]["cont"]

    def getPopulation(self, name):
        return self.dict[name]["popl"]

    def getLandArea(self, name):
        return self.dict[name]["area"]

    def popDensity(self, name):
        return float(self.getPopulation(name)) / float(self.getLandArea(name))

    def __str__(self, name):
        return name + ': ' + self.getContinent(name) + ' ' + str(self.getPopulation(name)) + ' ' + str(self.getLandArea(name))
