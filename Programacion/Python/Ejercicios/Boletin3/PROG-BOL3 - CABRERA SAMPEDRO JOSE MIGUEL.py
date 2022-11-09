"""Realizar un programa que lea un número entero por teclado e informe de si
el número es par o impar (el cero se considera par).
"""
"""
try:
    numero = int(input("Introduce un numero: "))
    if numero %2 == 1:
        print(f"El numero {numero} es impar")
    else:
        print(f"El numero {numero} es par")
except:
    print("Introduce un nº porfavor")
"""
"""Realizar un programa que solicite dos números por teclado e imprima en
pantalla si son iguales, el primero mayor que el segundo o el primero más
pequeño que el segundo."""

"""num1=int(input("Introduce primer numero: "))
num2=int(input("Introduce segundo numero: "))

try:
    if num1 > num2:
        print(f"El {num1} es mayor a {num2}")
    elif num1 < num2:
        print(f"El {num1} es menor que {num2}")
    else:
        print(f"{num1} y {num2} son iguales")
except:
    print("Introduce un numero porfavor")"""

"""Realizar un programa que lea un número por teclado. El programa debe
imprimir en pantalla un mensaje con “El número xx es múltiplo de 2” o un
mensaje con “El número xx es múltiplo de 3”. Si es múltiplo de 2 y de 3
deben aparecer los dos mensajes. Si no es múltiplo de ninguno de los dos
el programa finaliza sin mostrar ningún mensaje.

num=int(input("Introduce un numero "))

if num%2==0 and num%3==0:
    print(f"El numero {num} es multiplo de 2 y 3")
elif num%2==0:
    print(f"El numero {num} es multiplo de 2")
elif num%3==0:
    print(f"El numero {num} es multiplo de 3")
"""
"""Realizar un programa que lea la edad de una persona menor a 100 años e
informe de si es un niño (0-12 años), un adolescente (13-17), un joven (18-
29) o un adulto."""

"""edad = abs(int(input("Introduzca su edad: ")))

try:
    if edad >=0 and edad <= 12:
        print("Es un niño")
    elif edad >=13 and edad <=17:
        print("Es adolescente")
    elif edad >=18 and edad <=29:
        print("Es un joven")
    elif edad >29 and edad < 100:
        print("Es un adulto")
    else:
        print("No puedes poner una edad mayor a 99")
except:
    print("Introduzca un numero")"""

"""Realizar un programa que solicite 4 números e imprima la media de los
números. También debe imprimir aquellos números que son superiores a la
media"""

"""num1=int(input("Introduzca primer numero: "))
num2=int(input("Introduzca numero 2: "))
num3=int(input("Introduzca numero 3: "))
num4=int(input("Introduzca ultimo numero: "))
media=(num1+num2+num3+num4)/4

print(f"La media de {num1}, {num2}, {num3} y {num4} es {media}")
for i in(num1,num2,num3,num4):
    if i > media:
        print(f"{i} es un numero mayor que la media de todos")"""

"""Realizar un programa que solicite un carácter por teclado e informe por
pantalla si el carácter es una vocal o no lo es. Si es una vocal mostrará el
mensaje “Es la primera vocal (A)” o “Es la segunda vocal (E)”, etc.
"""
"""import string

caracter=input("Introduzca caracter: ")
vocales=["a","e","i","o","u","A","E","I","O","U"]
try:
    
    if caracter in (vocales):
        vocal=vocales.index(caracter)
        if vocal == 0 or vocal == 5:
            print("Es la primera vocal (A)")
        elif vocal == 1 or vocal == 6:
            print("Es la segunda vocal (E)")
        elif vocal == 2 or vocal == 7:
            print("Es la tercera vocal (I)")
        elif vocal == 3 or vocal == 8:
            print("Es la cuarta vocal (O)")
        elif vocal == 4 or vocal == 9:
            print("Es la quita vocal (U)")
    else:
        if caracter in(string.ascii_lowercase) or caracter in(string.ascii_uppercase):
            print("Es una consonante")
        else:
            print("No puedes poner numeros")
except:
    print("Introduzca un caracter alfabetico")"""


"""7. Realizar un programa que lea el estado civil de una persona (S-Soltero, CCasado, V-Viudo y D-Divorciado) y su edad. Después debe mostrar por
pantalla el porcentaje de retención que debe aplicársele de acuerdo con las
siguientes reglas:
 A los solteros o divorciados menores de 35 años, un 12%
 Todas las personas mayores de 50 años, un 8.5%
 A los viudos o casados menores de 35 años, un 11.3%
 Al resto de casos se le aplica un 10.5%"""


