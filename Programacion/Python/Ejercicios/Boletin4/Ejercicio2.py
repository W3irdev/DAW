# Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius.

print("Esto es un convertidor de Fº a Cº introduzca el valor en grados Fahrenheit a continuación: ")

fahrenheit = float(input())
celcius= float((fahrenheit-32)*5/9)
print(f"{fahrenheit}ºF en grados centigrados es {celcius}ºC")