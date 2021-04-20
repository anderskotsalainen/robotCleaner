class RobotCleaner:
    def __init__(self, startingXCoordinate, startingYCoordinate):
        self.xCoordinate = startingXCoordinate
        self.yCoordinate = startingYCoordinate
        self.cleanedLocations = dict()
        self.cleanedLocations[str(startingXCoordinate) +
                              str(startingYCoordinate)] = 'cleaned'

    def moveRobotCleaner(self, direction, numberOfSteps):
        if direction == 'N':
            for x in range(numberOfSteps):
                self.yCoordinate += 1
                self.cleanedLocations[str(
                    self.xCoordinate)+str(self.yCoordinate)] = 'cleaned'

        elif direction == 'S':

            for x in range(numberOfSteps):
                self.yCoordinate -= 1
                self.cleanedLocations[str(
                    self.xCoordinate)+str(self.yCoordinate)] = 'cleaned'

        elif direction == 'E':

            for x in range(numberOfSteps):
                self.xCoordinate += 1
                self.cleanedLocations[str(
                    self.xCoordinate)+str(self.yCoordinate)] = 'cleaned'

        elif direction == 'W':

            for x in range(numberOfSteps):
                self.xCoordinate -= 1
                self.cleanedLocations[str(
                    self.xCoordinate)+str(self.yCoordinate)] = 'cleaned'
