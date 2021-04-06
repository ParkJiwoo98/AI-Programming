import problem


def main():
    p = problem.Tsp()
    p.createProblem()
    steepestAscent(p)
    p.describeProblem()
    displaySetting()
    p.displayResult()


def steepestAscent(p):
    current = p.randomInit()
    valueC = p.evaluate(current)
    while True:
        neighbors = p.mutants(current)
        (successor, valueS) = p.bestOf(neighbors)
        if valueS >= valueC:
            break
        else:
            current = successor
            valueC = valueS
    p.saveResult(current, valueC)


def displaySetting():
    print()
    print("Search algorithm: Steepest-Ascent Hill Climbing")


main()
