from routes.exception import NoRouteException
from routes.parser import Parser
from routes.route import Route
from tests.testcase import TestCase


class RouteTest(TestCase):
    def test_calculate(self):
        routes, nodes = Parser.parse(self.TEST_CSV)

        for case in [
            ('A', 'A', '(0, 0)'), ('A', 'B', '(0, 5)'),
            ('A', 'C', '(1, 10)'), ('A', 'D', '(0, 15)'),
            ('E', 'J', '(2, 30)')
        ]:
            cost = Route(routes, nodes).calculate(case[0], case[1])
            cost1 = Route(routes, nodes).calculate(case[1], case[0], True)
            self.assertEqual('{}'.format(cost), case[2])
            self.assertEqual('{}'.format(cost1), case[2])

    def test_calculate_raises(self):
        routes, nodes = Parser.parse(self.TEST_CSV)

        for case in [('A', 'E'), ('A', 'F'), ('A', 'G'), ('A', 'H'), ('A', 'I'), ('X', 'Y')]:
            with self.assertRaises(NoRouteException):
                Route(routes, nodes).calculate(case[0], case[1])
