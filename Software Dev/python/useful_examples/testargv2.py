"collect command-line options in a dictionary"


def getopts(argv_):
    opts = {}
    while argv_:
        if argv_[0][0] == '-':  # find "-name value" pairs
            opts[argv_[0]] = argv_[1]  # dict key is "-name" arg
            argv_ = argv_[2:]
        else:
            argv_ = argv_[1:]
    return opts


if __name__ == '__main__':
    from sys import argv  # example client code
    MYARGS = getopts(argv)
    if '-i' in MYARGS:
        print(MYARGS['-i'])
    print(MYARGS)
