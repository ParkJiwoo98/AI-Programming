import problem


def main():
    p = problem.Numeric()
    p.createProblem()
    gradientDescent(p)
    p.describeProblem()
    displaySetting(p)
    p.displayResult()


def gradientDescent(p):
    current = p.randomInit()
    valueC = p.evaluate(current)
    while True:
        neighbors = p.gradientMutants(current)
        successor, valueS = p.bestOf(neighbors)
        if valueS >= valueC:
            break
        else:
            current = successor
            valueC = valueS
    p.saveResult(current, valueC)


def displaySetting(p):
    print()
    print("Search algorithm: Gradient-Descent Hill Climbing")
    print()
    print("Update Rate:", p.updateRate)


main()