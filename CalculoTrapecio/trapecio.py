def calcular_area_trapecio(base_mayor, base_menor, altura):
    """
    Calcula el área de un trapecio.

    Parámetros:
    base_mayor (float): La base mayor del trapecio.
    base_menor (float): La base menor del trapecio.
    altura (float): La altura del trapecio.

    Retorna:
    float: El área calculada.

    Lanza:
    ValueError: Si alguna entrada es menor o igual a 0.
    """
    if base_mayor <= 0 or base_menor <= 0 or altura <= 0:
        raise ValueError("⚠️ Error: Las bases y la altura deben ser mayores que 0.")
    return ((base_mayor + base_menor) * altura) / 2


def main():
    """Función principal para interactuar con el usuario"""
    print("\n--- Cálculo del Área de un Trapecio ---")

    try:
        base_mayor = float(input("Ingrese la base mayor: "))
        base_menor = float(input("Ingrese la base menor: "))
        altura = float(input("Ingrese la altura: "))

        # Validar que los valores sean positivos
        if base_mayor <= 0 or base_menor <= 0 or altura <= 0:
            print("⚠️ Error: Todos los valores deben ser mayores que 0.")
            return

        # Calcular área
        area = calcular_area_trapecio(base_mayor, base_menor, altura)

        # Mostrar resultado
        print(f"\n✅ El área del trapecio con base mayor {base_mayor}, base menor {base_menor} y altura {altura} es: {area:.2f} unidades cuadradas.\n")

    except ValueError:
        print("⚠️ Error: Por favor, ingrese solo números válidos.")

# Ejecutar el programa
if __name__ == "__main__":
    main()
