import random
from collections import Counter

TOTAL_COFRES = 10_000

boletos = (
    ["Común"] * 1385
    + ["Raro"] * 509
    + ["Épico"] * 106
)


def simular():
    resultados = [random.choice(boletos) for _ in range(TOTAL_COFRES)]
    conteo = Counter(resultados)

    print(f"Simulación de {TOTAL_COFRES:,} aperturas de cofres\n")
    print(f"{'Tipo':<12}{'Cantidad':>12}{'Porcentaje':>14}")

    for tipo in ("Común", "Raro", "Épico"):
        cantidad = conteo[tipo]
        porcentaje = cantidad / TOTAL_COFRES * 100
        print(f"{tipo:<12}{cantidad:>12,}{porcentaje:>13.1f}%")

    print(f"{'Total':<12}{TOTAL_COFRES:>12,}{100.0:>13.1f}%")


if __name__ == "__main__":
    simular()
