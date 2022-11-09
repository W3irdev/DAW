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

"""Solucion aportada en hackerrank

def is_leap(year):
    leap = False
    
    # Write your logic here
    if year %4!=0:
        leap= False
    if year %4==0 and year %100!=0: 
        leap= True      
    if year %4==0 and year %100==0 and year %400==0:
        leap= True
    return leap

year = int(input())
print(is_leap(year))"""