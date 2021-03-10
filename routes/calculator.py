from abc import ABC, abstractmethod

from routes.cost import Cost


class Calculator(ABC):
    def __init__(self, routes: dict, nodes: set):
        """Constructor

        Initialize route connections among points.

        Arguments:
          routes {dict} -- Deep nested dict with branch and time cost
          nodes {set}   -- Flat set with all available points
        """
        self.routes, self.nodes = routes, nodes

    @abstractmethod
    def calculate(self, start: str, end: str, twoway: bool = False) -> Cost:
        pass
