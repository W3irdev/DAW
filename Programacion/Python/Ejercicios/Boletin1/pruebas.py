#b) Debe ser Falsa si la persona no es un usuario fiable, esto ocurrirá cuando tenga menos de
# 1000 euros en la variable saldo o se haya quedado al descubierto más de 5 veces. Este
# último dato se almacenará en la variable descubierto

cuenta=2000
moroso=6
print(not(cuenta < 1000 or moroso > 5))
