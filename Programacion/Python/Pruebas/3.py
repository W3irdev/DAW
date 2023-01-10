
def get_posicion_eq_valor(lista):
    lista_nueva=[]
    contador=0
    for posicion in lista:
        if lista.index(posicion)==posicion:
            lista_nueva.append(posicion)
            lista[contador]=" "
            contador+=1
        else:
            lista[contador]=" "
            contador+=1

    return lista_nueva

assert(get_posicion_eq_valor([1,1,3,5,4])==[1,4])

def obtener_frecuencia(lista):
    numeros=[]
    contador=1
    mensaje=""
    for i in lista:
        contador=1
        if i not in numeros:
            numeros.append(i)
        elif i in numeros:
            contador+=1
        
        mensaje+=f"El numero {i} ha aparecido {contador} veces \n"

    return mensaje

print(obtener_frecuencia([1,1,3,4,5,6,6,6,7,8,9]))

def dame_numero(longitud):
    from random import randint
    lista_numeros=[]
    for i in range(longitud):
        lista_numeros+=[randint(0,100)]


    return lista_numeros

print(get_posicion_eq_valor(dame_numero(10)))

