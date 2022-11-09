#Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
import math
print("""\

          *
        * *
 h    * * *  b
    * * * *
  * * * * *  
      a    """)

lado1 = int(input("Introduzca primer lado (a) "))
lado2 = int(input("Introduzca segundo lado (b) "))

print("La hipotenusa del triangulo es " + str((lado1**2+lado2**2)**0.5))

# Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius.

print("Esto es un convertidor de Fº a Cº introduzca el valor en grados Fahrenheit a continuación: ")

fahrenheit = float(input())
celcius= float((fahrenheit-32)*5/9)
print(f"{fahrenheit}ºF en grados centigrados es {celcius}ºC")

#Calcular la media de tres números pedidos por teclado

from statistics import mean


num1=int(input("Introduzca primer numero: "))
num2=int(input("Introduzca segundo numero: "))
num3=int(input("Introduzca tercer numero: "))
lista=[num1, num2, num3]
calculo=num1+num2+num3
media = (calculo)/3

print(f"la media aritmetica de {lista} es {media}")

#Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto deberá pagar finalmente por su compra.

print("Introduzca el precio del articulo o cesta para saber cuanto tendrá que pagar con descuento del 15% aplicado.")
precio=int(input())

descuento=precio*(0.15)
total=precio-descuento

print(f"En total tendrá que pagar {total}€")

#Pide al usuario dos números y muestra la "distancia" entre ellos (el valor absoluto de su
#diferencia, de modo que el resultado sea siempre positivo).


num1=int(input("Introduzca primer valor: "))
num2=int(input("Introduzca segundo valor: "))
distancia=num1-num2
total=(distancia*(-1))
if distancia <0:
    print(f"La distancia entre A y B, es {total}")
else:
    print(f"La distancia entre A y B es {distancia}")

#Pide al usuario dos pares de números x1,y2 y x2,y2, que representen dos puntos en el plano.
#Calcula y muestra la distancia entre ellos.
import math

x1=int(input("Introduzca x1: "))
y1=int(input("Introduzca y1: "))
x2=int(input("Introduzca x2: "))
y2=int(input("Introduzca y2: "))

pun1=[x1,y1]
pun2=[x2,y2]
d=math.dist(pun1,pun2)
#print(f"La distancia entre el punto {pun1} y {pun2} es {d}")
print(f"La distancia entre el punto {pun1} y {pun2} es {((x2-x1)**2+(y2-y1)**2)**0.5:.2f}")

#Realizar un algoritmos que lea un número y que muestre su raíz cuadrada y su raíz cúbica.
#Python no tiene ninguna función predefinida que permita calcular la raíz cúbica, ¿cómo se
#puede calcular?
#La raiz cubica se puede calcular elevando un numero a la division de 1/3

import math
num=int(input("Introduzca numero: "))

rq = math.sqrt(num)
rc = num**(1/3)

"""
print(f"La raiz cuadrada de {num} es {rq}")
print(f"La raiz cubica de {num} es {rc}")"""

print(f"La raiz cuadrada de {num} es {num**0.5}")
print(f"La raiz cubica de {num} es {rc}")

#Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos) después de
#pedirnos cuantas monedas tenemos de 2e, 1e, 50 céntimos, 20 céntimos o 10 céntimos).


try:
    de=int(input("¿Cuantas monedas de 2€ tienes?: "))
    ue=int(input("¿Cuantas monedas de 1€ tienes?: "))
    cc=int(input("¿Cuantas monedas de 50 centimos tienes?: "))
    vc=int(input("¿Cuantas monedas de 20 centimos tienes?: "))
    dc=int(input("¿Cuantas monedas de 10 centimos tienes? "))


    euros=(de*2)+(ue)+(cc*50/100)+(vc*20/100)+(dc*10/100)
    centimos=(de*200)+(ue*100)+(cc*50)+(vc*20)+(dc*10)
    proeuros=centimos//100
    proporcional=centimos%100
    print(f"Tienes {proeuros}€ euros y {proporcional} centimos")

except:
    print ("Introduce algun valor, no puede quedar blanco")

"""Realiza un algoritmo que calcule la potencia, para ello pide por teclado la base y el
exponente. Pueden ocurrir tres cosas:
◦ El exponente sea positivo, sólo tienes que imprimir la potencia.
◦ El exponente sea 0, el resultado es 1.
◦ El exponente sea negativo, el resultado es 1/potencia con el exponente positivo."""

try:
    base=int(input("Introduce la base: "))
    exponente=int(input("Introduce exponente: "))
    exponenteabs=abs(exponente)
    exponentepos=(-(exponente))
    resultado=base**exponente
    if exponente>0:      
        print(f"La potencia de {base} elevado a {exponente} es {resultado}")
    elif exponente==0:
        print(f"La potencia de {base} elevado a {exponente} es 1")
    elif exponente<0:
        resultadoneg=base**exponentepos
        print(f"El resultado es {1/(resultadoneg)}")
except:
    print("Introduce datos validos")

"""Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los
lados de un triángulo. El programa debe determinar que tipo de triangulo es, teniendo en
cuenta los siguiente:
◦ Si se cumple Pitágoras entonces es triángulo rectángulo
◦ Si sólo dos lados del triángulo son iguales entonces es isósceles.
◦ Si los 3 lados son iguales entonces es equilátero.
◦ Si no se cumple ninguna de las condiciones anteriores, es escaleno.
"""


