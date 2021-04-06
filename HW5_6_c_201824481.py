import pickle
from nation import Nation

nationDict = Nation()
f1 = open("nationsDict.dat", "rb")
listOfCountries = pickle.load(f1)
name = []
f1.close()

continent = str(input('Enter a continent: '))
for key, value in listOfCountries.items():
    if value["cont"] == continent:
        nationDict.insertCountry(value["name"], value["cont"], value["popl"], value["area"])
        name.append([value["name"], nationDict.popDensity(value["name"])])

name.sort(key=lambda x:x[1], reverse=True)

for i in range(0, 5):
    print('  ' + name[i][0])