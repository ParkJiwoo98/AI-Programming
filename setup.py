class Setup:
    def __init__(self):
        self.delta = 0.01
        self.updateRate = 0
        self.dx = 0
        self.aType = 0
        self._resolution = 0

    def setVariables(self, parameters):
        if parameters['pType'] == 1:
            self._resolution = int(1 / parameters['mrF'])
        if parameters['pType'] == 2:
            self._resolution = int(1 / parameters['mR'])
        self.delta = parameters['delta']
        self.updateRate = parameters['alpha']
        self.dx = parameters['dx']
        self.aType = parameters['aType']

    def getAType(self):
        return self.aType