import random
from setup import Setup
import math


class Problem(Setup):
    def __init__(self):
        super().__init__()
        self.solution = []
        self.minimum = 0
        self.NumEval = 0

        self.pFileName = ''
        self.bestSolution = []
        self.bestMinimum = 0
        self.avgMinimum = 0
        self.avgNumEval = 0
        self.sumNumEval = 0
        self.avgWhen = 0

    def setVariables(self, parameters):
        Setup.setVariables(self, parameters)
        self.pFileName = parameters['pFileName']

    def saveResult(self, solution, minimum):
        self.solution = solution
        self.minimum = minimum

    def report(self):
        aType = self.aType
        if 1 <= aType <= 4:
            print("Average number of evaluations: {0:,}".format(round(self.avgNumEval)))
        if 5 <= aType <= 6:
            print("Average iteration of finding the best: {0:,}".format(self.avgWhen))
        print()

    def reportNumEvals(self):
        if 1 <= self.aType <= 4:
            print()
            print("Total number of evaluations: {0:,}".format(self.sumNumEval))

    def getSolution(self):
        return self.solution

    def getNumEval(self):
        return self.NumEval

    def getValue(self):
        return self.minimum

    def storeExpResult(self, results):
        self.bestSolution = results[0]
        self.bestMinimum = results[1]
        self.avgMinimum = results[2]
        self.avgNumEval = results[3]
        self.sumNumEval = results[4]
        self.avgWhen = results[5]


