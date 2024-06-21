import pandas as pd

def validar_prestamo(edad, ingresos_anuales, historial_crediticio):
    if edad < 18:
        return "Rechazado"
    elif ingresos_anuales < 20000:
        return "Rechazado"
    elif historial_crediticio == "Malo":
        return "Rechazado"
    elif historial_crediticio == "Bueno":
        return "Aprobado"
    else:
        return "Rechazado"

def prueba_caja_negra_prestamos():
    pruebas = [
        (17, 30000, "Bueno", "Rechazado"),           # Caso 1
        (19, 15000, "Bueno", "Rechazado"),           # Caso 2
        (20, 25000, "Malo", "Rechazado"),            # Caso 3
        (25, 30000, "Bueno", "Aprobado"),            # Caso 4
        (18, 20000, "Bueno", "Aprobado"),            # Caso 4 adicional (borde)
        (30, 50000, "Malo", "Rechazado"),            # Caso 3 adicional
        (40, 50000, "Bueno", "Aprobado"),            # Caso 4 adicional
    ]
    
    resultados = []
    
    for i, (edad, ingresos, historial, salida_esperada) in enumerate(pruebas, 1):
        resultado = validar_prestamo(edad, ingresos, historial)
        resultados.append({
            "Caso": i,
            "Edad": edad,
            "Ingresos Anuales": ingresos,
            "Historial Crediticio": historial,
            "Salida Esperada": salida_esperada,
            "Salida Obtenida": resultado,
            "Prueba Pasada": resultado == salida_esperada
        })
    
    df = pd.DataFrame(resultados)
    print(df)

# Ejemplo de uso
prueba_caja_negra_prestamos()
