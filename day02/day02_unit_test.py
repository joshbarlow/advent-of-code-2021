import unittest

import part1, part2

class Test_TestPart1(unittest.TestCase):
    def test_part1(self):

        inputData = ['forward 5','down 5','forward 8','up 3','down 8','forward 2']

        self.assertEqual(part1.calculateDepth(inputData), 150)

class Test_TestPart2(unittest.TestCase):
    def test_part2(self):

        inputData = ['forward 5','down 5','forward 8','up 3','down 8','forward 2']

        self.assertEqual(part2.calculateDepth(inputData), 900)

if __name__ == '__main__':
    unittest.main()
