import time
"""#1
jugadorA=""
jugadorB=""
while jugadorA != "SPOCK" or jugadorB !="SPOCK":
    jugadorA=""
    jugadorB=""
    while jugadorA not in ("PIEDRA","PAPEL","TIJERAS","LAGARTO","SPOCK"):
        jugadorA=input("Introduzca elemento A: ").upper()
    while jugadorB not in ("PIEDRA","PAPEL","TIJERAS","LAGARTO","SPOCK"):
        jugadorB=input("Introduzca elemento B: ").upper()
    
    if jugadorA=="PIEDRA" and jugadorB in ("LAGARTO","TIJERAS"):
        jugada="GANA"
    elif jugadorA=="PAPEL" and jugadorB in ("SPOCK","PIEDRA"):
        jugada="GANA"
    elif jugadorA=="LAGARTO" and jugadorB in ("SPOCK","PAPEL"):
        jugada="GANA"
    elif jugadorA=="SPOCK" and jugadorB in ("TIJERAS","PIEDRA"):
        jugada="GANA"
    elif jugadorA=="TIJERAS" and jugadorB in ("PAPEL","LAGARTO"):
        jugada="GANA"
    elif jugadorA==jugadorB:
        jugada="EMPATA"
    else:
        jugada="PIERDE"
    if jugada =="GANA":
        print(f"{jugadorA} {jugada} A {jugadorB}")
    else:
        print(f"{jugadorA} {jugada} ANTE {jugadorB}")
for i in range(5):
    i*="."
    print(f"Terminando juego{i}", end="\r")
    time.sleep(0.5)"""


#2

"""alumnos=0
alumnossalen=0
menu=0
mostrarmenu="##########################################\n# Bienvenido al IES Jacarandá!!:         #\n1. Alumnos que han entrado: \n2. Alumnos que han abandonado el centro: \n3. Alumnos en el IES: \n4. Mostrar menu \n5. Salir\n##########################################"

print(mostrarmenu)
while menu!=5:
    menu=int(input("Introduzca Opcion(introduzca 4 para visualizar menu): "))
    if menu==1:
        alumnos+=int(input("¿Cuantos alumnos acceden al centro? "))
    elif menu==2:
        alumnossalen=int(input("¿Cuantos alumnos abandonan el centro? "))
        if alumnos-alumnossalen <0:
            print(f"No puede ser que haya alumnos en negativo.\nActualmente hay {alumnos}")
        else:
            alumnos=alumnos-alumnossalen
    elif menu==3:
        print(f"\nEn el centro hay actualmente {alumnos}\n")
    elif menu==4:
        print(mostrarmenu)
    elif menu>5 or menu<1:
        print(mostrarmenu)
        menu=int(input("Introduzca una opcion valida:"))
"""
"""#3
total=2
edad=0
java=0
python=0
javamujer=0
javahombre=0
edadjava=0
edadpython=0
sexo=""
pythonhombre=0
pythonmujer=0
menu=0
contador=0
mostrarmenu="1. Introducir datos\n2. Salir"
while contador <total:
    print(mostrarmenu)
    menu=int(input("Seleccione Opcion"))
    if menu==1:
        edad=int(input("Introduzca su edad: "))
        while edad <18 or edad > 65:
            edad=int(input("La edad minima para trabajar es 16 años: "))
        while sexo != "H" and sexo != "M":
            sexo=input("Introduce sexo H/M").upper()
        lenguaje=""
        while lenguaje != "J" and lenguaje!="P":
            lenguaje=input("Introduzca lenguaje Java (J) o Python (P) ").upper()
        if lenguaje =="J" and sexo =="H":
            javahombre+=1
            java+=1
            edadjava+=edad
            sexo=""
            edad=0
        elif lenguaje =="J" and sexo =="M":
            javamujer+=1
            java+=1
            edadjava+=edad
            sexo=""
            edad=0
        elif lenguaje == "P" and sexo =="H":
            pythonhombre+=1
            python+=1
            edadpython+=edad
            sexo=""
            edad=0
        else:
            pythonmujer+=1
            python+=1
            edadpython+=edad
            sexo=""
            edad=0
        contador+=1
    else:
        contador=total
print(f"El {(python*100)/total}% usa Python, de los que {pythonhombre} son hombres y {pythonmujer} mujeres y su edad media es {edadpython/total} años")
print(f"El {(java*100)/total}% usa Python, de los que {javahombre} son hombres y {javamujer} mujeres y su edad media es {edadjava/total} años")"""

"""contador=0

lenguaje=""

while contador < 5:
    lenguaje=""
    while lenguaje!="python" and lenguaje!="java":
        lenguaje=input("Introduzca")
    contador+=1
"""