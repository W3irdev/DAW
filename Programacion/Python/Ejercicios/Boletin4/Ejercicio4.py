#Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto deberá pagar finalmente por su compra.

print("Introduzca el precio del articulo o cesta para saber cuanto tendrá que pagar con descuento del 15% aplicado.")
precio=int(input())

descuento=precio*(0.15)
total=precio-descuento

print(f"En total tendrá que pagar {total}€")