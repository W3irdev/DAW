"""La asociación de vinicultores tiene como política fijar un precio inicial al kilo de uva, la cual
se clasifica en tipos A y B, y además en tamaños 1 y 2. Cuando se realiza la venta del
producto, ésta es de un solo tipo y tamaño, se requiere determinar cuánto recibirá un
productor por la uva que entrega en un embarque, considerando lo siguiente: si es de tipo A,
se le cargan 20 céntimos al precio inicial cuando es de tamaño 1; y 30 céntimos si es de
tamaño 2. Si es de tipo B, se rebajan 30 céntimos cuando es de tamaño 1, y 50 céntimos
cuando es de tamaño 2. Realice un algoritmo para determinar la ganancia obtenida."""

pini=100*4
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
        print("\nDebe introducir alguna opcion")
print("Saliendo...\n")
            

        


