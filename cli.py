from sys import argv
import start


if __name__ == '__main__':
    _argv = argv[1:] if argv[0].startswith('python') else argv
    print(_argv)

    subcmd = _argv[1]

    if subcmd.lower() in ('interact', 'x'):
        start.start(_argv[2])

    elif subcmd.lower() in ('start', 's'):
        raise NotImplementedError()

    elif subcmd.lower() in ('stop', 'h'):
        raise NotImplementedError()

    elif subcmd.lower() in ('install', 'i'):
        raise NotImplementedError()

    elif subcmd.lower() in ('download', 'w'):
        raise NotImplementedError()

    elif subcmd.lower() in ('acrhive', 'a'):
        raise NotImplementedError()

    elif subcmd.lower() in ('create', 'c'):
        raise NotImplementedError()

    elif subcmd.lower() in ('delete', 'd'):
        raise NotImplementedError()

    elif subcmd.lower() in ('send-file'):
        raise NotImplementedError()

    elif subcmd.lower() in ('get-file'):
        raise NotImplementedError()

    elif subcmd.lower() in ('add-repo'):
        raise NotImplementedError()

    elif subcmd.lower() in ('remove-repo'):
        raise NotImplementedError()

    elif subcmd.lower() in ('update-repo'):
        raise NotImplementedError()
