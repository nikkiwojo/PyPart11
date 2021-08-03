import unittest
import shapes

class testing_shapes(unittest.TestCase):

    def test_rectangle_perimeter(self):
        given = (10,7)
        expected = 34
        actual = shapes.rectangle(10,7)
        self.assertEqual(expected, actual.perimeter())


    def test_square_perimeter(self):
        given = (50,50)
        expected = 200
        actual = shapes.square(50,50)
        self.assertEqual(expected, actual.perimeter())


    def test_rectangle_area(self):
        given = (3,7)
        expected = 21
        actual = shapes.rectangle(3,7)
        self.assertEqual(expected, actual.area())


    def test_square_area(self):
        given = (20,20)
        expected = 400
        actual = shapes.square(20,20)
        self.assertEqual(expected, actual.area())