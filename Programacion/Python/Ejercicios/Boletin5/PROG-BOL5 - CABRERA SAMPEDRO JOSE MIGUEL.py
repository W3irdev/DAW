"""1. Escribe el código de un programa que reciba un número de nota de 0 a 100 y nos
informe de las calificaciones en el siguiente formato:
    90-100, Sobresaliente
    70-89, Notable
    60-69, Bien
    50-59, Suficiente
    0-49, Suspenso
"""



try:
    nota=int(input("Introduzca nota: "))

    while nota<0 or nota>100:
        nota=int(input("Introduzca una nota entre 0 y 100: "))
    if nota >= 90:
        calificacion="Sobresaliente"
    elif nota >= 70:
        calificacion="Notable"
    elif nota >=60:
        calificacion="Bien"
    elif nota >=50:
        calificacion="Suficiente"
    else:
        calificacion="Suspensa"
        
    print(f"La asignatura esta {calificacion}")


except:
    print("Introduzca un numero entre 0 y 100: ")

"""2. Escribe una aplicación que pida la fecha actual (día y mes) y el hemisferio
(Norte/Sur) e indique en qué estación se encuentra:
a. Hemisferio Norte: Otoño (desde 23 Septiembre), Invierno (desde 21
diciembre), Primavera (desde 21 Marzo), Verano (desde 21 Junio).
b. Hemisferio Sur: Primavera (desde 23 Septiembre), Verano (desde 21
diciembre), Otoño (desde 21 Marzo), Invierno (desde 21 Junio)."""

invierno=["DICIEMBRE","ENERO","FEBRERO","MARZO","12","1","2","3"]
primavera=["MARZO","ABRIL","MAYO","JUNIO","3","4","5","6"]
verano=["JUNIO","JULIO","AGOSTO","SEPTIEMBRE","6","7","8","9"]
try:
    fecha=int(input("Dia: ")),((input("Mes: ")).upper())
    hemi=(input("Indique hemisferio: ")).upper()
    estacion=None

    while (fecha[0] > 31 or (hemi !="NORTE" and hemi !="SUR")) or ((fecha[1] == "FEBRERO" or fecha[1] == "2") and fecha[0]>29):
        if (fecha[1] == "FEBRERO" or fecha[1] == "2") and fecha[0]>29:
            print("El mes de Febrero no puede tener mas de 29 dias en año bisiestos")
            fecha=int(input("Dia: ")),(input("Mes: ")).upper()
        else:
            fecha=int(input("Dia: ")),(input("Mes: ")).upper()
            hemi=(input("Indique hemisferio: ")).upper()
    if hemi == "NORTE":
        if fecha[1] in invierno:
            if fecha[0] < 21 and (fecha[1] == invierno[0] or fecha[1] == invierno[4]):
                estacion="Otoño"
            else:
                estacion="Invierno"
        elif fecha[1] in primavera:
            if fecha[0] < 21 and (fecha[1] == primavera[0] or fecha[1] == primavera[4]):
                estacion="Otoño"
            else:
                estacion="Verano"
        elif fecha[1] in verano:
            if fecha[0] < 21 and (fecha[1] == verano[0] or fecha[1] == verano[4]):
                estacion="Otoño"
            else:
                estacion="Primavera"
        print(estacion)
    elif hemi == "SUR":
        if fecha[1] in invierno:
            if fecha[0] < 21 and (fecha[1] == invierno[0] or fecha[1] == invierno[4]):
                estacion="Primavera"
            else:
                estacion="Verano"
        elif fecha[1] in primavera:
            if fecha[0] < 21 and (fecha[1] == primavera[0] or fecha[1] == primavera[4]):
                estacion="Primavera"
            else:
                estacion="Invierno"
        elif fecha[1] in verano:
            if fecha[0] < 21 and (fecha[1] == verano[0] or fecha[1] == verano[4]):
                estacion="Primavera"
            else:
                estacion="Otoño"
        print(estacion)
    else:
        print("Introduzca un dia y un mes valido")



