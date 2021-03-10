class Option(object):
    """CLI Option parser

    Parses all or picks an option value by its name from a long argv list.
    """

    @staticmethod
    def pick(args: list, opt: str) -> str:
        """Pick option by name

        Picks an option value by its name from a long argv list.

        Arguments:
          args {list}  -- Argv list
          opt {string} -- Option name

        Returns:
          string       -- Option value
        """
        arlen = len(args)
        for i in range(arlen):
            if args[i] == opt:
                return args[i + 1] if i + 1 < arlen and args[i + 1][:2] != '--' else ''

            if args[i].startswith(opt + '='):
                return args[i][len(opt) + 1:]

        return ''

    @staticmethod
    def parse(args: list) -> dict:
        """Parse argv options once and for all

        Parse argv options once and for all as a dict. The option value can be accessed by it's name.
        The unnamed arguments list can be accessed by `--`: (Option.parse()['--'])

        Arguments:
          args {list} -- Argv list

        Returns:
          dict        -- Named opt: value dict
        """
        opt, opts, arlen = None, {'--': []}, len(args)
        for i in range(arlen):
            if args[i].startswith('--'):
                opt = args[i][2:]
                if '=' in opt:
                    opt, val = opt.split('=')
                    opts[opt], opt = val, None
                else:
                    opts[opt] = ''

            elif opt is not None:
                opts[opt], opt = args[i], None

            elif i > 0:
                opts['--'].extend([args[i]])

        return opts
