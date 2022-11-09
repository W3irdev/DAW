"""1. Calcular el resultado de las siguientes expresiones logicas"""
#a) 7>=27 and not (7<=2)
print(f"\n1.a) 7>=27 and not (7<=2) es {7>=27 and not (7<=2)}")
#b) 24>5 AND 10<=10 OR 10=5
print(f"\n1.b) 24>5 AND 10<=10 OR 10=5 es {24>5 and 10<=10 or 10==5}")
#c) (10>=15 OR 23=13) AND NOT(8=8)
print(f"\n1.c (10>=15 OR 23=13) AND NOT(8=8) es {(10>=15 or 23==13) and not (8==8)}")
#d) NOT (6/3>3) OR 7>7
print(f"\n1.d NOT (6/3>3) OR 7>7 es {not (6/3>3) or 7>7}")

"""2. Calcular el valor de las siguientes expresiones aritméticas:
"""
#a) 27 mod 4 + 15/4
print(f"\nla solucion de 2.a) es: {27%4+15/4}")
#b) 37/4^2-2
print(f"\nla solucion de 2.b) es: {37/4**2-2}")
#c) 9*2/3*10*3
print(f"\nla solucion de 2.c) es: {9*2/3*10*3}")
#d)(7*3-4*4)^2/4*2
print(f"\nla solucion de 2.d) es: {(7*3-4*4)**2/4*2}")

""" 3. Escribir una expresión lógica que cumpla:
"""
#a) Debe ser Verdadera si el contenido de la variable entera precio es igual o superior a 60 euros pero igual o inferior a 420 euros.
precio=int(input("\nIntroduzca precio para el ejercicio 2.a "))
if precio >= 60 and precio <=420:
    print(bool(precio))
else: print(False)

#b) Debe ser Verdadera si el numero contenido en la variable entera numero es impar
numero=int(input("\nIntroduzca numero para el ejercicio 2.b "))
if numero % 2 ==1:
    print(bool(numero))
else: print(False)

#c) Debe ser Verdadera si las dos variables enteras saldo de una cuenta, y dineroSacar son válidas.
cuenta=1000
dineroSacar=int(input("\nIntroduce dinero a sacar para el ejercicio 3.c "))
if dineroSacar <= cuenta:
    print(True)
else: print(False)

#d) Debe ser Verdadera si las variables enteras hora y minutos son correctas, es decir, que estén comprendidas entre 0:0 y 23:59.
hora =int(input("\nIntroduzca hora para el ejercicio 3.d: "))
minutos =int(input("Introduzca minutos: "))
if hora >=0 and hora <=23 and minutos >=0 and minutos <=59:
    print(f"Son las {hora}:{minutos} ",True)
else: print(False)

#e) Debe ser Verdadera si la variable estadoCivil que almacena el estado civil de una 
# persona no es correcta (S-Soltero, C-Casado, V-Viudo, D-Divorciado).
estadoCivil=input("\nIntroduzca su estado civil. \nS-Soltero\nC-Casado\nV-Viudo\nD-Divorciado\n")
estadoCorrecto=("S","C","V","D","Soltero","Casado","Viudo","Divorciado")
try:
    if estadoCivil not in estadoCorrecto:
        print(True)
    else: print(False)
except:
    print("Introduzca un estado civil")

"""4. Escribir una expresión lógica que cumpla:"""
#a) Debe ser Falsa cuando la variable cantidad que contiene la cantidad a sacar de un cajero
# es superior a 300 euros o negativa.
cantidad=int(input("\nIntroduzca cantidad a sacar para el ejercicio 4.a): "))
if cantidad <0 or cantidad>300:
    print(False)
else: print(True)
#b) Debe ser Falsa si la persona es un adolescente, es decir, la variable edad está entre 16-22 años.
edad=int(input("\nIntroduzca edad para el ejercicio 4.b): "))
if edad >=16 and edad <=22:
    print(False)
else: print(True)
#c) Debe ser Falsa si la variable respuesta a una pregunta de tipo (S/N) es válida.
respuesta=input("\nEjercicio 4.c) S/N\n")
if respuesta == "S" or respuesta == "N":
    print(False)
else: print(True)
#d) Debe ser Falsa si el número contenido en la variable entera numero es múltiplo de 7 o de 3.
numero=int(input("\nIntroduce numero para el ejercicio 4.d): \n"))
if numero %7 == 0 or numero %3 == 0:
    print(False)
else: print(True)

""" 5. Escribir la tabla de verdad para las siguientes expresiones lógicas:"""
#(A OR B) AND NOT(A)
"""
A  | B  |  RESULT
 T | T  |  F
 T | F  |  F
 F | T  |  F
 F | F  |  F  
"""
#b) NOT (A OR B) AND B

"""
A  | B  |  RESULT
T  | T  |     F
T  | F  |     F
F  | T  |     F
F  | F  |     F
"""
#C) A OR NOT (B)
"""
A | B | RESULT
T | T |  T
T | F |  T
F | T |  F
F | F |  T
"""
#  d) NOT ((A AND B) AND (B OR A))
"""
A | B | RESULT
T | T |  F
T | F |  F
F | T |  T
F | F |  T
"""






