#Realizar un algoritmos que lea un número y que muestre su raíz cuadrada y su raíz cúbica.
#Python no tiene ninguna función predefinida que permita calcular la raíz cúbica, ¿cómo se
#puede calcular?
#La raiz cubica se puede calcular elevando un numero a la division de 1/3

import math
num=int(input("Introduzca numero: "))

rq = math.sqrt(num)
rc = num**(1/3)

"""
print(f"La raiz cuadrada de {num} es {rq}")
print(f"La raiz cubica de {num} es {rc}")"""

print(f"La raiz cuadrada de {num} es {num**0.5}")
print(f"La raiz cubica de {num} es {rc}")