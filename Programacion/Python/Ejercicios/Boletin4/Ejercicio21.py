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
    



