from fractions import Fraction
numerador = int(input("Ingrese el númerador "))
denominador = int(input("Ingrese el denominador "))
# print(Fraction(numerador/denominador))
casosADividir = int(input("Ingrese la opción requerida, solo hay ocho opciones desde el 2 al 19 "))

if casosADividir == 1:
    numerador = numerador/2
    denominador = denominador/2
    print((int)(numerador))
    print('-')
    print((int)(denominador))
elif casosADividir == 2:
    numerador = numerador/3
    denominador = denominador/3
    print((int)(numerador))
    print('-')
    print((int)(denominador))
elif casosADividir == 3:
    numerador = numerador/5
    denominador = denominador/5
    print((int)(numerador))
    print('-')
    print((int)(denominador))
elif casosADividir == 4:
    numerador = numerador/7
    denominador = denominador/7
    print((int)(numerador))
    print('-')
    print((int)(denominador))
elif casosADividir == 5:
    numerador = numerador/11
    denominador = denominador/11
    print((int)(numerador))
    print('-')
    print((int)(denominador))
elif casosADividir == 6:
    numerador = numerador/13
    denominador = denominador/13
    print((int)(numerador))
    print('-')
    print((int)(denominador))
elif casosADividir == 7:
    numerador = numerador/17
    denominador = denominador/17
    print((int)(numerador))
    print('-')
    print((int)(denominador))
elif casosADividir == 8:
    numerador = numerador/19
    denominador = denominador/19
    print((int)(numerador))
    print('-')
    print((int)(denominador))
    