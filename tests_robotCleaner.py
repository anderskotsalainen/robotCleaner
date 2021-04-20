import unittest
from main import validateNumberOfInputCommands, validateNumberOfSteps, validateStartingPosition
from robotCleaner import RobotCleaner


class TestRobotCleaner(unittest.TestCase):

    def test_validateNumberOfInputCommands(self):
        self.assertEqual(validateNumberOfInputCommands(10), 10)
        self.assertEqual(validateNumberOfInputCommands(-5), -1)
        self.assertEqual(validateNumberOfInputCommands(10001), -1)

    def test_validateNumberOfSteps(self):
        self.assertEqual(validateNumberOfSteps(10), 10)
        self.assertEqual(validateNumberOfInputCommands(-5), -1)
        self.assertEqual(validateNumberOfInputCommands(10001), -1)

    def test_validateStartingPosition(self):
        self.assertTrue(validateStartingPosition(500, -500))
        self.assertFalse(validateStartingPosition(-100001, 500))

    def test_RobotCleaner(self):
        robotCleaner = RobotCleaner(0, 0)
        self.assertEqual(robotCleaner.xCoordinate, 0)
        self.assertEqual(robotCleaner.yCoordinate, 0)
        robotCleaner.moveRobotCleaner('N', 1)
        self.assertEqual(robotCleaner.yCoordinate, 1)
        robotCleaner.moveRobotCleaner('S', 1)
        self.assertEqual(robotCleaner.yCoordinate, 0)
        robotCleaner.moveRobotCleaner('E', 1)
        self.assertEqual(robotCleaner.xCoordinate, 1)
        robotCleaner.moveRobotCleaner('W', 1)
        self.assertEqual(robotCleaner.xCoordinate, 0)
        self.assertEqual(len(robotCleaner.cleanedLocations), 3)


if __name__ == '__main__':
    unittest.main()
