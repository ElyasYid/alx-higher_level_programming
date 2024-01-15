#!/usr/bin/python3
"""Defines unittests for models/rectangle.py.

Unittest classes:
    TestRectangle_instantiation - line 24
    TestRectangle_width - line 114
    TestRectangle_height - line 137
    TestRectangle_x - line 161
    TestRectangle_y - line 181
    TestRectangle_order_of_initialization - line 201
    TestRectangle_area - line 229
    TestRectangle_stdout - line 252
    TestRectangle_update_args - line 324
    TestRectangle_update_kwargs - line 363
    TestRectangle_to_dictionary - line 422
"""
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Rectangle class."""

    def test_recbase(self):
        self.assertIsInstance(Rectangle(1, 2), Base)

    def test_noarg(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_1arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_2args(self):
        rec1 = Rectangle(1, 2)
        rec2 = Rectangle(2, 3)
        self.assertEqual(rec1.id, rec2.id - 1)

    def test_3args(self):
        rec1 = Rectangle(1, 2, 3)
        rec2 = Rectangle(2, 3, 4)
        self.assertEqual(rec1.id, rec2.id - 1)

    def test_4args(self):
        rec1 = Rectangle(1, 2, 3, 4)
        rec2 = Rectangle(2, 3, 4, 5)
        self.assertEqual(rec1.id, rec2.id - 1)

    def test_5args(self):
        self.assertEqual(7, Rectangle(10, 2, 0, 0, 7).id)

    def test_above5args(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_wpriv(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 3, 0, 0, 3).__width)

    def test_hpriv(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 3, 0, 0, 3).__height)

    def test_xpriv(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 3, 0, 0, 3).__x)

    def test_ypriv(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 3, 0, 0, 3).__y)

    def test_wgetter(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(1, r.width)

    def test_wsetter(self):
        rec = Rectangle(1, 7, 7, 5, 1)
        rec.width = 5
        self.assertEqual(5, rec.width)

    def test_hgetter(self):
        rec = Rectangle(1, 6, 8, 4, 9)
        self.assertEqual(6, rec.height)

    def test_hsetter(self):
        rec = Rectangle(1, 6, 8, 4, 9)
        rec.height = 4
        self.assertEqual(4, rec.height)

    def test_xgetter(self):
        rec = Rectangle(1, 2, 5, 7, 1)
        self.assertEqual(5, rec.x)

    def test_xsetter(self):
        rec = Rectangle(1, 2, 3, 5, 1)
        rec.x = 0
        self.assertEqual(0, rec.x)

    def test_ygetter(self):
        rec = Rectangle(1, 2, 3, 4, 1)
        self.assertEqual(4, rec.y)

    def test_ysetter(self):
        rec = Rectangle(1, 2, 3, 4, 1)
        rec.y = 0
        self.assertEqual(0, rec.y)


class TestRectangle_width(unittest.TestCase):
    """Unittests for testing initialization of Rectangle width attribute."""

    def test_Nowidth(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 1)

    def test_strwidth(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("ja", 1)

    def test_flwidth(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(2.45, 1)

    def test_negw(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-11, 1)

    def test_z(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 1)


class TestRectangle_height(unittest.TestCase):
    """Unittests for testing initialization of Rectangle height attribute."""

    def test_Nh(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, None)

    def test_strh(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "aj")

    def test_flh(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, 6.9)

    def test_nh(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -13)

    def test_zh(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)


class TestRectangle_x(unittest.TestCase):
    """Unittests for testing initialization of Rectangle x attribute."""

    def test_Nx(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, None)

    def test_stx(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "ka", 3)

    def test_flx(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, 4.2, 3)

    def test_negx(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 2, -1, 4)


class TestRectangle_y(unittest.TestCase):
    """Unittests for testing initialization of Rectangle y attribute."""

    def test_Ny(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, None)

    def test_stry(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, "ak")

    def test_fly(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, 9.6)

    def test_negy(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 2, 3, -1)


class TestRectangle_order_of_initialization(unittest.TestCase):
    """Unittests for testing Rectangle order of attribute initialization."""

    def test_wbh(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("h", "night")

    def test_wbx(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("wrwr", 2, "bee")

    def test_wby(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("wr", 2, 3, "wev")

    def test_hbx(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "wce", "wb")

    def test_hby(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "ev", 2, "brt")

    def test_xby(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "asd", "wec")


class TestRectangle_area(unittest.TestCase):
    """Unittests for testing the area method of the Rectangle class."""

    def test_ar1(self):
        rec = Rectangle(1, 2, 0, 0, 0)
        self.assertEqual(2, rec.area())

    def test_ar2(self):
        rec = Rectangle(10000000000, 10000000000, 0, 0, 1)
        self.assertEqual(100000000000000000000, rec.area())

    def test_armod(self):
        rec = Rectangle(1, 1, 1, 1, 1)
        rec.width = 10
        rec.height = 10
        self.assertEqual(100, rec.area())

    def test_aarg(self):
        rec = Rectangle(4, 6, 0, 0, 1)
        with self.assertRaises(TypeError):
            rec.area(3)


class TestRectangle_stdout(unittest.TestCase):
    """Unittests for testing __str__ and display methods of Rectangle class."""

    @staticmethod
    def getstd(rec, meth):
        """gets and returns text printed to stdout.

        Args:
            rec (Rectangle): The Rectangle to print to stdout.
            meth (str): The method to run on rect.
        Returns:
            The text printed to stdout by calling method on sq.
        """
        getit = io.StringIO()
        sys.stdout = getit
        if meth == "print":
            print(rec)
        else:
            rec.display()
        sys.stdout = sys.__stdout__
        return getit

    # Test __str__ method
    def test_strwh(self):
        r = Rectangle(1, 2)
        getit = TestRectangle_stdout.getstd(r, "print")
        yees = "[Rectangle] ({}) 0/0 - 1/2\n".format(r.id)
        self.assertEqual(yees, getit.getvalue())

    def test_strwhx(self):
        r = Rectangle(2, 4, 2)
        yees = "[Rectangle] ({}) 2/0 - 2/4".format(r.id)
        self.assertEqual(yees, r.__str__())

    def test_strwhxy(self):
        r = Rectangle(3, 4, 9, 8)
        yees = "[Rectangle] ({}) 9/8 - 3/4".format(r.id)
        self.assertEqual(yees, str(r))

    def test_strwhxyid(self):
        r = Rectangle(34, 88, 4, 6, 7)
        self.assertEqual("[Rectangle] (7) 4/6 - 34/88", str(r))

    # Test display method
    def test_dwh(self):
        r = Rectangle(3, 2, 0, 0, 0)
        getit = TestRectangle_stdout.getstd(r, "display")
        self.assertEqual("###\n###\n", getit.getvalue())

    def test_dwhx(self):
        r = Rectangle(3, 2, 1, 0, 1)
        getit = TestRectangle_stdout.getstd(r, "display")
        self.assertEqual(" ###\n ###\n", getit.getvalue())

    def test_dwhy(self):
        r = Rectangle(4, 5, 0, 1, 0)
        getit = TestRectangle_stdout.getstd(r, "display")
        dis = "\n####\n####\n####\n####\n####\n"
        self.assertEqual(dis, getit.getvalue())

    def test_dwhxy(self):
        r = Rectangle(2, 4, 3, 2, 0)
        getit = TestRectangle_stdout.getstd(r, "display")
        dis = "\n\n   ##\n   ##\n   ##\n   ##\n"
        self.assertEqual(dis, getit.getvalue())

    def test_display_one_arg(self):
        r = Rectangle(12, 44, 2, 2, 9)
        with self.assertRaises(TypeError):
            r.display(1)


class TestRectangle_update_args(unittest.TestCase):
    """Unittests for testing update args method of the Rectangle class."""

    def test_uzero(self):
        r = Rectangle(1, 1, 1, 1, 1)
        r.update()
        self.assertEqual("[Rectangle] (1) 1/1 - 1/1", str(r))

    def test_uone(self):
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(9)
        self.assertEqual("[Rectangle] (9) 1/1 - 1/1", str(r))

    def test_utwo(self):
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(9, 2)
        self.assertEqual("[Rectangle] (9) 1/1 - 2/1", str(r))

    def test_uthree(self):
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(9, 2, 3)
        self.assertEqual("[Rectangle] (9) 1/1 - 2/3", str(r))

    def test_ufour(self):
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(9, 2, 3, 4)
        self.assertEqual("[Rectangle] (9) 4/1 - 2/3", str(r))

    def test_ufive(self):
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(9, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (9) 4/5 - 2/3", str(r))

    def test_umorefive(self):
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(9, 2, 3, 4, 5, 6)
        self.assertEqual("[Rectangle] (9) 4/5 - 2/3", str(r))


class TestRectangle_update_kwargs(unittest.TestCase):
    """Unittests for testing update kwargs method of the Rectangle class."""

    def test_ukone(self):
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(id=11)
        self.assertEqual("[Rectangle] (11) 1/1 - 1/1", str(r))

    def test_uktwo(self):
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(width=3, id=11)
        self.assertEqual("[Rectangle] (11) 1/1 - 3/1", str(r))

    def test_ukthree(self):
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(width=4, height=5, id=9)
        self.assertEqual("[Rectangle] (9) 1/1 - 4/5", str(r))

    def test_ukfour(self):
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(id=9, x=0, height=5, y=0, width=3)
        self.assertEqual("[Rectangle] (9) 0/0 - 3/5", str(r))

    def test_ukfive(self):
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(y=0, x=0, id=9, width=3, height=4)
        self.assertEqual("[Rectangle] (9) 0/0 - 3/4", str(r))

    def test_ukinv(self):
        r = Rectangle(1, 1, 1, 1, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(width="iafhkd")

    def test_ukzerozero(self):
        r = Rectangle(1, 1, 1, 1, 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=0)

    def test_uknegative(self):
        r = Rectangle(1, 1, 1, 1, 1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(y=-44)

    def test_uargkwargs(self):
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(9, 3, height=22, y=32)
        self.assertEqual("[Rectangle] (9) 1/1 - 3/1", str(r))

    def test_ukwrongkey(self):
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(qw=3, rt=2)
        self.assertEqual("[Rectangle] (1) 1/1 - 1/1", str(r))

    def test_uksowro(self):
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(height=4, id=9, aa=1, ba=54, x=1, y=1)
        self.assertEqual("[Rectangle] (9) 1/1 - 10/4", str(r))


class TestRectangle_to_dictionary(unittest.TestCase):
    """Unittests for testing to_dictionary method of the Rectangle class."""

    def test_tdo(self):
        r = Rectangle(1, 1, 0, 0, 1)
        correct = {'x': 0, 'y': 0, 'id': 1, 'height': 1, 'width': 1}
        self.assertDictEqual(correct, r.to_dictionary())

    def test_tdnobjchan(self):
        r1 = Rectangle(77, 9, 0, 0, 8)
        r2 = Rectangle(11, 4, 12, 7, 9)
        r2.update(**r1.to_dictionary())
        self.assertNotEqual(r1, r2)

    def test_toarg(self):
        r = Rectangle(12, 3, 5, 7, 23)
        with self.assertRaises(TypeError):
            r.to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
