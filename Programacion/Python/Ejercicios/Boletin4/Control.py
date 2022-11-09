"""En el gimnasio Jacafitness tienen el siguiente horario: Los Lunes, Miércoles y Jueves imparten 
Spinning de 12 a 14, Yoga de 16 a 20h y Body Combat de 20 a 22; Los Martes y Jueves
La sesion de Spinning y Yoga se intercambian.

Elabora un programa que dé la bienvenida al gimnasio Jacafitness y tras preguntar por la hora y el dia de 
la semana te indique la actividad que puedes realizar"""



try:

    print("\nBienvenidos/as a Jacafitness\n\nNuestro Horario es:\nLunes, Miercoles y Jueves:\nSpinning de 12 a 14h.\nYoga de 16 a 20h.\nBody Combat de 20 a 22h")
    print("\nMartes y Jueves:\nYoga de 12 a 14h.\nSpinning de 16 a 20h.\nBody Combat de 20 a 22h.\n")
    dia=input("¿Que dia de la semana es? \n")
    hora=int(input("¿Que hora es?(formato: 1 a 24h): \n"))

    spinning=["Lunes","Miercoles","Viernes","lunes","miercoles","viernes"]
    yoga=["Martes","Jueves","martes","jueves"]
    if dia in spinning:
        if hora >=12 and hora <14:
            print("Ahora mismo la clase es de spinning")
        elif hora >=16 and hora <20:
            print("Ahora mismo hay clases de Yoga")
        elif hora >=20 and hora <22:
            print("Ahora la clase es de Body Combat")
    elif dia in yoga:
        if hora >=12 and hora <14:
            print("Ahora mismo la clase es de Yoga")
        elif hora >=16 and hora <20:
            print("Ahora mismo hay clases de Spinning")
        elif hora >=20 and hora <22:
            print("Ahora la clase es de Body Combat")

    else:
        print("Ahora mismo no hay clases")
except:
    print("Introduzca un dia de Lunes-Viernes y una hora correcta")
