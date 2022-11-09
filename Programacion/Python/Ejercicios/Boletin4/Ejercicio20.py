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
