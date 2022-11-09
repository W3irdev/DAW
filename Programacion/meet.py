import webbrowser

pantalla="################MEET################\n1. Base de datos\n2. Programacion\n3. Sistemas Informaticos\n4. Lenguaje de marcas\n5. Entorno de desarrollo\n6. Salir\n################MEET################"
print(pantalla)
menu=int(input("\nIntroduce clase meet (6 para mostrar menu): "))

while menu not in range(1,6):
    menu=int(input("\nIntroduce clase meet (6 para mostrar menu): "))

if menu==1:
    webbrowser.open("https://meet.google.com/rgh-zvfr-bsr?pli=1&authuser=1")
elif menu==2:
    webbrowser.open("https://meet.google.com/scc-qbnw-zcr")
elif menu==3:
    webbrowser.open("https://meet.google.com/obk-mxip-bmn")
elif menu==4:
    webbrowser.open("https://meet.google.com/qjm-kjcm-zrc")
elif menu==5:
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley")
else:
    menu==6
