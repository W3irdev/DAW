"""1- Crea un programa que tras preguntar por dos números realice la división del mayor
de ellos por el menor y muestre el resultado de la división, es decir, el cociente y el
resto. Solo puedes utilizar la suma o la resta, pero no otras operaciones."""

"""def multiplicacion(n,m):
    memo=0
    memo1=0
    for i in range(m):
        memo=n
        memo1=memo1+memo
    return memo1

m=int(input("Introduzca dividendo: "))
n=int(input("Introduzca divisor: "))

for i in range(m+1):
    if multiplicacion(n,i) <= m:
        cociente=i
if multiplicacion(cociente,n) != m:
    resto=m-multiplicacion(n,cociente)
else:
    resto=0
print(f"{m}/{n} es {cociente} y de resto {resto}")"""

"""2. Diseñar un programa que pida dos números enteros y nos muestre los siguientes
números que son múltiplos del segundo introducido a partir del primero. Por ejemplo,
si introducimos:
13 y 7 ⇒ 14, 21, 28, 35, 42, 49, 56, 63, 70, 77
(a partir de 13 los siguientes 10 múltiplos de 7)
"""

"""try:
    a=int(input("Introduzca limite minimo "))
    b=int(input("Introduzca multiplicador "))

    while (a <=0 or b <=0):
        a=int(input("Introduzca limite minimo "))
        b=int(input("Introduzca multiplicador "))

    contador=1
    multiplo=0
    multiplicador=1
    print(f"{a} y {b} ==>",end=" ")
    while contador < 11:
        multiplo=b*multiplicador
        if multiplo >=a:
            print(f"{multiplo},",end=" ")
            multiplicador+=1
            contador+=1
        else:
            multiplicador+=1

except:
    print("Introduzca valores numericos")"""


"""numInicio, multiplo= 13, 7
inicio=0


for i in range(numInicio, numInicio+multiplo):
    if i % multiplo==0:
        inicio=i
        print(i, i%multiplo)
contador=0
mensaje=""
while contador <10:
    if contador < 9:
        mensaje+= str(inicio)+", "
    else:
        mensaje+= str(inicio)
    inicio+=multiplo
    contador+=1
print(mensaje)"""
"""3. Diseñar un programa que muestre, para cada número introducido por teclado, si es
par, si es positivo y su cuadrado. El proceso se repetirá hasta que el número
introducido por teclado sea 0. Por ejemplo:
4 ⇒ es par, positivo y su cuadrado es 16
-7 ⇒ es impar, negativo y su cuadrado es 49"""

"""try:
    num=int(input("Introduzca un numero para comprobar (Introduzca 0 para cerrar el programa): "))

    while num != 0:
        if num > 0:
            estado="positivo"
        else:
            estado="negativo"
        if num%2==0:
            paridad="par"
        else:
            paridad="impar"    
        print(f"{num} ⇒ es {paridad}, {estado} y su cuadrado es {num**2}")
        num=int(input("Introduzca un numero para comprobar (Introduzca 0 para cerrar el programa): "))
except:
    print("Introduzca valores numericos")
print("Saliendo...")"""

#___________________________________________________________________________________________________________
"""
num=int(input("Introduzca un numero para comprobar (Introduzca 0 para cerrar el programa): "))
while num != 0:
    estado="positivo"
    n="par"

    if num <0:
        estado = "negativo"
    if num%2!=0:
        n="impar"
    print(f"El numero {num} es estado, {n} y su cuadrado es {num**2}")
    num=int(input("Introduzca un numero para comprobar (Introduzca 0 para cerrar el programa): "))
"""


"""4. Diseña un programa que reciba el tamaño de una secuencia numérica y muestre en
una única línea cada una de las siguientes secuencias. Si se recibe el número 6 se
imprimiría:
a. 1, -5, 25, -125, 625, -3125
b. 1, -1, 0, 1, -1, 0
c. 1, 3, 9, 27, 81, 243
"""
"""try:
    num=int(input("Introduzca un numero: "))
    while num <=0:
        num=int(input("Introduzca un numero mayor que 0: "))
    contador=0
    secuencia1=1
    secuencia2=1
    secuencia3=1
    a=""
    b=""
    c=""
    while contador < num:
        secuencia1=(-5)**contador
        if contador == num-1:
            a+=str(f"{secuencia1}")
        else:
            a+=str(f"{secuencia1}, ")
        if contador%3==0:
            secuencia2="1 "
        elif contador%3==1:
            secuencia2="-1 "
        elif contador%3==2:
            secuencia2="0 "
        if contador == num-1:
            b+=f"{secuencia2}"
        else:
            b+=f"{secuencia2}, "
        secuencia3=3**contador
        if contador == num-1:
            c+=str(secuencia3)
        else:
            c+=str(f"{secuencia3}, ")
        contador+=1
    print(f"a. {a}"),print("b. "+b),print("c. "+c)
except:
    print("Introduzca valores numericos")"""

