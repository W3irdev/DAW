"""11. Cuadrado de números:
Crea un programa que lea del teclado un número y genere un cuadrado con el patrón siguiente
donde cada elemento está separado por un espacio.
"""

try:
    num=int(input("Introduzca numero 1-9 para generar el patron (Ejecute 0 para salir): "))

    while num < 0 or num > 9:
        num=int(input("Introduzca numero 1-9 para generar el patron (Ejecute 0 para salir): "))

    while num > 0:

        numfix=num
        figura=""
        matriz=[]
        cuadrado=""
        izquierdo=""
        matrizcuadrado=[]
        cuadrado2=""
        matrizcuadrado2=[]
        for i in range(num,0,-1):
            figura=(i-1)*(str(num)+" ")
            cuadrado+=f"{num} "
            matriz.append(cuadrado)
            matrizcuadrado.append(figura)
            matrizcuadrado2.append(cuadrado2)
            
            num-=1
            izquierdo+=f"\n{cuadrado+figura*2+cuadrado2}"
            if i == 1:
                pass
            else:
                cuadrado2=str(i)+" "+cuadrado2

        contador=numfix-1
        cuadradoinverso=""
        cuadradobajo=""
        while contador >0:
            cuadradoinverso+=f"\n{matriz[contador-1]}{2*matrizcuadrado[contador-1]}{matrizcuadrado2[contador-1]}"
            contador-=1


        total=f"{izquierdo}{cuadradoinverso}"

        print(total)
        num=int(input("Introduzca numero 1-9 para generar el patron (Ejecute 0 para salir): "))
except:
    print("No puede dejar en blanco el dato")