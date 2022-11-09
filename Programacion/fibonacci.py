""" 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 114

"""

n=int(input("Introduzca tamaño secuencia: "))
a=0
b=1
c=0
contador=1
salida=""
while(contador<=n+1):
    a=b
    b=c
    if c==0:
        c=a+b
    elif contador==n+1:
        salida+=f"{c}"
    else:	    
        salida+=f"{c}, "	
    c=a+b
    contador+=1
print(salida)