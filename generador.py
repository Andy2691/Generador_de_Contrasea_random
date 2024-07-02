# Generador de contraseñas de manera aleatoria

# Importamos los módulos necesarios
import string  # Este módulo contiene varios conjuntos de caracteres (letras, dígitos, puntuación, etc.)
import random  # Este módulo se utiliza para realizar operaciones aleatorias

# Definimos una función que genera una contraseña
def generar_contraseña(longitud):
    # Concatenamos letras (mayúsculas y minúsculas), dígitos y caracteres de puntuación en una sola cadena
    caracteres = string.ascii_letters + string.digits + string.punctuation
    # Inicializamos una cadena vacía para almacenar la contraseña generada
    contraseña = ""

    # Iteramos 'longitud' veces para generar cada carácter de la contraseña
    for i in range(longitud):
        # Elegimos un carácter al azar de la cadena 'caracteres' y lo añadimos a 'contraseña'
        contraseña += random.choice(caracteres)
    # Devolvemos la contraseña generada
    return contraseña

# Solicitamos al usuario que ingrese la longitud deseada para la contraseña
longitud = int(input("Cual es la longitud de la contraseña?: "))

# Generamos una nueva contraseña llamando a la función con la longitud proporcionada
nueva_contraseña = generar_contraseña(longitud)
# Imprimimos la contraseña generada
print("La nueva contraseña es: ", nueva_contraseña)
