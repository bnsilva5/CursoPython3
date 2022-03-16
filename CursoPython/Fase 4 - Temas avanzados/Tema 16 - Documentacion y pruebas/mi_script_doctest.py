def suma(a, b):
    """
    La funcion suma(a, b) recibe dos parametros a y b.
    Devuelve la suma de los dos
    
    >>> suma(5, 10)
    15

    >>> suma(0,0)
    0

    >>> suma(-5, 7)
    2
    """
    return a+b

if __name__== "__main__":
    import doctest
    doctest.testmod()