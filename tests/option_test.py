from routes.option import Option
from tests.testcase import TestCase


class TestOption(TestCase):
    def test_pick(self):
        args = ['--this', 'value', '--that-thing=that-value', '--x', '--y', 'yo']

        self.assertEqual(Option.pick(args, '--this'), 'value')
        self.assertEqual(Option.pick(args, '--that-thing'), 'that-value')
        self.assertEqual(Option.pick(args, '--x'), '')
        self.assertEqual(Option.pick(args, '--y'), 'yo')
        self.assertEqual(Option.pick([], 'z'), '')

    def test_parse(self):
        args = ['--this', 'value', '--that-thing=that-value', '--x', '--y', 'yo', 'arg1', 'arg2']
        options = Option.parse(args)

        self.assertEqual(options.get('this'), 'value')
        self.assertEqual(options.get('that-thing'), 'that-value')
        self.assertTrue('x' in options)
        self.assertTrue(options['y'], 'yo')
        self.assertEqual(['arg1', 'arg2'], options['--'])
