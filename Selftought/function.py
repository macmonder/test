from csv import excel

from pip._vendor.distlib.compat import raw_input
from setuptools.command.test import test


def test(times):
    """
    Prints Hello
    :param times:
    """
    try:
        i: int
        for i in range(times):
            print('Hello')
            raw_input('Enter')
    except TypeError:
        print('Please enter an int')
        
test(test)
