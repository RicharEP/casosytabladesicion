import random
import string

def generar_contraseña():
    longitud = random.randint(8, 10)
    
    letras_mayusculas = random.choices(string.ascii_uppercase, k=1)
    letras_minusculas = random.choices(string.ascii_lowercase, k=1)
    numeros = random.choices(string.digits, k=1)
    caracteres_especiales = random.choices(string.punctuation, k=1)

    restantes = longitud - 4  # Ya tenemos 4 caracteres obligatorios

    todos_caracteres = letras_mayusculas + letras_minusculas + numeros + caracteres_especiales
    todos_caracteres += random.choices(string.ascii_letters + string.digits + string.punctuation, k=restantes)
    
    random.shuffle(todos_caracteres)

    return ''.join(todos_caracteres)

# Ejemplo de uso
contraseña = generar_contraseña()
print("Contraseña generada:", contraseña)
