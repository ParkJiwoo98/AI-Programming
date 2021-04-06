import problem


def main():
    p = problem.Tsp()
    p.createProblem()
    firstChoice(p)
    p.describeProblem()
    displaySetting()
    p.displayResult()


def firstChoice(p):
    current = p.randomInit()
    valueC = p.evaluate(current)
    i = 0
    while i < p.LIMIT_STUCK:
        successor = p.randomMutant(current)
        valueS = p.evaluate(successor)
        if valueS < valueC:
            current = successor
            valueC = valueS
            i = 0
        else:
            i += 1
    p.saveResult(current, valueC)


def displaySetting():
    print()
    print("Search algorithm: First-Choice Hill Climbing")


main()
