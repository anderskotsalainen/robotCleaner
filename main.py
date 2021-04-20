

from robotCleaner import RobotCleaner


def reportFinalCleaningTotal(numberOfSpotsCleaned):
    print('=> Cleaned: ', numberOfSpotsCleaned)


def validateNumberOfInputCommands(numberOfCommands):
    if numberOfCommands >= 0 and numberOfCommands <= 10000:
        return numberOfCommands
    else:
        return -1


def validateNumberOfSteps(numberOfSteps):
    if numberOfSteps >= 0 and numberOfSteps <= 10000:
        return numberOfSteps
    else:
        return -1


def validateStartingPosition(startingXCoordinate, startingYCoordinate):
    if startingXCoordinate >= -100000 and startingXCoordinate <= 100000 and startingYCoordinate >= -100000 and startingYCoordinate <= 100000:
        return True
    else:
        return False


def main():
    inputLinCount = int(0)
    numberOfCommands = int(0)
    startingXCoordinate = int(0)
    startingYCoordinate = int(0)

    while True:
        data = input()
        inputLinCount += 1
        if inputLinCount == 1:
            numberOfCommands = validateNumberOfInputCommands(int(data))
            if numberOfCommands == -1:
                reportFinalCleaningTotal(0)
                break
        elif inputLinCount == 2:
            if numberOfCommands == 0:
                reportFinalCleaningTotal(0)
                break
            else:
                startingXCoordinate = int(str(data).rsplit(' ')[0])
                startingYCoordinate = int(str(data).rsplit(' ')[1])
                if(validateStartingPosition(startingXCoordinate, startingYCoordinate)):
                    robotCleaner = RobotCleaner(
                        startingXCoordinate, startingYCoordinate)
                else:
                    reportFinalCleaningTotal(0)
                    break
        else:
            direction = str(data).rsplit(' ')[0]
            numberOfSteps = int(str(data).rsplit(' ')[1])
            if validateNumberOfSteps(numberOfSteps) != -1:
                robotCleaner.moveRobotCleaner(direction, numberOfSteps)
            else:
                continue
            if inputLinCount-2 >= numberOfCommands:
                reportFinalCleaningTotal(len(robotCleaner.cleanedLocations))
                break


if __name__ == "__main__":
    main()
