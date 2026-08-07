import random

class Ardilla:
    def __init__(self, nombre: str, velocidad: int):
        self.nombre = nombre
        self.velocidad = velocidad
        self.distancia_total = 0

    def avanzar(self):
        # Avanza según su velocidad más un factor de suerte
        self.distancia_total += self.velocidad + random.randint(1, 5)

def simular_carrera1():
    """Ejecuta la carrera 1 y genera los resultados."""
    competidores = [
        Ardilla("Ardilla de la Sierra", 6),
        Ardilla("Ardilla Cafetalera", 7),
        Ardilla("Ardilla Motozintleca", 5)
    ]
    
    meta = 80
    corriendo = True
    
    while corriendo:
        for ardilla in competidores:
            ardilla.avanzar()
            if ardilla.distancia_total >= meta:
                corriendo = False
                
    # Ordenar posiciones de mayor a menor distancia
    ganadores = sorted(competidores, key=lambda x: x.distancia_total, reverse=True)
    
    # Estructurar datos para el HTML
    podio = []
    for posicion, ardilla in enumerate(ganadores, 1):
        podio.append({
            "posicion": posicion,
            "nombre": ardilla.nombre,
            "distancia": ardilla.distancia_total
        })
    return podio

