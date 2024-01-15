#!/usr/bin/python3
"""Defines unittests for base.py.

Unittest classes:
    TestBase_instn - line 19
    TestBase_to_json_string - line 76
    TestBase_save_to_file - line 116
    TestBase_from_json_string - line 184
    TestBase_create - line 232
    TestBase_load_from_file - line 284
"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_instn(unittest.TestCase):
    """Unittests for testing instantiation of the Base class."""

    def test_noArg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_3Base(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_NoneId(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_uqueId(self):
        self.assertEqual(34, Base(34).id)

    def test_idPublic(self):
        b = Base(1)
        b.id = 36
        self.assertEqual(36, b.id)

    def test_nbInsPriv(self):
        with self.assertRaises(AttributeError):
            print(Base(89).__nb_instances)

    def test_strId(self):
        self.assertEqual("Mannie", Base("Mannie").id)

    def test_fltId(self):
        self.assertEqual(6.9, Base(6.9).id)

    def test_dicId(self):
        self.assertEqual({"M": 6, "F": 9}, Base({"M": 6, "F": 9}).id)

    def test_bo0Id(self):
        self.assertEqual(False, Base(False).id)

    def test_lstId(self):
        self.assertEqual([1, "cash", 4], Base([1, "cash", 4]).id)

    def test_tuId(self):
        self.assertEqual((0, 3), Base((0, 3)).id)

    def test_setId(self):
        self.assertEqual({3, 4, 5}, Base({3, 4, 5}).id)

    def test_2Args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)


class TestBase_to_json_string(unittest.TestCase):
    """Unittests for testing to_json_string method of Base class."""

    def test_tjs_rect_type(self):
        rec = Rectangle(9, 12, 4, 3, 8)
        self.assertEqual(str, type(Base.to_json_string([rec.to_dictionary()])))

    def test_tjsrect_1dict(self):
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertTrue(len(Base.to_json_string([r.to_dictionary()])) == 53)

    def test_tjs_rect_2dicts(self):
        rec1 = Rectangle(2, 3, 5, 19, 2)
        rec2 = Rectangle(4, 2, 4, 1, 12)
        list_dicts = [rec1.to_dictionary(), rec2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 106)

    def test_tjs_sqType(self):
        sq = Square(12, 5, 22, 8)
        self.assertEqual(str, type(Base.to_json_string([sq.to_dictionary()])))

    def test_tsq1dict(self):
        sq = Square(10, 2, 3, 4)
        self.assertTrue(len(Base.to_json_string([sq.to_dictionary()])) == 39)

    def test_tjs_sq2dicts(self):
        sq1 = Square(10, 2, 3, 4)
        sq2 = Square(4, 5, 21, 2)
        list_dicts = [sq1.to_dictionary(), sq2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 78)

    def test_tjs_noarg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_tjs_mult_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)


class TestBase_save_to_file(unittest.TestCase):
    """Unittests for testing save_to_file method of Base class."""

    @classmethod
    def dEl(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_stf_1r(self):
        rec = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([rec])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 53)

    def test_stf_2r(self):
        rec1 = Rectangle(10, 7, 2, 8, 5)
        rec2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([rec1, rec2])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 105)

    def test_stf_1sq(self):
        sq = Square(10, 7, 2, 8)
        Square.save_to_file([sq])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_stf_2sq(self):
        sq1 = Square(10, 7, 2, 8)
        sq2 = Square(8, 1, 2, 3)
        Square.save_to_file([sq1, sq2])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 77)

    def test_stfcls_name(self):
        sq = Square(10, 7, 2, 8)
        Base.save_to_file([sq])
        with open("Base.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_stf_ovw(self):
        sq = Square(9, 2, 39, 2)
        Square.save_to_file([sq])
        sq = Square(10, 7, 2, 8)
        Square.save_to_file([sq])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_stf_noargs(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_stf_multarg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)


class TestBase_from_json_string(unittest.TestCase):
    """Unittests for testing from_json_string method of Base class."""

    def test_fjs_type(self):
        ls = [{"id": 1, "width": 2, "height": 3}]
        js = Rectangle.to_json_string(ls)
        lso = Rectangle.from_json_string(js)
        self.assertEqual(list, type(lso))

    def test_fjs_1rec(self):
        ls = [{"id": 1, "width": 2, "height": 3, "x": 4}]
        js = Rectangle.to_json_string(ls)
        lso = Rectangle.from_json_string(js)
        self.assertEqual(ls, lso)

    def test_fjs_2rec(self):
        ls = [
            {"id": 1, "width": 2, "height": 3, "x": 4, "y": 5},
            {"id": 2, "width": 3, "height": 4, "x": 5, "y": 6},
        ]
        js = Rectangle.to_json_string(ls)
        lso = Rectangle.from_json_string(js)
        self.assertEqual(ls, lso)

    def test_fjs_1sq(self):
        ls = [{"id": 1, "size": 2, "height": 3}]
        js = Square.to_json_string(ls)
        lso = Square.from_json_string(js)
        self.assertEqual(ls, lso)

    def test_fjs_2sq(self):
        ls = [
            {"id": 1, "size": 2, "height": 3},
            {"id": 2, "size": 3, "height": 4}
        ]
        js = Square.to_json_string(ls)
        lso = Square.from_json_string(js)
        self.assertEqual(ls, lso)

    def test_fjs_nargs(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_fjs_multarg(self):
        with self.assertRaises(TypeError):
            Base.from_json_string([], 1)


class TestBase_create(unittest.TestCase):
    """Unittests for testing create method of Base class."""

    def test_crecto(self):
        rec1 = Rectangle(3, 5, 1, 2, 7)
        rec1_dict = rec1.to_dictionary()
        rec2 = Rectangle.create(**rec1_dict)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(rec1))

    def test_crecnew(self):
        rec1 = Rectangle(3, 5, 1, 2, 7)
        rec1_dict = rec1.to_dictionary()
        rec2 = Rectangle.create(**rec1_dict)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(rec2))

    def test_crecis(self):
        rec1 = Rectangle(4, 6, 2, 3, 8)
        rec1_dict = rec1.to_dictionary()
        rec2 = Rectangle.create(**rec1_dict)
        self.assertIsNot(rec1, rec2)

    def test_crecequ(self):
        rec1 = Rectangle(4, 6, 2, 3, 8)
        rec1_dict = rec1.to_dictionary()
        rec2 = Rectangle.create(**rec1_dict)
        self.assertNotEqual(rec1, rec2)

    def test_csqo(self):
        sq1 = Square(3, 5, 1, 7)
        sq1_dict = sq1.to_dictionary()
        sq2 = Square.create(**sq1_dict)
        self.assertEqual("[Square] (7) 5/1 - 3", str(sq1))

    def test_csqnew(self):
        sq1 = Square(3, 5, 1, 7)
        sq1_dict = sq1.to_dictionary()
        sq2 = Square.create(**sq1_dict)
        self.assertEqual("[Square] (7) 5/1 - 3", str(sq2))

    def test_csqis(self):
        sq1 = Square(9, 4, 8, 5)
        sq1_dict = sq1.to_dictionary()
        sq2 = Square.create(**sq1_dict)
        self.assertIsNot(sq1, sq2)

    def test_csqeq(self):
        sq1 = Square(9, 4, 8, 5)
        sq1_dict = sq1.to_dictionary()
        sq2 = Square.create(**sq1_dict)
        self.assertNotEqual(sq1, sq2)


class TestBase_load_from_file(unittest.TestCase):
    """Unittests for testing load_from_file_method of Base class."""

    @classmethod
    def dEl(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_lff_1rec(self):
        rec1 = Rectangle(1, 2, 3, 4, 5)
        rec2 = Rectangle(2, 3, 4, 5, 6)
        Rectangle.save_to_file([rec1, rec2])
        lreco = Rectangle.load_from_file()
        self.assertEqual(str(rec1), str(lreco[0]))

    def test_lff_2rec(self):
        rec1 = Rectangle(1, 2, 3, 4, 5)
        rec2 = Rectangle(2, 3, 4, 5, 6)
        Rectangle.save_to_file([rec1, rec2])
        lreco = Rectangle.load_from_file()
        self.assertEqual(str(rec2), str(lreco[1]))

    def test_lff_rectyp(self):
        rec1 = Rectangle(1, 2, 3, 4, 5)
        rec2 = Rectangle(2, 3, 4, 5, 6)
        Rectangle.save_to_file([rec1, rec2])
        o = Rectangle.load_from_file()
        self.assertTrue(all(type(obj) == Rectangle for obj in o))

    def test_lff_1sq(self):
        sq1 = Square(1, 2, 3, 4)
        sq2 = Square(2, 3, 4, 5)
        Square.save_to_file([sq1, sq2])
        lsqo = Square.load_from_file()
        self.assertEqual(str(sq1), str(lsqo[0]))

    def test_lff_2sq(self):
        sq1 = Square(1, 2, 3, 4)
        sq2 = Square(2, 3, 4, 5)
        Square.save_to_file([sq1, sq2])
        lsqo = Square.load_from_file()
        self.assertEqual(str(sq2), str(lsqo[1]))

    def test_lff_sqtyp(self):
        sq1 = Square(1, 2, 3, 4)
        sq2 = Square(2, 3, 4, 5)
        Square.save_to_file([sq1, sq2])
        oq = Square.load_from_file()
        self.assertTrue(all(type(obj) == Square for obj in oq))

    def test_lff_multarg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file([], 1)


if __name__ == "__main__":
    unittest.main()
