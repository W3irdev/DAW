#Calcular la media de tres números pedidos por teclado

from statistics import mean


num1=int(input("Introduzca primer numero: "))
num2=int(input("Introduzca segundo numero: "))
num3=int(input("Introduzca tercer numero: "))
lista=[num1, num2, num3]
calculo=num1+num2+num3
media = (calculo)/3

print(f"la media aritmetica de {lista} es {media}")

