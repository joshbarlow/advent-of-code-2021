import unittest

import part1

def importData():
    with open('test_input.txt') as input_file:
        inputDataArray = input_file.readlines()
    return inputDataArray

class Test_TestPart1(unittest.TestCase):
    def test_part1(self):

        self.assertEqual(part1.calculateCucumberSteps(importData()), 58)

if __name__ == '__main__':
    unittest.main()
