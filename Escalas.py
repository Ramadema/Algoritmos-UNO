import json

# Leer los archivos JSON que contienen los países por región
with open('Regiones/suramerica.json', 'r') as file:
    suramerica = json.load(file)

with open('Regiones/norteamerica.json', 'r') as file:
    norteamerica = json.load(file)


centroamerica = {
    "Guatemala", "Belice", "Honduras", 
    "El Salvador", "Nicaragua", "Costa Rica", 
    "Panamá"
}

# Mtriz de prueba
matriz_vuelos = [
    ["Argentina", "Estados Unidos"],  # Requiere escala
    ["Brasil", "Canadá"],             # Requiere escala
    ["México", "Chile"],              # No requiere escala
    ["Colombia", "México"],           # No requiere escala
    ["Estados Unidos", "Perú"],       # Requiere escala
    ["Argentina", "Costa Rica"],      # No requiere escala
    ["Honduras", "Brasil"],            # No requiere escala
    ["Canadá", "El Salvador"],         # No requiere escala
    ["Perú", "Panamá"],                # No requiere escala
]

# Función para generar escalas
def gestionar_escalas(matriz_vuelos, suramerica, norteamerica):
    print("\n")
    for vuelo in matriz_vuelos:
        pais_salida = vuelo[0]
        pais_llegada = vuelo[1]
        
        # se verifica si es un vuelo de América del Norte a América del Sur
        if pais_salida in norteamerica and pais_llegada in suramerica:
            print(f"El vuelo de {pais_salida} a {pais_llegada} \t\t\trequiere una escala.")

        # se verifica si es un vuelo de América del Sur a América del Norte
        elif pais_salida in suramerica and pais_llegada in norteamerica:
            print(f"El vuelo de {pais_salida} a {pais_llegada} \t\t\trequiere una escala.")
        else:
            print(f"El vuelo de {pais_salida} a {pais_llegada} \t\t\tes directo o dentro de la misma región.")


gestionar_escalas(matriz_vuelos, suramerica, norteamerica)
