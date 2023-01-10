menu="""
1. Apostar.
2. Añadir mas saldo.
3. Mostrar saldo
4. Retirarse.

"""

def dame_numero():
    from random import randint
    return randint(0,12)

opcion="0"
saldo=0
apuesta=-1
numero_apuesta=0
#Obligamos a aumentar el saldo, para empezar a jugar
while saldo <1:
    saldo=int(input("¿Cuanto saldo desea introducir?: "))
while opcion!="4":
    jugada=dame_numero()
    apuesta=-1
    print(menu)
    opcion=input("Elige opcion del menu: ")
    if opcion=="1":
        #Hacemos la apuesta, si apuesta 0, la jugada no se realizara
        while apuesta <0:
            apuesta=float(input("¿Cuanto va a apostar?: "))
            saldo=saldo-apuesta
        while numero_apuesta>1 and numero_apuesta <13:
            numero_apuesta=int(input("¿Que numero apuesta?: "))
        if jugada==numero_apuesta:
            print(f"El numero de dados suma {jugada}")
            saldo=saldo+(apuesta*2)
        elif jugada<numero_apuesta:
            saldo=saldo+(apuesta/2)
            print(f"El numero de dados suma {jugada}")
        else:
            print(f"El numero de dados suma {jugada}")
    #Almacenamos en saldo, la cantidad de la recarga
    elif opcion=="2":
        recarga=-1
        while recarga<0:
            recarga=int(input("¿Cuanto desea recargar?: "))
        saldo+=recarga
    #Mostramos saldo
    elif opcion=="3":
        print(f"tiene de saldo {saldo}€")

