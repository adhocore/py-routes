class Cost(object):
    """Represents a route cost

    The cost is number of stops and total time taken.
    """

    def __init__(self, stops: int, time: int):
        """Constructor

        Arguments:
          stops {int} -- Num of stops
          time  {int} -- Total time taken
        """
        self.stops, self.time = stops, time

    def __repr__(self) -> str:
        """String representation of Cost"""
        return '({}, {})'.format(self.stops, self.time)

    def __lt__(self, other: 'Cost') -> bool:
        """Compares if the Cost is better than other

        A cost is better than the other if:
          - The time is less than other; OR
          - The time is same but number of stops is less than other

        Arguments:
          other: {Cost} -- The other Cost

        Returns:
          bool          -- True if less than the other
        """
        return True if self.time < other.time else self.time == other.time and self.stops < other.stops
