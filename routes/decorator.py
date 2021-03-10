from sys import maxsize

from routes.cost import Cost
from routes.exception import NoRouteException


def reverse(func):
    """Reverse route decorator

    Attempts route calculation from the reverse (end to start) should the other way fail.

    Arguments:
      func {function}  -- Route.calculate method

    Returns:
      Cost             -- The best cost

    Raises:
      NoRouteException -- When the end point is not reachable
    """
    def inner(self, *args) -> Cost:
        best = func(self, *args)
        if best.time == maxsize:
            if len(args) > 2 and args[2]:
                return func(self, args[1], args[0], False)

            raise NoRouteException

        return best

    return inner
