def generar_digito_control(nss):
    nss=str(nss)
    if len(str(nss))==9:
        digito_control=int(nss[:9])%97
    elif len(str(nss))==10:
        digito_control=int(nss[:10])%97
    elif len(str(digito_control))<2:
        digito_control=str("0"+digito_control)

    return digito_control

assert(generar_digito_control("555555555")==83)

def es_emitido_andalucia(nss):
    nss=str(nss)
    valido=False
    try:
        if len(nss)==12:
            if nss[-2:]==str(generar_digito_control(nss[:10])) and nss[:2] in ["04","11","14","18","21","23","29","41"]:
                valido=True
        elif len(nss)==11:
            if nss[-2:]==str(generar_digito_control(nss[:9])) and nss[:2] in ["04","11","14","18","21","23","29","41"]:
                valido=True
    except ValueError:
        valido="Solo puedes introducir numeros"
    return valido

assert(es_emitido_andalucia("110130116424"))