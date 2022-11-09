"""El director de una escuela está organizando un viaje de estudios, y requiere determinar
cuánto debe cobrar a cada alumno y cuánto debe pagar a la compañía de viajes por el
servicio. La forma de cobrar es la siguiente: si son 100 alumnos o más, el costo por cada
alumno es de 65 euros; de 50 a 99 alumnos, el costo es de 70 euros, de 30 a 49, de 95 euros,
y si son menos de 30, el costo de la renta del autobús es de 4000 euros, sin importar el
número de alumnos. Realice un algoritmo que permita determinar el pago a la compañía de
autobuses y lo que debe pagar cada alumno por el viaje."""

alumnos=int(input("Cuantos alumnos van: "))

if alumnos >=100:
    print(f"El autobus cuesta "+ str((alumnos*65)) + "€, y cada alumno debe pagar " + str((alumnos*65)/(alumnos)) + ("€"))
elif alumnos >=50 and alumnos<=99:
    print(f"El autobus cuesta "+ str((alumnos*70)) + "€, y cada alumno debe pagar " + str((alumnos*70)/(alumnos)) + ("€"))
elif alumnos >=49 and alumnos<=30:
    print(f"El autobus cuesta "+ str((alumnos*95)) + "€, y cada alumno debe pagar " + str((alumnos*95)/(alumnos)) + ("€"))
elif alumnos <=29:
    print("El autobus cuesta 4000€" + f", y cada alumno debe pagar {4000/alumnos:.2f}€")