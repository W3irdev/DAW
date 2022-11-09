#Pide al usuario dos pares de números x1,y2 y x2,y2, que representen dos puntos en el plano.
#Calcula y muestra la distancia entre ellos.
import math

x1=int(input("Introduzca x1: "))
y1=int(input("Introduzca y1: "))
x2=int(input("Introduzca x2: "))
y2=int(input("Introduzca y2: "))

pun1=[x1,y1]
pun2=[x2,y2]
d=math.dist(pun1,pun2)
#print(f"La distancia entre el punto {pun1} y {pun2} es {d}")
print(f"La distancia entre el punto {pun1} y {pun2} es {((x2-x1)**2+(y2-y1)**2)**0.5:.2f}")