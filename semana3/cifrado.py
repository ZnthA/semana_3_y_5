def cifrar(mensaje,clave):
    cifrado = ""
    for letra in mensaje:
        if not letra.isalpha():
            continue
        letra = letra.upper()
        codigo = ord(letra)+clave
        if codigo > ord("Z"):
            codigo = ord("A")
        cifrado+=chr(codigo)
    return cifrado



#desincriptar
def descifrar(mensaje,clave):
    cifrado = ""
    for letra in mensaje:
        if not letra.isalpha():
            continue
        letra = letra.upper()
        codigo = ord(letra)-clave
        if codigo > ord("Z"):
            codigo = ord("A")
        cifrado+=chr(codigo)
    return cifrado