class Numeric(Problem):
    def __init__(self):
        super().__init__()
        self.domain = []
        self.expression = ''

    def setVariables(self, parameters):
        Problem.setVariables(self, parameters)
        varNames = []
        low = []
        up = []
        infile = open(self.pFileName, 'r')
        self.expression = infile.readline()
        line = infile.readline()
        while line != '':
            data = line.split(',')
            varNames.append(data[0])
            low.append(float(data[1]))
            up.append(float(data[2]))
            line = infile.readline()
        infile.close()
        self.domain = [varNames, low, up]

    def randomInit(self):
        init = []
        for i in range(0, 5):
            data = random.uniform(self.domain[1][i], self.domain[2][i])
            init.append(data)
        return init

    def evaluate(self, current):
        self.NumEval += 1
        expr = self.expression
        varNames = self.domain[0]
        for i in range(len(varNames)):
            assignment = varNames[i] + '=' + str(current[i])
            exec(assignment)
        return eval(expr)

    def mutate(self, current, i, d):
        curCopy = current[:]
        l = self.domain[1][i]
        u = self.domain[2][i]
        if l <= (curCopy[i] + d) <= u:
            curCopy[i] += d
        return curCopy

    def describe(self):
        print()
        print("Objective function:")
        print(self.expression)
        print("Search space:")
        varNames = self.domain[0]
        low = self.domain[1]
        up = self.domain[2]
        for i in range(len(low)):
            print(" " + varNames[i] + ":", (low[i], up[i]))

    def randomMutant(self, current):
        i = random.randint(0, len(current) - 1)
        if random.uniform(0, 1) > 0.5:
            d = self.delta
        else:
            d = -self.delta
        return self.mutate(current, i, d)

    def mutants(self, current):
        neighbors = []
        for i in range(len(current)):
            mutant = self.mutate(current, i, self.delta)
            neighbors.append(mutant)
            mutant = self.mutate(current, i, -self.delta)
            neighbors.append(mutant)
        return neighbors

    def isLegal(self, x):
        low = self.domain[1]
        up = self.domain[2]
        flag = True
        for i in range(len(low)):
            if x[i] < low[i] or up[i] < x[i]:
                flag = False
                break
        return flag

    def takeStep(self, x, v):
        grad = self.gradient(x, v)
        xCopy = x[:]
        for i in range(len(xCopy)):
            xCopy[i] = xCopy[i] - self.updateRate * grad[i]
        if self.isLegal(xCopy):
            return xCopy
        else:
            return x

    def gradient(self, x, v):
        grad = []
        for i in range(len(x)):
            xCopyH = x[:]
            xCopyH[i] += self.dx
            g = (self.evaluate(xCopyH) - v) / self.dx
            grad.append(g)
        return grad

    def coordinate(self):
        c = [round(value, 3) for value in self.bestSolution]
        return tuple(c)

    def report(self):
        avgMinimum = round(self.avgMinimum, 3)
        print()
        print("Average objective value: {0:,}".format(avgMinimum))
        Problem.report(self)
        print("Best solution found:")
        print(self.coordinate())
        print("Best value: {0:,.3f}".format(self.bestMinimum))
        self.reportNumEvals()

    def initializePop(self, size):  # Make a population of given size
        pop = []
        for i in range(size):
            chromosome = self.randBinStr()
            pop.append([0, chromosome])
        return pop

    def randBinStr(self):
        k = len(self.domain[0]) * self._resolution
        chromosome = []
        for i in range(k):
            allele = random.randint(0, 1)
            chromosome.append(allele)
        return chromosome

    def evalInd(self, ind):  # ind: [fitness, chromosome]
        ind[0] = self.evaluate(self.decode(ind[1]))  # Record fitness

    def decode(self, chromosome):
        r = self._resolution
        low = self.domain[1]  # list of lower bounds
        up = self.domain[2]  # list of upper bounds
        genotype = chromosome[:]
        phenotype = []
        start = 0
        end = r  # The following loop repeats for # variables
        for var in range(len(self.domain[0])):
            value = self.binaryToDecimal(genotype[start:end],
                                         low[var], up[var])
            phenotype.append(value)
            start += r
            end += r
        return phenotype

    def binaryToDecimal(self, binCode, l, u):
        r = len(binCode)
        decimalValue = 0
        for i in range(r):
            decimalValue += binCode[i] * (2 ** (r - 1 - i))
        return l + (u - l) * decimalValue / 2 ** r

    def crossover(self, ind1, ind2, uXp):
        # pC is interpreted as uXp# (probability of swap)
        chr1, chr2 = self.uXover(ind1[1], ind2[1], uXp)
        return [0, chr1], [0, chr2]

    def uXover(self, chrInd1, chrInd2, uXp):  # uniform crossover
        chr1 = chrInd1[:]  # Make copies
        chr2 = chrInd2[:]
        for i in range(len(chr1)):
            if random.uniform(0, 1) < uXp:
                chr1[i], chr2[i] = chr2[i], chr1[i]
        return chr1, chr2

    def mutation(self, ind, mrF):  # bit-flip mutation
        # pM is interpreted as mrF (factor to adjust mutation rate)
        child = ind[:]  # Make copy
        n = len(ind[1])
        for i in range(n):
            if random.uniform(0, 1) < mrF * (1 / n):
                child[1][i] = 1 - child[1][i]
        return child

    def indToSol(self, ind):
        return self.decode(ind[1])


