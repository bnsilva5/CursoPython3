import sys

if len(sys.argv) == 2:
    print("Entra primer if")
    numero = int(sys.argv[1])
    if (numero > 1):
        print("Segundo if")
    else:
        print("Escriba un numero entero positivo")
else:
    print("sugerencia: descomposicion.py [1-]")