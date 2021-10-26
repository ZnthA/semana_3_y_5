"""Crea un programa que pida introducir una dirección de email
por teclado. El programa debe imprimir en consola si la dirección
de email es correcta o no en función de si esta tiene el símbolo
‘@’. Si tiene una ‘@’ la dirección será correcta. Si tiene más de una
o ninguna ‘@’ la dirección será errónea. Si la ‘@’ está al comienzo de
la dirección de email o al final, la dirección
también será errónea,"""


direccion = input("Ingresar direccion email: ")
arroba = direccion.count("@")
if arroba !=1 or direccion.rfind("@") == (len(direccion)-1) or direccion.find("@") == 0: 
    print("Dirección Email incorrecta")
else:
    print("Dirección Email correcta")