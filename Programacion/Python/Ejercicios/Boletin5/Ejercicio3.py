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