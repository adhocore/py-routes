from sys import maxsize

from routes.calculator import Calculator
from routes.cost import Cost
from routes.decorator import reverse


class Route(Calculator):
    """Calculate route between two points

    It implements recursion on branch paths to calculate the overall cost.
    """

    @reverse
    def calculate(self, start: str, end: str, reverse: bool = False) -> Cost:
        """Calculate route cost

        Calculate route between two points using recursion on branch paths.

        Arguments:
          start {string}   -- The start point
          end {string}     -- The end point

        Keyword Arguments:
          reverse {bool}   -- Whether to perform reverse lookup (default: {False})

        Returns:
          Cost             -- Best cost route in terms of stops and total duration

        Raises:
          NoRouteException -- When the end point is not reachable
        """
        start, end = start.upper(), end.upper()

        if start == end:
            return Cost(0, 0)

        # We start with number of stops as -1 to account for recursive increment on each depth
        return self.cost(start, end, -1, 0, Cost(maxsize, maxsize), {start: 1})

    def cost(self, path: str, end: str, stops: int, time: int, best: Cost, visited: dict) -> Cost:
        """Find best cost of a branch path

        Arguments:
          path {string} -- Start branch point
          end {string}  -- Target point
          stops {int}   -- Stops from the start path
          time {int}    -- Time from the start path
          best {Cost}   -- Best cost so far

        Returns:
          Cost          -- Best cost route in terms of stops and total duration
        """
        if path == end:
            return Cost(stops, time)
        if path not in self.routes:
            return Cost(0, maxsize)

        visited[path] = 1
        for to, dist in self.routes[path].items():
            if to not in visited:
                best = min(best, self.cost(to, end, stops + 1, time + dist, best, visited))

        return best
