# def baz():
#    return ('bar' if foo() else qux())

def baz():
    if foo():
        return 'bar'
    else:
        return qux()