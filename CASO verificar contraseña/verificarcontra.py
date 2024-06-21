import re

def verificar_contraseña(contraseña):
    # Verifica la longitud de la contraseña
    if len(contraseña) > 10:
        return "La contraseña supera los 10 caracteres"
    elif len(contraseña) < 8:
        return "La contraseña es menor a 8 caracteres"
    elif 8 <= len(contraseña) <= 10:
        # Verifica que haya al menos una letra mayúscula
        if not re.search(r'[A-Z]', contraseña):
            return "La contraseña no tiene ninguna letra mayúscula"
        
        # Verifica que haya al menos una letra
        if not re.search(r'[A-Za-z]', contraseña):
            return "La contraseña no tiene ninguna letra"
        
        # Verifica que haya al menos un carácter especial
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', contraseña):
            return "La contraseña no tiene ningún carácter especial"
        
        # Verifica que haya al menos un número
        if not re.search(r'\d', contraseña):
            return "La contraseña no tiene ningún número"
        
        # Verifica que haya al menos una letra minúscula
        if not re.search(r'[a-z]', contraseña):
            return "La contraseña no tiene ninguna letra minúscula"
        
        return "La contraseña cumple todas las condiciones"

# Ejemplo de uso
contraseña = "Prueba15!"
resultado = verificar_contraseña(contraseña)
print(resultado)