class Tsp(Problem):
    def __init__(self):
        super().__init__()
        self.numCities = 0
        self.locations = []
        self.table = []

    def setVariables(self, parameters):
        Problem.setVariables(self, parameters)
        infile = open(self.pFileName, 'r')
        self.numCities = int(infile.readline())
        line = infile.readline()
        while line != '':
            self.locations.append(eval(line))
            line = infile.readline()
        infile.close()
        self.calcDistanceTable()

    def calcDistanceTable(self):
        for i in range(self.numCities):
            data = []
            for j in range(self.numCities):
                data.append(math.sqrt(math.pow((self.locations[i][0] - self.locations[j][0]), 2)
                                      + math.pow((self.locations[i][1] - self.locations[j][1]), 2)))
            self.table.append(data)

    def randomInit(self):
        init = list(range(self.numCities))
        random.shuffle(init)
        return init

    def evaluate(self, current):
        self.NumEval += 1
        cost = 0
        for i in range(self.numCities - 1):
            cost += self.table[current[i]][current[i+1]]
        return cost

    def inversion(self, current, i, j):
        curCopy = current[:]
        while i < j:
            curCopy[i], curCopy[j] = curCopy[j], curCopy[i]
            i += 1
            j -= 1
        return curCopy

    def describe(self):
        print()
        print("Number of cities:", self.numCities)
        print("City locations:")
        for i in range(self.numCities):
            print("{0:>12}".format(str(self.locations[i])), end='')
            if i % 5 == 4:
                print()

    def tenPerRow(self):
        for i in range(len(self.bestSolution)):
            print("{0:>5}".format(self.bestSolution[i]), end='')
            if i % 10 == 9:
                print()

    def randomMutant(self, current):
        while True:
            i, j = sorted([random.randrange(self.numCities)
                           for _ in range(2)])
            if i < j:
                curCopy = self.inversion(current, i, j)
                break
        return curCopy

    def mutants(self, current):
        neighbors = []
        count = 0
        triedPairs = []
        while count <= self.numCities:
            i, j = sorted([random.randrange(self.numCities) for _ in range(2)])
            if i < j and [i, j] not in triedPairs:
                triedPairs.append([i, j])
                curCopy = self.inversion(current, i, j)
                count += 1
                neighbors.append(curCopy)
        return neighbors

    def report(self):
        print()
        print("Average objective value: {0:,.3f}".format(self.avgMinimum))
        print()
        print("Best solution found:")
        self.tenPerRow()
        Problem.report(self)
        print("Best value: {0:,.3f}".format(self.bestMinimum))
        self.reportNumEvals()

    def initializePop(self, size):  # Make a population of given size
        n = self.numCities  # n: number of cities
        pop = []
        for i in range(size):
            chromosome = self.randomInit()
            pop.append([0, chromosome])
        return pop

    def evalInd(self, ind):  # ind: [fitness, chromosome]
        ind[0] = self.evaluate(ind[1])  # Record fitness

    def crossover(self, ind1, ind2, XR):
        # pC is interpreted as XR (crossover rate)
        if random.uniform(0, 1) <= XR:
            chr1, chr2 = self.oXover(ind1[1], ind2[1])
        else:
            chr1, chr2 = ind1[1][:], ind2[1][:]  # No change
        return [0, chr1], [0, chr2]

    def oXover(self, chrInd1, chrInd2):  # Ordered Crossover
        chr1 = chrInd1[:]
        chr2 = chrInd2[:]  # Make copies
        size = len(chr1)
        a, b = sorted([random.randrange(size) for _ in range(2)])
        holes1, holes2 = [True] * size, [True] * size
        for i in range(size):
            if i < a or i > b:
                holes1[chr2[i]] = False
                holes2[chr1[i]] = False
        # We must keep the original values somewhere
        # before scrambling everything
        temp1, temp2 = chr1, chr2
        k1, k2 = b + 1, b + 1
        for i in range(size):
            if not holes1[temp1[(i + b + 1) % size]]:
                chr1[k1 % size] = temp1[(i + b + 1) % size]
                k1 += 1
            if not holes2[temp2[(i + b + 1) % size]]:
                chr2[k2 % size] = temp2[(i + b + 1) % size]
                k2 += 1
        # Swap the content between a and b (included)
        for i in range(a, b + 1):
            chr1[i], chr2[i] = chr2[i], chr1[i]
        return chr1, chr2

    def mutation(self, ind, mR):  # mutation by inversion
        # pM is interpreted as mR (mutation rate for inversion)
        child = ind[:]  # Make copy
        if random.uniform(0, 1) <= mR:
            i, j = sorted([random.randrange(self.numCities)
                           for _ in range(2)])
            child[1] = self.inversion(child[1], i, j)
        return child

    def indToSol(self, ind):
        return ind[1]