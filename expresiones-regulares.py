import re

patron = re.compile('[A-Z][0-9][0-9][0-9][a-z][a-z][a-z]...')

print("Las condiciones para crear la contraseña son: Primera letra mayúscula, 3 números consecutivos, 3 letras minúsculas consecutivas y 3 caracteres especiales.\n\n")
sw = 1
while(sw == 1):
    passw = input("Ingrese su contraseña: ")

    if patron.match(passw):
        print("\nSu contraseña es válida")
        sw = 0 

    else:
        print("\nDebe ingresar una contraseña válida\n\n")
        sw = 1


input()

#Santiago Piedriz, Henry Núñez
