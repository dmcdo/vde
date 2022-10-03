from sys import argv
import start


if __name__ == "__main__":
    _argv = argv[1:] if argv[0].startswith('python') else argv

    if len(_argv) < 2:
        raise RuntimeError('No container name provided')

    elif _argv[1][0] == "-":
        raise NotImplementedError()
    
    elif len(argv) > 2:
        raise NotImplementedError()
    
    else:
        start.start(_argv[1])
