import unittest

import part1, part2

class Test_TestPart1(unittest.TestCase):
    def test_part1(self):

        inputData = ['00100','11110','10110','10111','10101','01111','00111','11100','10000','11001','00010','01010']

        self.assertEqual(part1.calculatePower(inputData), 198)

class Test_TestPart2(unittest.TestCase):
    def test_part2(self):

        inputData = ['00100','11110','10110','10111','10101','01111','00111','11100','10000','11001','00010','01010']

        self.assertEqual(part2.calculateLifeRating(inputData), 230)

if __name__ == '__main__':
    unittest.main()
