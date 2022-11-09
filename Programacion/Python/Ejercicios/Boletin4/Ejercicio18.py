"""Escribe un programa que pida el limite inferior y superior de un intervalo. Si el límite
inferior es mayor que el superior lo tiene que volver a pedir.
A continuación se van introduciendo números hasta que introduzcamos el 0. Cuando termine
el programa dará las siguientes informaciones:
◦ La suma de los números que están dentro del intervalo (intervalo abierto).
◦ Cuantos números están fuera del intervalo.
◦ Informa si hemos introducido algún número igual a los límites del intervalo.
"""

try:
    inf=1
    sup=10
    suma=0
    contador=0
    num3=int(input("Introduzca un numero (introduce 0 para terminar el programa) "))
    igual=False
    if sup > inf:
        while num3!=0:
            if num3!=0:
                if num3 > inf and num3 < sup:
                    suma+=num3
                elif num3 > sup or num3 < inf:
                    contador+=1
                elif num3==sup or num3==inf:
                    igual=True
                num3=int(input("Introduzca un numero (introduce 0 para terminar el programa) "))
        print(f"La suma de los numeros dentro del intervalo es {suma}")
        print(f"{contador} numeros estan fuera del intervalo")
        if igual==True:
            print(f"Has introducido numeros que coinciden con el intervalo")
except:
    print("Introduzca valores")
