# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Días de la semana (7 días)
# Tercera dimensión: Semanas (4 semanas)
temperaturas = [
    [   # QUEVEDO
        [   # Semana 1
            {"day": "Lunes", "temp": 38},
            {"day": "Martes", "temp": 30},
            {"day": "Miércoles", "temp": 32},
            {"day": "Jueves", "temp": 39},
            {"day": "Viernes", "temp": 35},
            {"day": "Sábado", "temp": 38},
            {"day": "Domingo", "temp": 32}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 36},
            {"day": "Martes", "temp": 39},
            {"day": "Miércoles", "temp": 33},
            {"day": "Jueves", "temp": 31},
            {"day": "Viernes", "temp": 37},
            {"day": "Sábado", "temp": 39},
            {"day": "Domingo", "temp": 33}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 37},
            {"day": "Martes", "temp": 31},
            {"day": "Miércoles", "temp": 35},
            {"day": "Jueves", "temp": 32},
            {"day": "Viernes", "temp": 38},
            {"day": "Sábado", "temp": 31},
            {"day": "Domingo", "temp": 35}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 35},
            {"day": "Martes", "temp": 38},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 39},
            {"day": "Viernes", "temp": 34},
            {"day": "Sábado", "temp": 37},
            {"day": "Domingo", "temp": 31}
        ]
    ],
    [   # GUAYAQUIL
        [   # Semana 1
            {"day": "Lunes", "temp": 32},
            {"day": "Martes", "temp": 34},
            {"day": "Miércoles", "temp": 38},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 33},
            {"day": "Sábado", "temp": 35},
            {"day": "Domingo", "temp": 39}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 33},
            {"day": "Martes", "temp": 36},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 32},
            {"day": "Viernes", "temp": 35},
            {"day": "Sábado", "temp": 37},
            {"day": "Domingo", "temp": 31}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 31},
            {"day": "Martes", "temp": 35},
            {"day": "Miércoles", "temp": 38},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 32},
            {"day": "Sábado", "temp": 36},
            {"day": "Domingo", "temp": 30}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 34},
            {"day": "Martes", "temp": 37},
            {"day": "Miércoles", "temp": 39},
            {"day": "Jueves", "temp": 31},
            {"day": "Viernes", "temp": 34},
            {"day": "Sábado", "temp": 37},
            {"day": "Domingo", "temp": 30}
        ]
    ],
    [   # QUITO
        [   # Semana 1
            {"day": "Lunes", "temp": 20},
            {"day": "Martes", "temp":22},
            {"day": "Miércoles", "temp":24},
            {"day": "Jueves", "temp": 31},
            {"day": "Viernes", "temp": 38},
            {"day": "Sábado", "temp": 35},
            {"day": "Domingo", "temp": 32}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 29},
            {"day": "Martes", "temp": 31},
            {"day": "Miércoles", "temp": 23},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 27},
            {"day": "Sábado", "temp": 24},
            {"day": "Domingo", "temp": 31}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 21},
            {"day": "Martes", "temp": 23},
            {"day": "Miércoles", "temp": 25},
            {"day": "Jueves", "temp": 22},
            {"day": "Viernes", "temp": 29},
            {"day": "Sábado", "temp": 26},
            {"day": "Domingo", "temp": 23}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 28},
            {"day": "Martes", "temp": 30},
            {"day": "Miércoles", "temp": 22},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 26},
            {"day": "Sábado", "temp": 23},
            {"day": "Domingo", "temp": 20}
        ]
    ]
]

# Calcular el promedio de temperaturas para cada ciudad y semana
ciudades = ["QUEVEDO", "GUAYAQUIL", "QUITO"]
for ciudad_idx, ciudad in enumerate(temperaturas):
    for semana_idx, semana in enumerate(ciudad):
        suma_temperaturas = sum([dia["temp"] for dia in semana])
        promedio = suma_temperaturas / len(semana)
        print(f"Promedio de temperaturas en {ciudades[ciudad_idx]}, Semana {semana_idx + 1}: {promedio:.2f} grados")