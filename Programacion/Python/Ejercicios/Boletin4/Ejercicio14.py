"""La política de cobro de una compañía telefónica es: cuando se realiza una llamada, el cobro
es por el tiempo que ésta dura, de tal forma que los primeros cinco minutos cuestan 1 euro,
los siguientes tres, 80 céntimos, los siguientes dos minutos, 70 céntimos, y a partir del
décimo minuto, 50 céntimos. Además, se carga un impuesto de 3 % cuando es domingo, y si
es otro día, en turno de mañana, 15 %, y en turno de tarde, 10 %. Realice un algoritmo para
determinar cuánto debe pagar por cada concepto una persona que realiza una llamada."""

duracion=int(input("Cuanto ha durado la llamada en minutos?"))
domingo=0
manana=0

if duracion <= 5:
    print("1. Lunes-Sabado\n2. Domingo")
    domingo=int(input("Es domingo? "))
    if domingo ==2:
        coste=1*1.03
        print(f"El coste de la llamada es {coste}")
    elif domingo ==1:
        print("1. Mañana\n2. Tarde")
        tarde=int(input("Es mañana o tarde?"))
        if tarde == 2:
            coste=1*1.1
            print(f"El coste de la llamada es {coste}")
        elif tarde == 1:
            coste=1*1.15
            print(f"El coste de la llamada es {coste}")
elif duracion > 5 and duracion <= 8:
    print("1. Lunes-Sabado\n2. Domingo")
    domingo=int(input("Es domingo? "))
    if domingo ==2:
        coste=1.8*1.03
        print(f"El coste de la llamada es {coste}")
    elif domingo ==1:
        print("1. Mañana\n2. Tarde")
        tarde=int(input("Es mañana o tarde?"))
        if tarde == 2:
            coste=1.8*1.1
            print(f"El coste de la llamada es {coste}")
        elif tarde == 1:
            coste=1.8*1.15
            print(f"El coste de la llamada es {coste}")
elif duracion > 8 and duracion <= 10:
    print("1. Lunes-Sabado\n2. Domingo")
    domingo=int(input("Es domingo? "))
    if domingo ==2:
        coste=2.5*1.03
        print(f"El coste de la llamada es {coste}")
    elif domingo ==1:
        print("1. Mañana\n2. Tarde")
        tarde=int(input("Es mañana o tarde?"))
        if tarde == 2:
            coste=2.5*1.1
            print(f"El coste de la llamada es {coste}")
        elif tarde == 1:
            coste=2.5*1.15
            print(f"El coste de la llamada es {coste}")
elif duracion >=10:
    print("1. Lunes-Sabado\n2. Domingo")
    domingo=int(input("Es domingo? "))
    if domingo ==2:
        coste=3*1.03
        print(f"El coste de la llamada es {coste}")
    elif domingo ==1:
        print("1. Mañana\n2. Tarde")
        tarde=int(input("Es mañana o tarde?"))
        if tarde == 2:
            coste=3*1.1
            print(f"El coste de la llamada es {coste}")
        elif tarde == 1:
            coste=3*1.15
            print(f"El coste de la llamada es {coste}")

    