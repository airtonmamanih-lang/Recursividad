import matplotlib.pyplot as plt
from IPython.display import clear_output
import time

n = int(input("Ingrese la cantidad de discos: "))

torres = {
    'A': list(range(n, 0, -1)),
    'B': [],
    'C': []
}

contador = 0
movimiento_actual = "Estado inicial"
historial = []

def dibujar():
    clear_output(wait=True)

    fig, ax = plt.subplots(figsize=(10, 5))

    posiciones = {'A': 1, 'B': 2, 'C': 3}

    for torre, discos in torres.items():
        x = posiciones[torre]

        ax.plot([x, x], [0, n + 1], linewidth=5)

        for nivel, disco in enumerate(discos):

            ancho = disco * 0.18

            ax.barh(
                nivel + 1,
                ancho,
                left=x - ancho / 2,
                height=0.5
            )

            ax.text(
                x,
                nivel + 1,
                str(disco),
                ha='center',
                va='center',
                fontsize=12,
                fontweight='bold'
            )

    ax.set_xlim(0.5, 3.5)
    ax.set_ylim(0, n + 2)

    ax.set_xticks([1, 2, 3])
    ax.set_xticklabels(["A", "B", "C"])

    ax.set_title("TORRE DE HANOI")

    plt.figtext(
        0.5,
        0.02,
        f"Movimiento {contador}: {movimiento_actual}",
        ha="center",
        fontsize=12
    )

    plt.show()

def mover(origen, destino):
    global contador, movimiento_actual

    disco = torres[origen].pop()
    torres[destino].append(disco)

    contador += 1

    movimiento_actual = f"Disco {disco}: {origen} → {destino}"

    historial.append((contador, disco, origen, destino))

    print(f"Movimiento {contador}: Disco {disco} de {origen} a {destino}")

    dibujar()
    time.sleep(0.8)

def hanoi(n, origen, auxiliar, destino):

    if n == 1:
        mover(origen, destino)

    else:
        hanoi(n - 1, origen, destino, auxiliar)

        mover(origen, destino)

        hanoi(n - 1, auxiliar, origen, destino)

dibujar()
time.sleep(1)

hanoi(n, 'A', 'B', 'C')

print("\n" + "="*50)
print("RESUMEN DE MOVIMIENTOS")
print("="*50)

for num, disco, origen, destino in historial:
    print(f"{num:2d}. Disco {disco}: {origen} → {destino}")

print("\nTotal de movimientos:", contador)
print("Mínimo teórico:", 2**n - 1)

print("\nEstado final de las torres:")
print("A:", torres['A'])
print("B:", torres['B'])
print("C:", torres['C'])