"""Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los
lados de un triángulo. El programa debe determinar que tipo de triangulo es, teniendo en
cuenta los siguiente:
◦ Si se cumple Pitágoras entonces es triángulo rectángulo
◦ Si sólo dos lados del triángulo son iguales entonces es isósceles.
◦ Si los 3 lados son iguales entonces es equilátero.
◦ Si no se cumple ninguna de las condiciones anteriores, es escaleno.
"""


try:
    a=int(input("Introduce lado A: "))
    b=int(input("Introduce lado B: "))
    c=int(input("Introduce lado C: "))

    while a >0 and b >0 and c>0:
        if (a**2)+(b**2)==(c**2) or (b**2)+(c**2)==(a**2) or (c**2)+(b**2)==(a**2):
            print("El triangulo es rectangulo")
        elif a==b!=c or b==c!=a or c==a!=b:
            print("El triangulo es isosceles")
        elif a==b==c:
            print("El triangulo es equilatero")
        else:
            print("El triangulo es escaleno")
    else:
        print("Introduce numeros positivos y mayor a 0")

except:
    print("Introduce valores correctos y positivos")