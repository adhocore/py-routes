from os import path
from re import findall

from routes.exception import ParserException


class Parser(object):
    """Parses a CSV file

    Parse CSV file and prepare route dict and nodes.
    """

    @staticmethod
    def parse(file: str) -> (dict, set):
        """Parse CSV file and extract route info

        Arguments:
          file {string}   -- CSV file path

        Returns:
          dict            -- Route dict with branch cost and nodes

        Raises:
          ParserException -- When file path or file data is invalid
        """
        if file == '' or not path.isfile(file):
            raise ParserException('The route file path is not valid: ' + file)

        routes, nodes = {}, []

        with open(file, 'r') as csv:
            for line in csv:
                row = Parser.row(line)
                if len(row) < 3 or not row[2].isdigit():
                    continue

                nodes.extend([col for i, col in enumerate(row) if i < 2])
                if row[0] not in routes:
                    routes[row[0]] = {}
                routes[row[0]][row[1]] = int(row[2])

        if not nodes:
            raise ParserException('The route file does not contain valid route data')

        return routes, set(nodes)

    @staticmethod
    def row(line: str) -> list:
        """Parse a CSV row

        Parses and normalizes given line as CSV row accounting for quotes.

        Arguments:
          line {str} -- The CSV string

        Returns:
          list       -- The 0 indexed list of CSV columns
        """
        regex = '(?:^|,)(?=[^"]|(")?)"?((?(1)[^"]*|[^,"]*))"?(?=,|$)'

        # Grep the normalized columns
        return [cols[1].strip().upper() for cols in findall(regex, line)]