except:
    print("Introduzca valores validos")

"""3. Crea un programa que dada una fecha en formato (dd-mm-yyyy), nos devuelva
cuántos días han transcurrido desde el 1 de enero de ese mismo año (considera que
puede tratarse de un año bisiesto)."""


def bisiesto():
    ano=fecha[2]
    if (ano %4==0) and (ano%100!=0 or ano%400==0):
        return 29
    else:
        return 28

try:
    meses=1
    fecha=[int(input("Introduzca una fecha en formato dd-mm-yyyy. \nDia: ")),int(input("Mes: ")),int(input("Año: "))]
    meslargo=[3,5,7,8,10,12]
    totaldias=0
    while (fecha[0] >31 or fecha[0] < 1) or (fecha[1]>12 or fecha[1]<1):
        print("Introduzca una fecha correcta porfavor")
        fecha=[int(input("Dia: ")),int(input("Mes: ")),int(input("Año: "))]

    if fecha[1]==1:
        print(f"Han pasado {fecha[0]} dias")
    elif bisiesto()==29:
        while meses < fecha[1]:
            if meses==2:
                totaldias+=29
            elif meses in meslargo:
                totaldias+=31
            else:
                totaldias+=30
            meses+=1
        print(f"En el dia {fecha[0]}-{fecha[1]}-{fecha[2]}. Han pasado {(totaldias)+(fecha[0])+1} dias")
    else:
        while meses < fecha[1]:
            if meses==2:
                totaldias+=28
            elif meses in meslargo:
                totaldias+=31
            else:
                totaldias+=30
            meses+=1
        print(f"En el dia {fecha[0]}-{fecha[1]}-{fecha[2]}. Han pasado {(totaldias)+(fecha[0])+1} dias")

except:
    print("Introduzca valores en formato dd-mm-yyyy")
    
"""4. Existen cuatro grupos sanguíneos en seres humanos, que se multiplican por dos si
consideramos el factor Rh. Unos grupos son compatibles con otros atendiendo al
criterio que podemos ver en las siguientes tablas.
Grupo Dona a Recibe de Rh Dona a Recibe de
A A, AB A, 0 + + +, -
B B, AB B, 0 - +, - -
AB AB A, B, AB, 0
0 A, B, AB, 0 0
Elabora un programa que reciba dos grupos sanguíneos y devuelva si son
compatibles y en qué sentido.
Por ejemplo, si se recibe A y B debería decir que no son compatibles.
Por el contrario, si se recibe 0 y AB debería indicar que son compatibles y AB es
receptor de 0."""

grupoA=["A","0"]
grupoB=["B","0"]
grupoAB=["A","B","AB","0"]
grupo0=["0"]

grupo1=input("Introduce el grupo sanguineo receptor: ")
grupo2=input("Introduce el grupo sanguineo donante: ")

while grupo1 not in grupoAB or grupo2 not in grupoAB:
    grupo1=input("Introduce el grupo sanguineo receptor: ")
    grupo2=input("Introduce el grupo sanguineo donante: ")

recibe=None
compatible=False
if grupo1 == "A":
    if grupo2 == "AB" or grupo2 == "A" or grupo2 == "0":
        compatible=True
        recibe="de grupo A, AB o 0"
elif grupo1 == "B":
    if grupo2 == "AB" or grupo2 == "B" or grupo2 == "0":
        compatible=True
        recibe="de grupo B, AB o 0"
elif grupo1 == "AB":
    if grupo2 == "AB" or grupo2 == "A" or grupo2 == "B" or grupo2 == "0":
        compatible=True
        recibe="de grupo A, AB, B o 0"
elif grupo1 == "0":
    if grupo2 == "0":
        compatible=False
        recibe="solo recibe de 0"
else:
    compatible="No son compatibles"

if compatible == True:
    print(f"{grupo1} y {grupo2} son compatible y {grupo1} puede recibir de {recibe} ")
else:
    print(f"{grupo1} y {grupo2} no son compatibles")

