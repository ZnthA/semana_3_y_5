#invertir palabras
# cadena = input("Ingresar palabra: ")
# print(cadena[::-1]) #+1


#Ingresar una cadena de texto y mostrar si es palíndromo o no
cadena = input("Ingresar palabra: ")
if cadena.lower() == cadena[::-1].lower():
    print("Es un palindromo") 
else:
    print("No es un palindromo")