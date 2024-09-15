def calcular_temperatura_promedio(temperaturas):
    """
    Calcula la temperatura promedio de cada ciudad a partir de un diccionario
    con datos de temperaturas.

    Args:
    temperaturas (dict): Un diccionario donde las llaves son nombres de ciudades
                         y los valores son listas de temperaturas.

    Returns:
    dict: Un diccionario con la temperatura promedio para cada ciudad.
    """
    promedios = {}

    for ciudad, temps in temperaturas.items():
        if temps:  # Verifica que la lista de temperaturas no esté vacía
            promedio = sum(temps) / len(temps)
            promedios[ciudad] = promedio
        else:
            promedios[ciudad] = None  # Si no hay datos, se asigna None

    return promedios


# Ejemplo de uso:
datos_temperaturas = {
    'GUAYAQUIL': [22.5, 23.0, 21.5, 22.0],
    'QUEVEDO': [18.5, 19.0, 18.0, 20.0],
    'QUITO': [25.0, 26.5, 24.0, 23.5]
}

print(calcular_temperatura_promedio(datos_temperaturas))