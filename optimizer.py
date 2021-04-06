from setup import Setup
import random
import math


class Optimizer(Setup):
    def __init__(self):
        super().__init__()
        self.pType = 0
        self.numExp = 0

    def setVariables(self, parameters):
        self.pType = parameters['pType']
        self.numExp = parameters['numExp']
        Setup.setVariables(self, parameters)

    def getNumExp(self):
        return self.numExp

    def displayNumExp(self):
        print()
        print("Number of experiments:", self.numExp)

    def displaySetting(self):
        if self.pType == 1 and self.aType != 4 and self.aType != 6:
            print("Mutation step size:", self.delta)


class HillClimbing(Optimizer):
    def __init__(self):
        super().__init__()
        self.limitStuck = 0
        self.numRestart = 0

    def displaySetting(self):
        if self.numRestart > 1:
            print("Number of random restarts:", self.numRestart)
            print()
        Optimizer.displaySetting(self)
        if self.aType == 2 or self.aType == 3:
            print("Max evaluations with no improvement: {0:,} iterations".format(self.limitStuck))

    def randomRestart(self, p):
        i = 1
        self.run(p)
        bestSolution = p.getSolution()
        bestMinimum = p.getValue()
        numEval = p.getNumEval()
        while i < self.numRestart:
            self.run(p)
            newSolution = p.getSolution()
            newMinimum = p.getValue()
            numEval += p.getNumEval()
            if newMinimum < bestMinimum:
                bestSolution = newSolution
                bestMinimum = newMinimum
            i += 1
        p.saveResult(bestSolution, bestMinimum)

    def setVariables(self, parameters):
        self.limitStuck = parameters['limitStuck']
        self.numRestart = parameters['numRestart']
        Optimizer.setVariables(self, parameters)


class SteepestAscent(HillClimbing):
    def run(self, p):
        current = p.randomInit()
        valueC = p.evaluate(current)
        while True:
            neighbors = p.mutants(current)
            successor, valueS = self.bestOf(neighbors, p)
            if valueS >= valueC:
                break
            else:
                current = successor
                valueC = valueS
        p.saveResult(current, valueC)

    def bestOf(self, neighbors, p):
        best = neighbors[0]
        bestValue = p.evaluate(best)
        for i in range(len(neighbors)):
            newValue = p.evaluate(neighbors[i])
            if newValue < bestValue:
                bestValue = newValue
                best = neighbors[i]
        return best, bestValue

    def displaySetting(self):
        print()
        print("Search algorithm: Steepest-Ascent Hill Climbing")
        print()
        HillClimbing.displaySetting(self)


class FirstChoice(HillClimbing):
    def run(self, p):
        # file = open('FirstChoiceTSP100.txt', 'w')
        current = p.randomInit()
        valueC = p.evaluate(current)
        # file.writelines(str(valueC) + '\n')
        i = 0
        while i < self.limitStuck:
            successor = p.randomMutant(current)
            valueS = p.evaluate(successor)
            # file.writelines(str(valueS) + '\n')
            if valueS < valueC:
                current = successor
                valueC = valueS
                i = 0
            else:
                i += 1
        # file.close()
        p.saveResult(current, valueC)

    def displaySetting(self):
        print()
        print("Search algorithm: First-Choice Hill Climbing")
        print()
        HillClimbing.displaySetting(self)


class Stochastic(HillClimbing):
    def run(self, p):
        current = p.randomInit()
        valueC = p.evaluate(current)
        i = 0
        while i < self.limitStuck:
            neighbors = p.mutants(current)
            successor, valueS = self.stochasticBest(neighbors, p)
            if valueS < valueC:
                current = successor
                valueC = valueS
                i = 0
            else:
                i += 1
        p.saveResult(current, valueC)

    def displaySetting(self):
        print()
        print("Search algorithm: Stochastic Hill Climbing")
        print()
        HillClimbing.displaySetting(self)

    def stochasticBest(self, neighbors, p):
        # Smaller values are better in the following list
        valuesForMin = [p.evaluate(indiv) for indiv in neighbors]
        largeValue = max(valuesForMin) + 1
        valuesForMax = [largeValue - val for val in valuesForMin]
        # Now, larger values are better
        total = sum(valuesForMax)
        randValue = random.uniform(0, total)
        s = valuesForMax[0]
        for i in range(len(valuesForMax)):
            if randValue <= s: # The one with index i is chosen
                break
            else:
                s += valuesForMax[i+1]
        return neighbors[i], valuesForMin[i]


class GradientDescent(HillClimbing):
    def run(self, p):
        current = p.randomInit()
        valueC = p.evaluate(current)
        while True:
            nextP = p.takeStep(current, valueC)
            valueN = p.evaluate(nextP)
            if valueN >= valueC:
                break
            else:
                current = nextP
                valueC = valueN
        p.saveResult(current, valueC)

    def displaySetting(self):
        print()
        print("Search algorithm: Gradient Descent Hill Climbing")
        print()
        HillClimbing.displaySetting(self)
        print("Update rate:", self.updateRate)
        print("Increment for calculating derivatives:", self.dx)


class MetaHeuristics(Optimizer):
    def __init__(self):
        super().__init__()
        self.limitEval = 0
        self.whenBestFound = 0

    def setVariables(self, parameters):
        self.limitEval = parameters['limitEval']
        Optimizer.setVariables(self, parameters)

    def displaySetting(self):
        Optimizer.displaySetting(self)
        print("Number of evaluations until termination: {0:,}".format(self.limitEval))

    def getWhenBestFound(self):
        return self.whenBestFound