"""5. La secuencia siguiente está definida para el conjunto de los números enteros:
n → n/2 (n es par)
n → 3n + 1 (n es impar)
Utilizando la función anterior y empezando en 13 se genera la siguiente secuencia
de números:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
Esta secuencia tiene 10 términos y se cree que cualquier secuencia termina en 1.
Elabora un programa que pida un número n e imprima una cadena con la secuencia
de números hasta llegar a 1."""

"""n=int(input("Introduzca un numero: "))
mensaje=""
entrada=str(n)
while n <=0:
    n=int(input())
while n != 1:
    if n%2!=0:
        n=int(3*n+1)
        mensaje+=str(n)+ " --> "
    else:
        if n==2:
            n=int(n/2)
            mensaje+=str(n)
        else:
            n=int(n/2)
            mensaje+=str(n)+ " --> "

print(entrada + " --> "+mensaje)"""

"""6. Juan recibe dos tipos de regalos de cumpleaños según el año en el que esté: si el
año es para su familia le regala un puzzle; si es impar, recibe dinero.
Cada nuevo cumpleaños recibe más regalos: así, cada año que recibe puzzles
obtiene el doble que el anterior; sin embargo, si se trata de dinero recibe 15€ más
que en la anterior ocasión.
Elabora un programa que calcule cuántos regalos ha recibido en total Juan, para una
edad determinada sabiendo que en el primer cumpleaños le regalaron un puzzle y
en el segundo 20€.
Ejemplo 1: 1 año ⇒ 1 puzzle
Ejemplo: 2 años ⇒ 1 puzzle y 20€
…..
…..
Ejemplo: 7 años ⇒ 10 puzzles y 170€"""        

"""try:
    año=int(input("Introduzca cuantos años va a cumplir: "))
    contador=1
    recibepuzzle=0
    acumulapuzzle=0
    recibedinero=0
    acumuladinero=0

    while año <=0:
        año=int(input("Los años no pueden ser menor a 1: "))
    while contador < año+1:
        if contador%2==1:
            if contador == 1:
                recibepuzzle=1
                acumulapuzzle=1
            else:
                recibepuzzle*=2
                acumulapuzzle=acumulapuzzle+recibepuzzle

        else:
            if contador==2:
                acumuladinero=20
                recibedinero=20
            else:
                recibedinero=recibedinero+15
                acumuladinero=recibedinero+acumuladinero
        contador+=1
    if año%2==1:
        print(f" {año} años ==> {acumulapuzzle} puzzles y {acumuladinero}€ (tenia {acumuladinero}€ y recibe {recibepuzzle} puzzles)")
    elif año%2==0:
        print(f" {año} años ==> {acumulapuzzle} puzzles y {acumuladinero}€ (tenia {acumulapuzzle} puzzles y recibe {recibedinero}€)")
    else:
        print("Introduzca algun año valido")
except:
    print("Introduzca algun año valido")"""



"""7. Triángulos. Escribe un programa que pida un número y a continuación pinte un
triángulo como los siguientes utilizando el número como símbolo.
"""

"""n=int(input())

for i in range(n+1):
    print((i*str(n)))"""

"""8. Escribe un programa que pregunte por el tipo de figura que quiere pintar y el tamaño
del lado de la figura y genere las figuras correspondientes en el siguiente formato
(los valores 3, 4 y 5 son de ejemplo, podrían pedirse desde 1 hasta 10).
"""
"""tipo=input("Introduzca tipo de figura (CUADRADO, TRIANGULO o ROMBOS): ").upper()
while tipo not in("CUADRADO","TRIANGULO","ROMBOS"):
    tipo=input("Introduzca tipo de figura (CUADRADO, TRIANGULO o ROMBOS): ").upper()

tamaño=int(input("Introduzca tamaño de la figura (1 a 10): "))

while tamaño >10 or tamaño < 1:
    tamaño=int(input())

if tipo =="CUADRADO":
    for i in range(tamaño):
        print(tamaño*" * ")
elif tipo =="TRIANGULO":

    for i in range(-1,tamaño+1):
        if (i+2)%2!=0:
            espacios=tamaño-i
            print(" "*espacios+"* "*(i+2))

elif tipo =="ROMBOS":
    contador=tamaño-1
    for i in range(-1,tamaño+1):
        if (i+2)%2!=0:
            espacios=tamaño-i
            print(" "*espacios+"* "*(i+2))  
    while contador > -2:
        if (contador+2)%2!=0:
            espacios=tamaño-contador
            print(" "*espacios+"* "*(contador+2))
        contador-=1
else:
    print("Introduzca un tipo de figura valido")
"""

"""9. Crea un programa nuevo basado en el anterior que genere las mismas figuras, pero
vacías:
"""

