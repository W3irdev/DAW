from operator import invert


nombre="Alejandra"
normal=""
invertido=""
# Ejemplo 1: for sin indice
for c in nombre:
    invertido= c + invertido

print(invertido)

normal, invertido = "",""
#Ejemplo 2: for con indice
for i in range(len(nombre)):
    normal = normal + nombre[i]
    invertido= nombre[i]+invertido

print(invertido)

invertido, posicion= 0
#Ejemplo 3: While
while posicion < len(nombre):
    normal=normal+nombre[posicion]
    invertido=nombre[posicion]+invertido
    posicion+=1
print(posicion)

#_______________________________________________________________________

  

mensaje=""
for i in range(1, 15):
    mensaje=mensaje+str(i)
    if i <14:
        mensaje+=", "

    #es lo mismo que --> #mensaje = mensaje +str(i) (" , " if i < 14 else "")

print(mensaje)

#__________________________________________________________________________

#En f"{num:.2}"" (esto te coge solo las dos ultimos decimales)
#En f"{textoNumero:#<20}" te añade # cantidad a la izquierda, para cambiar de lugar es ^entre > a la derecha

#con dir(cosaaanalizar) nos enseña las funciones disponibles

#Trucazo
print([i for i in range(20)])