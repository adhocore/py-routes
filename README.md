## adhocore/py-routes

A simple Python3 CLI app to find the optimal route between two points in terms of number of stops and duration.

It does not use Dijkstra's algorithm and has no external dependencies. It supports reverse traversal as well.

## FAQs

#### Why?
> It does not use Dijkstra's algorithm and has no external dependencies. It supports reverse traversal as well.

#### Do I know recursion is bad in Python?
> Yes, that's [why](#why).

---
### Structure

```
├── main.py             => The main CLI app
├── README.md           => The README (this file)
├── requirements.txt    => The Project deps definition (none)
├── routes              => The routes module
│   ├── __init__.py     => The Module init
│   ├── calculator.py   => The abstract route calculator
│   ├── cost.py         => The cost object
│   ├── decorator.py    => The reverse route decorator
│   ├── exception.py    => The container for exception
│   ├── option.py       => The argv option parser
│   ├── parser.py       => The routes.csv parser
│   ├── route.py        => The recursive ro
├── routes.csv          => The default input file with route info
└── tests               => The tests
    ├── __init__.py     => The Module init
    ├── cost_test.py    => The test for cost.py
    ├── main_test.py    => The test for main.py
    ├── option_test.py  => The test for option.py
    ├── parser_test.py  => The test for parser.py
    ├── route_test.py   => The test for route.py
    └── testcase.py     => The base testcase where we deal with CSV
```

### Usage

As a command line app, you can run it in shell:

```sh
# Show usage help
python3 main.py
# OR
python3 main.py --help
```

```
Usage:
  python main.py <options>

Options:
  <--file>     Path to csv file with route information
  <--start>    The starting point
  <--end>      The destination point
  [--two-way]  Check if the reverse route is possible
  [--help]     Show the help

Examples:
  python main.py --file=routes.csv --start=A --end=D
  python main.py --file routes.csv --start A --end D
  python main.py --file routes.csv --start D --end A --two-way

[Requires Python3.3+]
```

It interactively asks in the value for `start` and `end` points if you didn't pass them via shell.


#### Options

##### --start
Case insensitive start point.

##### --end
Case insensitive end point.

##### --file
We can use both relative (to this project root) or full path as file.
The file CSV is very flexible so can have all random stuffs in there like so:
```csv
"A", B,5
  B,"C",5
C,D ,7

A,D,"15"
 E, F,5
F,G, 5

G,H,10
XX,YY,10
```
Where the values in each row as `start,end,distance` i.e. `A,B,5` mean the distance between point `A` and `B` is `5`.

##### --two-way
And here is an option for power user. Suppose our input csv lacks elaborate routes for two way round trips, can pass in `--two-way` for reverse traversal.

> How it works?

```sh
python3 main.py --file=routes.csv --start=E --end=J           # Stops 2, Time 30
python3 main.py --file=routes.csv --start=J --end=E           # No routes
python3 main.py --file=routes.csv --start=J --end=E --two-way # Stops 2, Time 30
```

### Unit testing
```sh
python3 -m unittest discover -s tests -p '*_test.py'
```
