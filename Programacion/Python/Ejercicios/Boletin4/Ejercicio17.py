"""Escribir un programa que imprima todos los números pares entre dos números que se le
pidan al usuario"""

num1=int(input("Introduzca primer numero: "))
num2=int(input("Introduzca segundo numero: "))

try:
    if num1 < num2:
        for i in range(num1,num2):
            pares=i%2
            if pares == False:
                print(i)
    else: print("El primer numero debe ser mayor al segundo")

except:
    print("Introduzca dos numeros")