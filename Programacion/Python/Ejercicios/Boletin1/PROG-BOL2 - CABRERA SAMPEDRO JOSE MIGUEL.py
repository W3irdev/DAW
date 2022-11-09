"""Escribir una expresión lógica que cumpla:"""
# a) Debe ser Verdadera si el contenido de las variables enteras sueldo_bruto y sueldo_neto es el adecuado 
# para una retención del 22%

sueldo_bruto=1000
sueldo_neto=780
print(sueldo_neto == sueldo_bruto-(sueldo_bruto*0.22))

#b) Debe ser Verdadera si el contenido de la variable entera día es un valor válido para el mes de mayo.
dia=6
mayo=31
print(dia >0 and dia <= mayo)

#c) Debe ser Verdadera si el número contenido en las variables enteras num1 y num2 son múltiplos de tres.
num1=3
num2=6

print(num1%3==0 and num2%3==0)

#d) Debe ser Verdadera si la calificación contenida en la variable real nota es un aprobado.
nota=3

print(nota<=10 and nota>=5)

#e) Debe ser Verdadera si la media de la calificación contenida en las variables reales nota1, nota2 y nota3 es un aproblado.

nota1=5
nota2=4
nota3=5
media=(nota1+nota2+nota3)/3
print(media>=5)

"""Escribir una expresión lógica que cumpla:"""
#a) Debe ser Falsa si alguna de las calificaciones contenidas en las variables reales nota1, nota2
# y nota3 es un suspenso.

nota1=5
nota2=5
nota3=5
print(not(nota1 < 5 or nota2 < 5 or nota3 < 5))

#b) Debe ser Falsa si la persona no es un usuario fiable, esto ocurrirá cuando tenga menos de
# 1000 euros en la variable saldo o se haya quedado al descubierto más de 5 veces. Este
# último dato se almacenará en la variable descubierto

cuenta=2000
moroso=6
print(not(cuenta < 1000 or moroso > 5))

#c) Debe ser Falsa cuando el valor almacenado en la variable asignaturasAprobadas sea 
# inferior al 30% del valor almacenado en la variable asignaturasCurso.

asignaturasAprobadas=2
asignaturasCurso=10
print(asignaturasAprobadas > asignaturasCurso*0.30)

#d) Debe ser Falsa si los números contenido en las variables enteras mes y día no son válidos. 
# Vamos a considerar que no hay años bisiestos.

mes=28,22,23
dia=31
print(dia < mes)
