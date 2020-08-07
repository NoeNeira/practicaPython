"""
Crear un diccionario con 10 estudiantes y sus respectivas notas.
Luego crear una función que nos informe los estudiantes aprobados (nota >= 7),los estudiantes desaprobados 
(4 <= nota < 7) y los estudiantes aplazados (0 <= nota < 4).
"""

notasAlumnos = {
    "García": 10,
    "Suarez": 7,
    "Rodríguez": 2,
    "Gómez": 5,
    "Gonzalez": 6,
    "Leiva": 7,
    "Lopez": 1,
    "Fernandez": 9,
    "Perez": 4,
    "Martinez": 9
}

def getCondicionEstudiante(notasAlumnos):
    estudiantesAprobados = []
    estudiantesDesaprobados = []
    estudiantesAplazados = []
    for apellido, nota in notasAlumnos.items():
        if nota >=7:
            estudiantesAprobados.append(apellido)
        elif 4 <= nota < 7:
            estudiantesDesaprobados.append(apellido)
        else:
            estudiantesAplazados.append(apellido)

    print(estudiantesAprobados)
    print(estudiantesDesaprobados)
    print(estudiantesAplazados)        
               
getCondicionEstudiante(notasAlumnos)
