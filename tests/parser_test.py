from routes.parser import Parser, ParserException
from tests.testcase import TestCase


class TestParser(TestCase):
    def test_parse(self):
        routes, nodes = Parser.parse(self.TEST_CSV)

        self.assertEqual(8, len(routes))
        self.assertIn('A', routes)
        self.assertNotIn('D', routes)
        self.assertIn('B', routes['A'])
        self.assertEqual(15, routes['A']['D'])
        self.assertEqual(5, routes['I']['J'])

        self.assertEqual(10, len(nodes))
        self.assertIn('D', nodes)

    def test_row(self):
        row = Parser.row('A , B, 10')
        row1 = Parser.row('A ,"b,c"')

        self.assertEqual(3, len(row))
        self.assertEqual(['A', 'B', '10'], row)
        self.assertEqual(2, len(row1))
        self.assertEqual(['A', 'B,C'], row1)

    def test_parse_raises(self):
        with self.assertRaises(ParserException):
            Parser.parse('')

        with self.assertRaises(ParserException):
            Parser.parse('rand/file')