"""try:
    estadoCivil=input("Introduzca su estado civil\nS-Soltero, C-Casado, V-Viudo o D-Divorciado\n")
    edad=int(input("Introduzca su edad: "))
    if (estadoCivil.upper == "S" or estadoCivil.upper == "D") and edad <35:
        print("Se le aplica una retencion del 12%")
    elif edad>50:
        print("Se le aplica una reduccion del 8.5%")
    elif (estadoCivil.upper == "V" or estadoCivil.upper =="C") and edad <35:
        print("Se le aplica una retencion del 11.3%")
    else:
        print("Se le aplica una retencion del 10.5%")
except:
    print("Introduzca valores validos")
"""
"""8. Realizar un programa que lea por teclado dos marcaciones de un reloj
digital (horas, minutos, segundos) comprendidas entre las 0:0:0 y las
23:59:59 e informe cual de ellas es mayor.
Ejemplo:
Hora 1: 12:35:37
Hora 2: 12:38:36
“Hora 2 es mayor”"""
"""
horas1=int(input("Introduzca la hora 1: "))
minutos1=int(input("Introduzca los minutos 1: "))
segundos1=int(input("Introduzca los segundos 1: "))

horas2=int(input("Introduzca la hora 2: "))
minutos2=int(input("Introduzca los minutos 2: "))
segundos2=int(input("Introduzca los segundos 2: "))

if 0<=horas1<24 and 0<=horas2<24 and 0<=minutos1<60 and 0<=minutos2<60 and 0<=segundos1<60 and 0<=segundos2<60:

    if horas1>horas2:
        print("Hora 1 es mayor")
    elif horas1==horas2:
        if minutos1>minutos2:
            print("Hora 1 es mayor")
        elif minutos1==minutos2:
            if segundos1>segundos2:
                print("Hora 1 es mayor")
            else:
                print("Hora 2 es mayor")
        else:
            print("Hora 2 es mayor")
    else:
        print("Hora 2 es mayor")
else:
    print("Introduce horas comprendidas entre las 0 y las 24 horas del dia")"""

"""9. En un establecimiento en rebajas, hay 3 tipos de productos (A, B y C). El
porcentaje de rebaja que se aplicará sobre el precio original del producto se
calcula de la siguiente forma:
 Si el producto es de tipo A, independientemente de su precio se
aplica un 7% de descuento.
 Si el producto es de tipo C o bien el precio es inferior a 500€ se
aplicará un porcentaje del 12% de descuento.
 En el resto de casos se aplica un 9% de descuento.
Realizar un programa que solicite los datos necesarios (tipo de producto y
precio original) y calcule el precio rebajado. Debe comprobarse que los
datos de entrada son correctos, y si no lo son mostrar un mensaje de error."""

"""try: 
    precio=int(input("Introduce precio: "))
    pedirTipo=input("Tipo de producto: ")

    if pedirTipo in ["A","B","C"]:
        if pedirTipo == "A":
            print("El precio con descuento aplicado es " + str(precio-(precio*0.07)))
        elif pedirTipo == "C" or precio <500:
            print("El precio con descuento aplicado es " + str(precio-(precio*0.12)))
        elif pedirTipo =="B":
            print("El precio con descuento aplicado es " + str(precio-(precio*0.09)))
    else:
        print("Debes introducir tipo correcto \nA.\nB.\nC.")
except:
    print("Introduce valores validos")
"""
    
"""10.Realizar un programa que lea un carácter y dos números enteros por
teclado. Si el carácter leído es un operador aritmético, calcular la operación
correspondiente, si es cualquier otro debe mostrar un error."""

"""char=input("Introduce caracter: ")
num1=int(input("Introduce numero 1: "))
num2=int(input("Introduce numero 2: "))


if char == "+":
    print(f"{num1} + {num2} es {num1+num2}")
elif char == "-":
    print(f"{num1} - {num2} es {num1-num2}")
elif char == "/":
    print(f"{num1} / {num2} es {num1/num2}")
elif char == "//":
    print(f"{num1} // {num2} es {num1//num2}")
elif char == "*":
    print(f"{num1} x {num2} es {num1*num2}")
elif char =="**":
    print(f"{num1} elevado a {num2} es {num1**num2}")
elif char =="%":
    print(f"El resto de la division de {num1} / {num2} es {num1%num2}")
"""
            