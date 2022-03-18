import sys

if len(sys.argv) == 3:
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    if (num1 > 0 and num1 < 10 and num2 > 0 and num2 < 10):
        for f in range(num1):
            print("")
            for c in range(num2):
                print(" * ", end='')
    else:
        print("¡ERROR!, Valores incorrectos")
else:
    print("sugerencia: tabla.py 4 5")