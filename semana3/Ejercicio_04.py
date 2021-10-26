mensaje = input("INGRESAR MENSAJE: ")
cifrado = ""
for letra in mensaje:
    if not letra.isalpha():
        continue
    letra = letra.upper()
    codigo = ord(letra)+1
    if codigo > ord("Z"):
        codigo = ord("A")
    cifrado += chr(codigo)
print(cifrado)