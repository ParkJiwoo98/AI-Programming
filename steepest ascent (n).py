import problem


def main():
    p = problem.Numeric()
    p.createProblem()
    steepestAscent(p)
    p.describeProblem()
    displaySetting(p)
    p.displayResult()


def steepestAscent(p):
    current = p.randomInit()
    valueC = p.evaluate(current)
    while True:
        neighbors = p.mutants(current)
        successor, valueS = p.bestOf(neighbors)
        if valueS >= valueC:
            break
        else:
            current = successor
            valueC = valueS
    p.saveResult(current, valueC)


def displaySetting(p):
    print()
    print("Search algorithm: Steepest-Ascent Hill Climbing")
    print()
    print("Mutation step size:", p.DELTA)


main()