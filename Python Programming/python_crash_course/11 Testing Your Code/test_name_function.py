import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """ Tests for 'name_function.py'."""
    def test_name(self):
        """Do names like 'Ananta Asim' work?"""
        formatted_name = get_formatted_name('ananta','asim')
        self.assertEqual(formatted_name,'Ananta Asim')
unittest.main()