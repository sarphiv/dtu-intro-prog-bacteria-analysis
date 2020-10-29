from sys import stderr


def eprint(*args, **kwargs):
    """
    Passes arguments and keyword argumenst to the "print"-function,
    and then redirects the output to "stderr".
    """
    print(*args, file=stderr, **kwargs)
