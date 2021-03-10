from routes.cost import Cost
from tests.testcase import TestCase


class TestCost(TestCase):
    def test_init(self):
        cost = Cost(1, 10)
        self.assertEqual(cost.stops, 1)
        self.assertEqual(cost.time, 10)

    def test_repr(self):
        cost = Cost(2, 15)
        other = Cost(2, 10)
        self.assertEqual('{}'.format(cost), '(2, 15)')
        self.assertEqual(other.__repr__(), '(2, 10)')

    def test_lt(self):
        cost = Cost(2, 15)
        other = Cost(2, 10)
        other1 = Cost(2, 15)
        other2 = Cost(1, 15)

        self.assertTrue(other < cost)
        self.assertFalse(cost < other)
        self.assertFalse(cost < other1)
        self.assertFalse(other1 < cost)
        self.assertFalse(cost < other2)
        self.assertTrue(other2 < cost)
