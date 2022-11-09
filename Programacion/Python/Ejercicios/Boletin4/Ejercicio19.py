"""19. Escribe un programa que dados dos números, uno real (base) y un entero positivo
(exponente), saque por pantalla el resultado de la potencia. No se puede utilizar el operador
de potencia."""
import math
base=int(input("Introduzca base "))
exponente=int(input("Introduzca exponente "))
total=1
for i in range(exponente):
    total=total*base
print(f"{base} elevado a {exponente} es {total}")