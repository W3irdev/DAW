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
