def test(times):
    """
    Prints Hello
    :param times:
    """
    try:
        i: int
        for i in range(times):
            print('Hello')
            input()
    except TypeError:
        print('Please enter an int')

test(5)