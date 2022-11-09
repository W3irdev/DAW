#Pide al usuario dos números y muestra la "distancia" entre ellos (el valor absoluto de su
#diferencia, de modo que el resultado sea siempre positivo).


num1=int(input("Introduzca primer valor: "))
num2=int(input("Introduzca segundo valor: "))
distancia=num1-num2
total=(distancia*(-1))
if distancia <0:
    print(f"La distancia entre A y B, es {total}")
else:
    print(f"La distancia entre A y B es {distancia}")