try:
    a=int(input("Introduce lado A: "))
    b=int(input("Introduce lado B: "))
    c=int(input("Introduce lado C: "))

    while a >0 and b >0 and c>0:
        if (a**2)+(b**2)==(c**2) or (b**2)+(c**2)==(a**2) or (c**2)+(b**2)==(a**2):
            print("El triangulo es rectangulo")
        elif a==b!=c or b==c!=a or c==a!=b:
            print("El triangulo es isosceles")
        elif a==b==c:
            print("El triangulo es equilatero")
        else:
            print("El triangulo es escaleno")
    else:
        print("Introduce numeros positivos y mayor a 0")

except:
    print("Introduce valores correctos y positivos")

"""Escribir un programa que lea un año indicar si es bisiesto. Nota: un año es bisiesto si es un
número divisible por 4, pero no si es divisible por 100, excepto que también sea divisible
por 400."""

ano=int(input("Introduce año: "))
if ano % 4 != 0:
    print("No es bisiesto")
elif ano %4==0 and ano %100!=0:
    print("Es bisisesto")
elif ano %4==0 and ano %100==0 and ano %400!=0:
    print("No es bisiesto")
elif ano %4==0 and ano %100 == 0 and ano %400==0:
    print("Es bisiesto")

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

"""Realiza un programa que pida el día de la semana (del 1 al 7) y escriba el día
correspondiente. Si introducimos otro número nos da un error."""

try:
    dia=int(input("Introduzca dia de la semana(del 1 al 7): "))
    
    if dia == 1: print("Lunes")
    elif dia == 2: print("Martes")
    elif dia == 3: print("Miercoles")
    elif dia == 4: print("Jueves")
    elif dia == 5: print("Viernes")
    elif dia == 6: print("Sabado")
    elif dia == 7: print("Domingo")
    elif dia == 0 or dia > 7:
        print("Introduzca un numero del 1 al 7 porfavor")
            

except:
    print("Introduzca un numero del 1 al 7 porfavor")

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

"""Escribir un programa que imprima todos los números pares entre dos números que se le
pidan al usuario"""

num1=int(input("Introduzca primer numero: "))
num2=int(input("Introduzca segundo numero: "))

try:
    if num1 < num2:
        for i in range(num1,num2):
            pares=i%2
            if pares == False:
                print(i)
    else: print("El primer numero debe ser mayor al segundo")

except:
    print("Introduzca dos numeros")

"""Escribe un programa que pida el limite inferior y superior de un intervalo. Si el límite
inferior es mayor que el superior lo tiene que volver a pedir.
A continuación se van introduciendo números hasta que introduzcamos el 0. Cuando termine
el programa dará las siguientes informaciones:
◦ La suma de los números que están dentro del intervalo (intervalo abierto).
◦ Cuantos números están fuera del intervalo.
◦ Informa si hemos introducido algún número igual a los límites del intervalo.
"""

try:
    inf=1
    sup=10
    suma=0
    contador=0
    num3=int(input("Introduzca un numero (introduce 0 para terminar el programa) "))
    igual=0
    while sup >= inf:
        inf=int(input("Mete"))
    while num3!=0:
        
        if num3 > inf and num3 < sup:
            suma+=num3
        elif num3 > sup or num3 < inf:
            contador+=1
        else:
            igual+=1
        num3=int(input("Introduzca un numero (introduce 0 para terminar el programa) "))
    print(f"La suma de los numeros dentro del intervalo es {suma}")
    print(f"{contador} numeros estan fuera del intervalo")
    print(f"Has introducido {igual} que coinciden con el intervalo")
except:
    print("Introduzca valores")
    
"""19. Escribe un programa que dados dos números, uno real (base) y un entero positivo
(exponente), saque por pantalla el resultado de la potencia. No se puede utilizar el operador
de potencia."""
base=int(input("Introduzca base "))
exponente=int(input("Introduzca exponente "))
total=1
for i in range(exponente):
    total=total*base
print(f"{base} elevado a {exponente} es {total}")

"""Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó 10 €, el
segundo 20 €, el tercero 40 € y así sucesivamente. Realizar un programa para determinar
cuánto debe pagar mensualmente y el total de lo que pagará después de los 20 meses."""
meses=0
cuota=5
while meses <20:
    meses+=1
    cuota+=cuota
    total=cuota
    print("En el mes " + (str(meses)) + " tienes que pagar "+ str(cuota))
    for i in range(total):
        i+=i
        total=i

    

print("En total tienes que pagar " + str(total)) 


"""21. Mostrar en pantalla los N primero número primos. Se pide por teclado la cantidad de
números primos que queremos mostrar"""

cant=int(input("Introduce cuantos numeros primos quieres averiguar "))
bucles=0
primo=3
contador=0
resto=0
while bucles < cant:
    resto=0
    contador=0      
    for i in range(2,primo):
        resto=primo%i
        if resto==0:
            contador+=1
    if contador==0:
        print(primo)
        bucles+=1
    primo+=1
    