"""tipo=input("Introduzca tipo de figura (CUADRADO, TRIANGULO o ROMBOS): ").upper()
while tipo not in("CUADRADO","TRIANGULO","ROMBOS"):
    tipo=input("Introduzca tipo de figura (CUADRADO, TRIANGULO o ROMBOS): ").upper()

tamaño=int(input("Introduzca tamaño de la figura: "))

while tamaño >10 or tamaño < 1:
    tamaño=int(input("Introduzca tamaño de la figura: "))

if tipo =="CUADRADO":
    for i in range(tamaño):
        if i == 0 or i == tamaño-1:
            print(tamaño*"* ")
        else:
            print("* "+(tamaño-2)*"  "+"*")
elif tipo =="TRIANGULO":
    for i in range(-1,tamaño):
        espacios=tamaño-i
        espaciado=i*2
        if i ==-1 or i == tamaño-1:
            if (i+2)%2!=0:
                print(" "*espacios+"* "*(i+2))
        else:
            print(espacios*" "+"*"+espaciado*" "+" *")
elif tipo =="ROMBOS":
    contador=tamaño-1
    for i in range(-1,tamaño):
        espacios=tamaño-i
        espaciado=i*2
        if i ==-1:
            if (i+2)%2!=0:
                espacios=tamaño-i
                print(" "*espacios+"* "*(i+2))
        else:
            if (i+2)%2!=0:
                espacios=tamaño-i
                print(espacios*" "+"*"+espaciado*" "+" *")
    while contador > -2:
        espacios=tamaño-contador
        espaciado=contador*2
        if contador == -1:
            if (contador+2)%2!=0:
                print(" "*espacios+"* "*(contador+2))
        else:
            if (contador+2)%2!=0:
                print(" "*espacios+"*"+espaciado*" "+" *")
        contador-=1
else:
    print("Introduzca un tipo de figura valido")"""

"""10. Modifica el programa anterior para que en lugar de un asterisco podamos utilizar
cualquier otro caracter"""


"""tipo=input("Introduzca tipo de figura (CUADRADO, TRIANGULO o ROMBOS): ").upper()
figura=input("Introduzca caracter para usar de figura: ")
while tipo not in("CUADRADO","TRIANGULO","ROMBOS"):
    tipo=input("Introduzca tipo de figura (CUADRADO, TRIANGULO o ROMBOS): ").upper()

tamaño=int(input("Introduzca tamaño de la figura: "))

while tamaño >10 or tamaño < 1:
    tamaño=int(input("Introduzca tamaño de la figura: "))

if tipo =="CUADRADO":
    for i in range(tamaño):
        if i == 0 or i == tamaño-1:
            print(tamaño*(figura+" "))
        else:
            print(figura+" "+(tamaño-2)*"  "+figura)
elif tipo =="TRIANGULO":
    for i in range(-1,tamaño):
        espacios=tamaño-i
        espaciado=i*2
        if i ==-1 or i == tamaño-1:
            if (i+2)%2!=0:
                print(" "*espacios+(figura+" ")*(i+2))
        else:
            print(espacios*" "+figura+espaciado*" "+" "+figura)
elif tipo =="ROMBOS":
    contador=tamaño-1
    for i in range(-1,tamaño):
        espacios=tamaño-i
        espaciado=i*2
        if i ==-1:
            if (i+2)%2!=0:
                espacios=tamaño-i
                print(" "*espacios+(figura+" ")*(i+2))
        else:
            if (i+2)%2!=0:
                espacios=tamaño-i
                print(espacios*" "+figura+espaciado*" "+" "+figura)
    while contador > -2:
        espacios=tamaño-contador
        espaciado=contador*2
        if contador == -1:
            if (contador+2)%2!=0:
                print(" "*espacios+(figura+" ")*(contador+2))
        else:
            if (contador+2)%2!=0:
                print(" "*espacios+figura+espaciado*" "+" "+figura)
        contador-=1
else:
    print("Introduzca un tipo de figura valido")"""

"""11. Cuadrado de números:
Crea un programa que lea del teclado un número y genere un cuadrado con el patrón siguiente
donde cada elemento está separado por un espacio.
"""

"""try:
    num=int(input("Introduzca numero 1-9 para generar el patron (Ejecute 0 para salir): "))

    while num < 0 or num > 9:
        num=int(input("Introduzca numero 1-9 para generar el patron (Ejecute 0 para salir): "))

    while num > 0:

        numfix=num
        figura=""
        matriz=[]
        cuadrado=""
        izquierdo=""
        matrizcuadrado=[]
        cuadrado2=""
        matrizcuadrado2=[]
        for i in range(num,0,-1):
            figura=(i-1)*(str(num)+" ")
            cuadrado+=f"{num} "
            matriz.append(cuadrado)
            matrizcuadrado.append(figura)
            matrizcuadrado2.append(cuadrado2)
            
            num-=1
            izquierdo+=f"\n{cuadrado+figura*2+cuadrado2}"
            if i == 1:
                pass
            else:
                cuadrado2=str(i)+" "+cuadrado2

        contador=numfix-1
        cuadradoinverso=""
        cuadradobajo=""
        while contador >0:
            cuadradoinverso+=f"\n{matriz[contador-1]}{2*matrizcuadrado[contador-1]}{matrizcuadrado2[contador-1]}"
            contador-=1


        total=f"{izquierdo}{cuadradoinverso}"

        print(total)
        num=int(input("Introduzca numero 1-9 para generar el patron (Ejecute 0 para salir): "))
except:
    print("No puede dejar en blanco el dato")
"""