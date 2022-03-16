def suma(a, b):
    """
    Esta funcion recibe dos paremetros y devuelve la suma de ambos

    pueden ser numeros:
    
    >>> suma(0,0)
    0

    >>> suma(-5, 7)
    2

    Cadenas de texto:

    >>> suma('bb', 'nn')
    'bbnn'

    O listas:

    >>> a = [1,2,3]
    >>> b = [4,5,6]
    >>> suma(a,b)
    [1, 2, 3, 4, 5, 6]

    Sumar distintos tipos:

    >>> suma(10, "hola")
    Traceback (most recent call last):
      ...
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    
    """
    return a+b

if __name__== "__main__":
    import doctest
    doctest.testmod()