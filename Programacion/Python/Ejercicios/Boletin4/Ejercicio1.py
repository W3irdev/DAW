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
