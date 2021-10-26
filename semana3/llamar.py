from cifrado import*

m = input("Ingresar mensaje a encriptar: ")
c = int(input("Ingresar clave de encriptacion: "))

print(cifrar(m,c))
mc = input("Ingresar mensaje cifrado: ")
cc = int(input("Ingresar clave para descifrar: "))
print(descifrar(mc,cc))