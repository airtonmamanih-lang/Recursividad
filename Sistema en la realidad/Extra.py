import json
import os
from datetime import datetime
from collections import Counter
import plotly.express as px

# Datos de la universidad en formato JSON
datos_json = """
{
    "Universidad Nacional Mayor de San Marcos": {
        "Facultad de Ingeniería de Sistemas e Informática": {
            "Ingeniería de Sistemas": [
                "Matemática Discreta",
                "Programación de Computadoras I",
                "Introducción a la Computación",
                "Fundamentos de Sistemas de Información",
                "Series y Ecuaciones Diferenciales",
                "Electromagnetismo y Óptica"
            ],
            "Ingeniería de Software": [
                "Algorítmica I",
                "Estadística y Probabilidades",
                "Física Electrónica",
                "Ingeniería Económica",
                "Introducción al Desarrollo de Software",
                "Matemática Básica"
            ],
            "Ciencias de la Computación": [
                "Introducción a la Ciencia de la Computación",
                "Programación de Computadoras I",
                "Desarrollo basado en Plataformas",
                "Series y Ecuaciones Diferenciales",
                "Electromagnetismo y Óptica",
                "Ingeniería Económica",
                "Electromagnetismo y Óptica"
            ],
            "Inteligencia Artificial": [
                "Programación II",
                "Series y Ecuaciones Diferenciales",
                "Algebra Lineal",
                "Física II",
                "Estadística y Probabilidades"
            ]
        },
        "Facultad de Ciencias Contables": {
            "Presupuesto y Finanzas Públicas": [
                "Fundamentos prácticos de Contabilidad y Costos",
                "Matemática Financiera",
                "Estadística Descriptiva y Probabilidades",
                "Economía General",
                "Administración General I",
                "Derecho Constitucional y Civil",
                "Derecho Tributario"
            ]
        },
        "Facultad de Ciencias Económicas": {
            "Economía Pública": [
                "Microeconomía I",
                "Macroeconomía I",
                "Cuentas Nacionales",
                "Matemática para Economía III",
                "Estadística II",
                "Contabilidad Financiera"
            ]
        },
        "Facultad de Ciencias Físicas": {
            "Ingeniería Mecánica de Fluidos": [
                "Geometría Descrptiva",
                "Análisis Vectorial y Tensorial",
                "Física II",
                "Estática",
                "Lenguaje de Programación",
                "Estadística y Probabilidades",
                "Álgebra y Geometría Analítica II"
            ]
        }
    },
    "Universidad Peruanana de Ciencias Aplicadas": {
        "Facultad de Comunicaciones": {
            "Marketing": [
                "Introducción a los Medios Digitales",
                "Informática para el Marketing",
                "Taller de Técnicas de Expresión Escrita",
                "Comportamiento del Consumidor"
            ]
        },
        "Facultad de Derecho": {
            "Derecho Civil": [
                "Derechos de Propiedad",
                "Teoría Constitucional y Política",
                "Fundamentos de la Contractación I",
                "Seminario Integrado de Investigación",
                "Contabilidad para Abogados",
                "Fundamentos de la Gerencia",
                "Taller de Liderazgo II"
            ]
        }
    }
}
"""

universidad = json.loads(datos_json)

contador = Counter()

def mostrar_estructura(elemento, nivel=0):
    if isinstance(elemento, dict):
        for clave, valor in elemento.items():

            if nivel == 0:
                contador["Universidad"] += 1
            elif nivel == 1:
                contador["Facultad"] += 1
            elif nivel == 2:
                contador["Carrera"] += 1

            print("    " * nivel + clave)
            mostrar_estructura(valor, nivel + 1)

    elif isinstance(elemento, list):
        for curso in elemento:
            contador["Curso"] += 1
            print("    " * nivel + curso)

print("=" * 50)
print("SISTEMA DE CURSOS UNIVERSITARIOS")
print("3er Ciclo Académico en la Universidad")
print("=" * 50)

print("\nFecha y hora de ejecución:")
print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

print("\nSistema operativo:")
print(os.name)

print("\nESTRUCTURA ACADÉMICA\n")
mostrar_estructura(universidad)

print("\nRESUMEN")
print("-" * 30)

for categoria, cantidad in contador.items():
    print(f"{categoria}: {cantidad}")

# -----------------------------------
# GRÁFICO DE BARRAS CON PLOTLY
# -----------------------------------

categorias = list(contador.keys())
cantidades = list(contador.values())

fig = px.bar(
    x=categorias,
    y=cantidades,
    text=cantidades,
    color=categorias,
    title="Resumen de la Estructura Académica",
    labels={
        "x": "Categoría",
        "y": "Cantidad"
    }
)

fig.update_traces(textposition="outside")

fig.update_layout(
    title_x=0.5,
    width=900,
    height=500,
    showlegend=False
)

fig.show()