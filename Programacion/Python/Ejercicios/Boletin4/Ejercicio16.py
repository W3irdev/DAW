"""Escribe un programa que pida un número entero entre uno y doce e imprima el número de
días que tiene el mes correspondiente."""
try:
    meses=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
    mes=None
    while mes !=0:
        mes=int(input("Numero de mes: "))
        if mes in (1,3,5,7,8,10,12):
            print("Es "+ meses[mes-1] + " y tiene 31 días")
        elif mes in (4,6,9,11):
            print("Es " + meses[mes-1] + " y tiene 30 días")
        elif mes == 2:
            print("Es " + meses[mes-1] + " y tiene 28 días.")
        else:
            print("No has introducido ningun nº que corresponda a un mes.")            
except:
    print("Introduzca un numero del 1 al 12 porfavor")