class SimulatedAnnealing(MetaHeuristics):
    def __init__(self):
        MetaHeuristics.__init__(self)
        self._numSample = 100

    def run(self, p):
        # file = open('SimulatedAnnealingTSP100.txt', 'w')
        current = p.randomInit()
        valueC = p.evaluate(current)
        best, valueBest = current, valueC
        whenBestFound = i = 1
        # file.write(str(valueC) + '\n')
        T = self.initTemp(p)
        while True:
            T = self.tSchedule(T)
            if T == 0 or i == self.limitEval:
                break
            next = p.randomMutant(current)
            valueS = p.evaluate(next)
            i += 1
            # file.write(str(valueS) + '\n')
            E = valueS - valueC
            if E < 0:
                self.whenBestFound = i
                current = next
                valueC = valueS
                best = current
                valueBest = valueC
                whenBestFound = i
            elif random.uniform(0, 1) <= math.exp(-E / T):
                current = next
                valueC = valueS
        # file.close()
        self.whenBestFound = whenBestFound
        p.saveResult(best, valueBest)

    def tSchedule(self, t):
        return t * (1 - (1 / 10**4))

    def initTemp(self, p): # To set initial acceptance probability to 0.5
        diffs = []
        for i in range(self._numSample):
            c0 = p.randomInit()     # A random point
            v0 = p.evaluate(c0)     # Its value
            c1 = p.randomMutant(c0) # A mutant
            v1 = p.evaluate(c1)     # Its value
            diffs.append(abs(v1 - v0))
        dE = sum(diffs) / self._numSample  # Average value difference
        t = dE / math.log(2)        # exp(–dE/t) = 0.5
        return t

    def displaySetting(self):
        print()
        print("Search algorithm: Simulated Annealing Meta Heuristics")
        print()
        MetaHeuristics.displaySetting(self)


class GA(MetaHeuristics):
    def __init__(self):
        MetaHeuristics.__init__(self)
        self._popSize = 0     # Population size
        self._uXp = 0   # Probability of swappping a locus for Xover
        self._mrF = 0   # Multiplication factor to 1/n for bit-flip mutation
        self._XR = 0    # Crossover rate for permutation code
        self._mR = 0    # Mutation rate for permutation code
        self._pC = 0    # Probability parameter for Xover
        self._pM = 0    # Probability parameter for mutation

    def run(self, p):
        pop = p.initializePop(self._popSize)
        best = self.findBest(pop, p)
        whenBest = i = 1
        while i < self.limitEval:
            newPop = []
            j = 0
            while j < self._popSize:
                parent1, parent2 = self.selectParent(pop)
                child1, child2 = p.crossover(parent1, parent2, self._pC)
                child1_ = p.mutation(child1, self._pM)
                child2_ = p.mutation(child2, self._pM)
                p.evalInd(child1_)
                p.evalInd(child2_)
                newPop.extend([child1_])
                newPop.extend([child2_])
                j += 2
            pop = newPop
            newBest = self.findBest(pop, p)
            if newBest[0] < best[0]:
                best = newBest
                whenBest = p.getNumEval()
            i += 1
        self.whenBestFound = whenBest
        bestSolution = p.indToSol(best)
        bestMinimum = best[0]
        p.saveResult(bestSolution, bestMinimum)

    def findBest(self, pop, p):
        best = pop[0]
        p.evalInd(best)
        bestValue = best[0]
        for i in range(len(pop)):
            p.evalInd(pop[i])
            newValue = pop[i][0]
            if newValue < bestValue:
                best = pop[i]
        return best

    def selectParent(self, pop):
        ind1, ind2 = self.selectTwo(pop)
        parent1 = self.tournament(ind1, ind2)
        ind1, ind2 = self.selectTwo(pop)
        parent2 = self.tournament(ind1, ind2)
        return parent1, parent2

    def selectTwo(self, pop):
        pop_ = pop[:]
        random.shuffle(pop_)
        return pop_[0], pop_[1]

    def tournament(self, ind1, ind2):
        if ind1[0] < ind2[0]:
            return ind1
        else:
            return ind2

    def setVariables(self, parameters):
        MetaHeuristics.setVariables(self, parameters)
        self._popSize = parameters['popSize']
        self._uXp = parameters['uXp']
        self._mrF = parameters['mrF']
        self._XR = parameters['XR']
        self._mR = parameters['mR']
        if self.pType == 1:
            self._pC = self._uXp
            self._pM = self._mrF
        if self.pType == 2:
            self._pC = self._XR
            self._pM = self._mR

    def displaySetting(self):
        print()
        print("Search Algorithm: Genetic Algorithm")
        print()
        MetaHeuristics.displaySetting(self)
        print()
        print("Population size:", self._popSize)
        if self.pType == 1:   # Numerical optimization
            print("Number of bits for binary encoding:", self._resolution)
            print("Swap probability for uniform crossover:", self._uXp)
            print("Multiplication factor to 1/L for bit-flip mutation:",
                  self._mrF)
        elif self.pType == 2: # TSP
            print("Crossover rate:", self._XR)
            print("Mutation rate:", self._mR)
