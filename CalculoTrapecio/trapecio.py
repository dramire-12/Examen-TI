def calcular_area_trapecio(base_mayor, base_menor, altura):
    """
    Calcula el área de un trapecio.

    Parámetros:
    base_mayor (float): La base mayor.
    base_menor (float): La base menor.
    altura (float): La altura.

    Retorna:
    float: Área calculada.
    """
    if base_mayor <= 0 or base_menor <= 0 or altura <= 0:
        raise ValueError("⚠️ Error: Las bases y la altura deben ser mayores que 0.")
    return ((base_mayor + base_menor) * altura) / 2


def calcular_perimetro_trapecio(base_mayor, base_menor, lado1, lado2):
    """
    Calcula el perímetro de un trapecio.

    Parámetros:
    base_mayor (float): La base mayor.
    base_menor (float): La base menor.
    lado1 (float): Uno de los lados no paralelos.
    lado2 (float): Otro de los lados no paralelos.

    Retorna:
    float: Perímetro calculado.
    """
    if base_mayor <= 0 or base_menor <= 0 or lado1 <= 0 or lado2 <= 0:
        raise ValueError("⚠️ Error: Todas las medidas deben ser mayores que 0.")
    return base_mayor + base_menor + lado1 + lado2


def main():
    """Menú interactivo para el cálculo de área y perímetro del trapecio"""
    print("\n--- Cálculo del Área y Perímetro de un Trapecio ---")

    try:
        base_mayor = float(input("Ingrese la base mayor: "))
        base_menor = float(input("Ingrese la base menor: "))
        altura = float(input("Ingrese la altura: "))

        if base_mayor <= 0 or base_menor <= 0 or altura <= 0:
            print("⚠️ Error: Las bases y la altura deben ser mayores que 0.")
            return

        print("\nOpciones disponibles:")
        print("1. Calcular solo el área")
        print("2. Calcular solo el perímetro")
        print("3. Calcular ambos (área y perímetro)")

        opcion = input("Seleccione una opción (1/2/3): ")

        if opcion == "1":
            area = calcular_area_trapecio(base_mayor, base_menor, altura)
            print(f"\n✅ El área del trapecio es: {area:.2f} unidades cuadradas.")

        elif opcion == "2":
            lado1 = float(input("Ingrese el primer lado no paralelo: "))
            lado2 = float(input("Ingrese el segundo lado no paralelo: "))

            if lado1 <= 0 or lado2 <= 0:
                print("⚠️ Error: Los lados deben ser mayores que 0.")
                return

            perimetro = calcular_perimetro_trapecio(base_mayor, base_menor, lado1, lado2)
            print(f"\n✅ El perímetro del trapecio es: {perimetro:.2f} unidades.")

        elif opcion == "3":
            lado1 = float(input("Ingrese el primer lado no paralelo: "))
            lado2 = float(input("Ingrese el segundo lado no paralelo: "))

            if lado1 <= 0 or lado2 <= 0:
                print("⚠️ Error: Los lados deben ser mayores que 0.")
                return

            area = calcular_area_trapecio(base_mayor, base_menor, altura)
            perimetro = calcular_perimetro_trapecio(base_mayor, base_menor, lado1, lado2)

            print(f"\n✅ Área del trapecio: {area:.2f} unidades cuadradas.")
            print(f"✅ Perímetro del trapecio: {perimetro:.2f} unidades.")

        else:
            print("⚠️ Opción no válida. Intente nuevamente.")

    except ValueError:
        print("⚠️ Error: Por favor, ingrese solo números válidos.")

if __name__ == "__main__":
    main()
