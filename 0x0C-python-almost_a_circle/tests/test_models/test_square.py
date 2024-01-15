#!/usr/bin/python3
"""Defines unittests for models/square.py.

Unittest classes:
    TestSquare_instantiation - line 23
    TestSquare_size - line 87
    TestSquare_x - line 111
    TestSquare_y - line 131
    TestSquare_order_of_initialization - line 151
    TestSquare_area - line 167
    TestSquare_stdout - line 188
    TestSquare_update_args - line 271
    TestSquare_update_kwargs - line 321
    TestSquare_to_dictionary - 367
"""
import io
import sys
import unittest
from models.base import Base
from models.square import Square


class TestSquare_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Square class."""

    def test_isbase(self):
        self.assertIsInstance(Square(1), Base)

    def test_issq(self):
        self.assertIsInstance(Square(1), Square)

    def test_noargs(self):
        with self.assertRaises(TypeError):
            Square()

    def test_1arg(self):
        sq1 = Square(10)
        sq2 = Square(1)
        self.assertEqual(sq1.id, sq2.id - 1)

    def test_2arg(self):
        sq1 = Square(1, 2)
        sq2 = Square(2, 1)
        self.assertEqual(sq1.id, sq2.id - 1)

    def test_3args(self):
        sq1 = Square(1, 2, 3)
        sq2 = Square(4, 5, 6)
        self.assertEqual(sq1.id, sq2.id - 1)

    def test_4args(self):
        self.assertEqual(7, Square(10, 2, 2, 7).id)

    def test_more4args(self):
        with self.assertRaises(TypeError):
            Square(9, 6, 11, 23, 55)

    def test_size_private(self):
        with self.assertRaises(AttributeError):
            print(Square(10, 2, 3, 4).__size)

    def test_sizegetter(self):
        self.assertEqual(4, Square(4, 1, 6, 3).size)

    def test_sizesetter(self):
        sq = Square(1, 2, 3, 4)
        sq.size = 5
        self.assertEqual(5, sq.size)

    def test_wgetter(self):
        sq = Square(1, 2, 3, 4)
        sq.size = 5
        self.assertEqual(5, sq.width)

    def test_hgetter(self):
        s = Square(1, 2, 3, 4)
        s.size = 5
        self.assertEqual(5, s.height)

    def test_xgetter(self):
        self.assertEqual(0, Square(1).x)

    def test_ygetter(self):
        self.assertEqual(0, Square(1).y)


class TestSquare_size(unittest.TestCase):
    """Unittests for testing size initialization of the Square class."""

    def test_Nosize(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    def test_strsize(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("asd")

    def test_fsize(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(56.4)

    def test_negsize(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-45, 53)

    def test_zerosize(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, 12)


class TestSquare_x(unittest.TestCase):
    """Unittests for testing initialization of Square x attribute."""

    def test_Nox(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, None)

    def test_strx(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "asdid")

    def test_flx(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, 1.3)

    def test_negx(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(12, -11, 3)


class TestSquare_y(unittest.TestCase):
    """Unittests for testing initialization of Square y attribute."""

    def test_Noy(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(12, 21, None)

    def test_stry(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, "iid")

    def test_fly(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, 12.4)

    def test_negy(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(1, 1, -3)


class TestSquare_order_of_initialization(unittest.TestCase):
    """Unittests for testing order of Square attribute initialization."""

    def test_sbx(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("wvhk", "wbvjk")

    def test_sby(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("inadse", 1, "wjkbr")

    def test_xby(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "wvno", "jno")


class TestSquare_area(unittest.TestCase):
    """Unittests for testing the area method of the Square class."""

    def test_arsmall(self):
        self.assertEqual(100, Square(10, 0, 0, 1).area())

    def test_arlarge(self):
        s = Square(10000000000, 0, 0, 1)
        self.assertEqual(100000000000000000000, s.area())

    def test_archange(self):
        s = Square(4, 0, 0, 1)
        s.size = 5
        self.assertEqual(25, s.area())

    def test_ar1arg(self):
        s = Square(4, 12, 8, 1)
        with self.assertRaises(TypeError):
            s.area(1)


class TestSquare_stdout(unittest.TestCase):
    """Unittests for testing __str__ and display methods of Square class."""

    @staticmethod
    def getstd(squ, meth):
        """Captures and returns text printed to stdout.

        Args:
            squ (Square): The Square ot print to stdout.
            meth (str): The method to run on sq.
        Returns:
            The text printed to stdout by calling method on sq.
        """
        getit = io.StringIO()
        sys.stdout = getit
        if meth == "print":
            print(squ)
        else:
            squ.display()
        sys.stdout = sys.__stdout__
        return getit

    def test_strprntsize(self):
        s = Square(4)
        getit = TestSquare_stdout.getstd(s, "print")
        correct = "[Square] ({}) 0/0 - 4\n".format(s.id)
        self.assertEqual(correct, getit.getvalue())

    def test_strsize_x(self):
        s = Square(5, 5)
        correct = "[Square] ({}) 5/0 - 5".format(s.id)
        self.assertEqual(correct, s.__str__())

    def test_strsizexy(self):
        s = Square(7, 4, 22)
        correct = "[Square] ({}) 4/22 - 7".format(s.id)
        self.assertEqual(correct, str(s))

    def test_strsxyid(self):
        s = Square(2, 88, 4, 19)
        self.assertEqual("[Square] (19) 88/4 - 2", str(s))

    def test_strchange(self):
        s = Square(7, 0, 0, [4])
        s.size = 15
        s.x = 8
        s.y = 10
        self.assertEqual("[Square] ([4]) 8/10 - 15", str(s))

    def test_str1arg(self):
        s = Square(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            s.__str__(1)

    # Test display method
    def test_dsize(self):
        s = Square(2, 0, 0, 9)
        getit = TestSquare_stdout.getstd(s, "display")
        self.assertEqual("##\n##\n", getit.getvalue())

    def test_dx(self):
        s = Square(3, 1, 0, 18)
        getit = TestSquare_stdout.getstd(s, "display")
        self.assertEqual(" ###\n ###\n ###\n", getit.getvalue())

    def test_dy(self):
        s = Square(4, 0, 1, 9)
        getit = TestSquare_stdout.getstd(s, "display")
        display = "\n####\n####\n####\n####\n"
        self.assertEqual(display, getit.getvalue())

    def test_dsxy(self):
        s = Square(2, 3, 2, 1)
        getit = TestSquare_stdout.getstd(s, "display")
        display = "\n\n   ##\n   ##\n"
        self.assertEqual(display, getit.getvalue())

    def test_display_one_arg(self):
        s = Square(3, 4, 5, 2)
        with self.assertRaises(TypeError):
            s.display(1)


class TestSquare_update_args(unittest.TestCase):
    """Unittests for testing update args method of the Square class."""

    def test_ua0(self):
        s = Square(10, 10, 10, 10)
        s.update()
        self.assertEqual("[Square] (10) 10/10 - 10", str(s))

    def test_ua1(self):
        s = Square(10, 10, 10, 10)
        s.update(89)
        self.assertEqual("[Square] (89) 10/10 - 10", str(s))

    def test_ua2(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2)
        self.assertEqual("[Square] (89) 10/10 - 2", str(s))

    def test_ua3(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2, 3)
        self.assertEqual("[Square] (89) 3/10 - 2", str(s))

    def test_ua4(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2, 3, 4)
        self.assertEqual("[Square] (89) 3/4 - 2", str(s))

    def test_uam4(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2, 3, 4, 5)
        self.assertEqual("[Square] (89) 3/4 - 2", str(s))

    def test_uaws(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2)
        self.assertEqual(2, s.width)

    def test_uahs(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2)
        self.assertEqual(2, s.height)

    def test_uanoid(self):
        s = Square(10, 10, 10, 10)
        s.update(None)
        c = "[Square] ({}) 10/10 - 10".format(s.id)
        self.assertEqual(c, str(s))


class TestSquare_update_kwargs(unittest.TestCase):
    """Unittests for testing update kwargs method of Square class."""

    def test_uk1one(self):
        s = Square(10, 10, 10, 10)
        s.update(id=1)
        self.assertEqual("[Square] (1) 10/10 - 10", str(s))

    def test_uk2two(self):
        s = Square(10, 10, 10, 10)
        s.update(size=1, id=2)
        self.assertEqual("[Square] (2) 10/10 - 1", str(s))

    def test_uk3three(self):
        s = Square(10, 10, 10, 10)
        s.update(y=1, size=3, id=89)
        self.assertEqual("[Square] (89) 10/1 - 3", str(s))

    def test_uk4four(self):
        s = Square(10, 10, 10, 10)
        s.update(id=89, x=1, y=3, size=4)
        self.assertEqual("[Square] (89) 1/3 - 4", str(s))

    def test_ukm4width_setter(self):
        s = Square(10, 10, 10, 10)
        s.update(id=89, size=8)
        self.assertEqual(8, s.width)

    def test_ukheight_setter(self):
        s = Square(10, 10, 10, 10)
        s.update(id=89, size=9)
        self.assertEqual(9, s.height)

    def test_ukNone_id(self):
        s = Square(10, 10, 10, 10)
        s.update(id=None)
        correct = "[Square] ({}) 10/10 - 10".format(s.id)
        self.assertEqual(correct, str(s))

    def test_update_kwargs_None_id_and_more(self):
        s = Square(10, 10, 10, 10)
        s.update(id=None, size=7, x=18)
        correct = "[Square] ({}) 18/10 - 7".format(s.id)
        self.assertEqual(correct, str(s))


class TestSquare_to_dictionary(unittest.TestCase):
    """Unittests for testing to_dictionary method of the Square class."""

    def test_tdo(self):
        s = Square(1, 1, 1, 1)
        correct = {'id': 1, 'x': 1, 'size': 1, 'y': 1}
        self.assertDictEqual(correct, s.to_dictionary())

    def test_tdnochan(self):
        s1 = Square(1, 1, 1, 1)
        s2 = Square(1, 1, 11)
        s2.update(**s1.to_dictionary())
        self.assertNotEqual(s1, s2)

    def test_tdarg(self):
        s = Square(1, 1, 1, 1)
        with self.assertRaises(TypeError):
            s.to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
