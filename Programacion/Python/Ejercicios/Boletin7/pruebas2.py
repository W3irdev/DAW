"""11. Cuadrado de números:
Crea un programa que lea del teclado un número y genere un cuadrado con el patrón siguiente
donde cada elemento está separado por un espacio.
"""
total=""
num=7
numfix=num
figura=""
filas=0
matriz=[]
cuadrado=""
izquierdo=""
derecho=""
figurader=""
cuadradoder=""
numder=num
matrizcuadrado=[]
for i in range(num,0,-1):
    figura=(i-1)*(str(num)+" ")
    cuadrado+=f"{num} "
    num-=1
    izquierdo+=f"\n{cuadrado+figura}"
    matriz.append(cuadrado)
    matrizcuadrado.append(figura)

contador=numfix-1
cuadradoinverso=""
cuadradobajo=""
while contador >0:
    cuadradoinverso+=f"\n{matriz[contador-1]}{matrizcuadrado[contador-1]}"
    contador-=1


parte1=f"{izquierdo}{cuadradoinverso}"
parte2=""
contador2=len(parte1)
while contador2 >1:
    contador2-=1
    parte2+=parte1[contador2]
total=f"{parte1}{parte2}"
    

print(parte1)
print(parte2)


