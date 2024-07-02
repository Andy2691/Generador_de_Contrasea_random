#Generador de contraseñas de manera randomica 
import string
import random 


def generar_contraseña(longitud):
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&'*+,-."
    contraseña = ""

    for i  in range(longitud):
        contraseña += random.choice(caracteres)
    return contraseña

longitud = int(input("Cual es la longitud de la contraseña?: ") ) 


nueva_contraseña = generar_contraseña(longitud)
print("La nueva contraseña es : ", nueva_contraseña)
