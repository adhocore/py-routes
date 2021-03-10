#!/usr/bin/env python

from sys import argv, exit

from routes.exception import NoRouteException, ParserException
from routes.option import Option
from routes.parser import Parser
from routes.route import Route


class Main:
    @staticmethod
    def usage() -> str:
        """Show help information and usage example"""
        return (
            '''
        Usage:
          python main.py <options>

        Options:
          <--file>     Path to csv file with route information
          <--start>    The starting point
          <--end>      The destination point
          [--two-way]  Check if the reverse route is possible
          [--recurse]  Use the recursive algorithm
          [--help]     Show the help

        Examples:
          python main.py --file=routes.csv --start=A --end=D
          python main.py --file routes.csv --start A --end D
          python main.py --file routes.csv --start D --end A --two-way

        [Requires Python3.3+]
            '''
            .replace('        ', '')
        )

    @staticmethod
    def run(options: dict) -> bool:
        """Run the app

        Run the CLI app using supplied options and print the result or error.

        Arguments:
            options {dict} -- The options dict with file, start, end props

        Returns:
            bool           -- True if success false otherwise
        """
        try:
            routes, nodes = Parser.parse(options['file'])
            route = Route(routes, nodes)
            cost = route.calculate(options['start'], options['end'], 'two-way' in options)
            print(
                'The route from {} to {} includes {} stops and will take {} minutes.'
                .format(options['start'], options['end'], cost.stops, cost.time)
            )

            return True
        except NoRouteException:
            print('No routes from {} to {}.'.format(options['start'], options['end']))

            return False
        except ParserException as e:
            print(e)

            return False


if __name__ == '__main__':

    opts = Option.parse(argv)
    if 'help' in opts or opts.get('file', '') == '':
        print(Main.usage())
        exit(0)

    while opts.get('start', '') == '':
        opts['start'] = input('What point are you getting on the train?: ')
    while opts.get('end', '') == '':
        opts['end'] = input('What point are you getting off the train?: ')

    code = 0 if Main.run(opts) else 1
    exit(code)
