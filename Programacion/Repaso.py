import time
"""#1.
n=1
out=""
while n < 100:
    if n%13==0 and n%7==0:
       print(f"The number {n} is a multiple of 7 and 13")
    elif n%7==0:
        print(f"The number {n} is a multiple of 7")
    elif n%13==0:
        print(f"The number {n} is a multiple of 13")
    else:
        print(n)
    n+=1"""

"""2. Escribe una aplicación que pida la fecha actual (día y mes) y el hemisferio
(Norte/Sur) e indique en qué estación se encuentra:
a. Hemisferio Norte: Otoño (desde 23 Septiembre), Invierno (desde 21
diciembre), Primavera (desde 21 Marzo), Verano (desde 21 Junio).
b. Hemisferio Sur: Primavera (desde 23 Septiembre), Verano (desde 21
diciembre), Otoño (desde 21 Marzo), Invierno (desde 21 Junio).
Ahora modifica el programa, para que se ejecute en bucle, mientras la opcion sea 1, si opcion es 2, salimos del programa"""

"""opcion=1

while opcion==1:
    dia=int(input("Introduzca dia "))
    mes=input("Introduzca mes ").upper()
    hemi=input("Introduzca hemisferio ").upper()
    while (dia > 31 or dia < 1) or (mes not in("ENERO","FEBRERO","MARZO","ABRIL","MAYO","JUNIO","JULIO","AGOSTO","SEPTIEMBRE","OCTUBRE","NOVIEMBRE","DICIEMBRE")) or hemi not in("NORTE","SUR") :
        dia=int(input("Introduzca dia "))
        mes=input("Introduzca mes ").upper()
        hemi=input("Introduzca hemisferio ").upper()
    if (dia >=23 and mes == "SEPTIEMBRE") or (mes in ("OCTUBRE","NOVIEMBRE")) or (dia <21 and mes == "DICIEMBRE"):
        if hemi=="NORTE":
            estacion="Otoño"
        else:
            estacion="Primavera"
    elif (dia >=21 and mes == "DICIEMBRE") or (mes in ("ENERO","FEBRERO")) or (dia <21 and mes == "MARZO"):
        if hemi=="NORTE":
            estacion="Invierno"
        else:
            estacion="Verano"
    elif (dia >=21 and mes == "MARZO") or (mes in ("ABRIL","MAYO")) or (dia <21 and mes == "JUNIO"):
        if hemi=="NORTE":
            estacion="Primavera"
        else:
            estacion="Otoño"
    else:
        estacion="Verano"
        if hemi=="SUR":
            estacion="Invierno"

    print(f"\nLa estacion actual es {estacion}\n")

    opcion=int(input("Introduzca opcion\n1. Preguntar otra estacion\n2. Salir\n"))
salir=""
for i in range(5):
    salir="Saliendo"+i*"."
    time.sleep(0.5)

    print(salir,end="\r")"""

"""3. Crea un programa que dada una fecha en formato (dd-mm-yyyy), nos devuelva
cuántos días han transcurrido desde el 1 de enero de ese mismo año (considera que
puede tratarse de un año bisiesto)."""
"""programa=1
while programa==1:
    days=0
    month=0
    year=0
    total=0
    bisiesto=True
    while (days>31 or days <1) or (month >12 or month <1) or (year<1) or ((days>28 and month==2) and bisiesto==False):            
        fecha=input("Introduzca fecha en formato dd-mm-yyyy ")
        months=[31,28,31,30,31,30,31,31,30,31,30,31]
        days=int(fecha[0:2])
        month=int(fecha[3:5])
        year=int(fecha[6:10])
        bisiesto=((year %4==0) and (year%100!=0 or year%400==0))
    for i in range(month-1):
        total+=months[i]
    total+=days
    esbisiesto="no es bisiesto"
    if bisiesto and month >2:
        total+=1
    print(f"Han transcurrido {total} dias ")
    programa=int(input("Introduzca opcion\n1. Preguntar por otra fecha\n2. Salir\n"))
salir=""
for i in range(5):
    salir="Saliendo"+i*"."
    time.sleep(0.5)
    print(salir,end="\r")
"""

"""Design a program that asks for a set of numbers. After inputting each number, the
program should ask “Do you want to enter more numbers (Y/N)?”. If the answer is “Y”
the program asks for other numbers. When the user finishes to enter all the numbers,
the program should say which one is the smallest. The messages are the following:
“Enter one number:”
“Do you want to enter more number (Y/N)?”
“The smallest number is XX”
"""

"""programa="Y"
conjunto=[]
while programa=="Y":
    n=int(input())
    while n<0:
        n=int(input("Numero no puede ser menor de 0: "))
    conjunto.append(n)
    programa=input("Quieres seguir metiend numeros? Y/N ").upper()
    while programa not in("Y","N"):
        print("limitese solo a Y/N")
        programa=input("Quieres seguir metiend numeros? Y/N ").upper()
conjunto.sort()
print(f"El numero mas pequeño es {conjunto[0]}")
"""


"""La asociación de vinicultores tiene como política fijar un precio inicial al kilo de uva, la cual
se clasifica en tipos A y B, y además en tamaños 1 y 2. Cuando se realiza la venta del
producto, ésta es de un solo tipo y tamaño, se requiere determinar cuánto recibirá un
productor por la uva que entrega en un embarque, considerando lo siguiente: si es de tipo A,
se le cargan 20 céntimos al precio inicial cuando es de tamaño 1; y 30 céntimos si es de
tamaño 2. Si es de tipo B, se rebajan 30 céntimos cuando es de tamaño 1, y 50 céntimos
cuando es de tamaño 2. Realice un algoritmo para determinar la ganancia obtenida."""

"""pini=100*4
menu=0
while menu!=3:
    try:
        print("\n1. Ingresar Kilos de uva \n2. Seleccione tipo de Uva\n3. Salir\n")
        menu=int(input("Introduzca Opcion "))
        if menu==1:
            kilos=int(input("Introduzca cantidad de Uvas en Kgs "))
        elif menu==2:
            tipo=int(input("Elige tipo de Uva.\n1. Tipo A\n2. Tipo B "))
            if tipo==1:
                tamaño=int(input("Elige tamaño de Uva.\n1. Tamaño 1\n2. Tamaño 2 "))
                if tamaño==1:
                    ganancia=(pini+20)*kilos
                    print(f"\nLa ganancia total sera de {ganancia}€\n\n")
                elif tamaño==2:
                    ganancia=(pini+30)*kilos
                    print(f"\nLa ganancia total sera de {ganancia}€\n\n")
            elif tipo==2:
                tamaño=int(input("Elige tamaño de Uva.\n1. Tamaño 1\n2. Tamaño 2 "))
                if tamaño==1:
                    ganancia=(pini-30)*kilos
                    print(f"\nLa ganancia total sera de {ganancia}€\n\n")
                elif tamaño==2:
                    ganancia=(pini-50)*kilos
                    print(f"\nLa ganancia total sera de {ganancia}€\n\n")
    except:
        print("\nDebe introducir alguna opcion")"""

"""Juan recibe dos tipos de regalos de cumpleaños según el año en el que esté: si el
año es impar su familia le regala un puzzle; si es par, recibe dinero.
Cada nuevo cumpleaños recibe más regalos: así, cada año que recibe puzzles
obtiene el doble que el anterior; sin embargo, si se trata de dinero recibe 15€ más
que en la anterior ocasión.
Elabora un programa que calcule cuántos regalos ha recibido en total Juan, para una
edad determinada sabiendo que en el primer cumpleaños le regalaron un puzzle y
en el segundo 20€.
"""

