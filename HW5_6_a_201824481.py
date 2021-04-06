import pickle
from nation import Nation

f1 = open("UN.txt", "r")
listOfCountries = f1.readlines()
f1.close()

nationDict = Nation()
for i in range(len(listOfCountries)):
    listOfCountries[i] = listOfCountries[i].rstrip()
    listOfCountries[i] = listOfCountries[i].split(',')
    nationDict.insertCountry(listOfCountries[i][0], listOfCountries[i][1], listOfCountries[i][2], listOfCountries[i][3])

name = str(input('Enter a country: '))
print(nationDict.__str__(name))

f2 = open("nationsDict.dat", "wb")
pickle.dump(nationDict.dict, f2)
f2.close()