import io
import sys

from main import Main
from tests.testcase import TestCase


class TestMain(TestCase):
    def test_usage(self):
        usage = Main.usage()

        self.assertIn('<--file>', usage)
        self.assertIn('<--start>', usage)
        self.assertIn('<--end>', usage)
        self.assertIn('[--two-way]', usage)

    def test_run_invalid(self):
        intercept = io.StringIO()
        sys.stdout = intercept

        self.assertFalse(Main.run({'file': ''}))
        self.assertIn('The route file path is not valid', intercept.getvalue())

        self.assertTrue(Main.run({'file': self.TEST_CSV, 'start': 'A', 'end': 'B'}))
        self.assertIn('The route from A to B includes 0 stops and will take 5 minutes.', intercept.getvalue())

        sys.stdout = sys.__stdout__
