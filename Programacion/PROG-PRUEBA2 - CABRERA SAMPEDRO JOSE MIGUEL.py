try:
    peso=float(input("Introduce peso: "))
    edad=int(input("Introduce edad: "))
    tipo=input("Introduce estilo de vida SEDENTARIA/ACTIVA/MUY ACTIVA: ").upper()
    recomendacion=""
    if peso > 0:
        while edad <1 or tipo not in ("SEDENTARIA, ACTIVA, MUY ACTIVA"):
            edad=int(input("Introduce edad: "))
            tipo=input("Introduce estilo de vida SEDENTARIA/ACTIVA/MUY ACTIVA: ").upper()
        if (edad > 70 and tipo=="SEDENTARIA") or (peso >100) or (peso > 74.4 and edad >50):
            recomendacion="debe ir al medico"
        else:
            recomendacion="no es urgente que acuda al medico si no tiene problemas de salud"
    else:
        recomendacion="no ha aportado datos validos"
    print(f"El cliente {recomendacion}")
except:
    print("El cliente no ha aportado datos validos")