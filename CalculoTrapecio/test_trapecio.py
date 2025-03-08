import unittest
from trapecio import calcular_area_trapecio  # Importamos la función a probar

class TestCalculoTrapecio(unittest.TestCase):
    
    def test_area_valores_correctos(self):
        """Prueba con valores normales"""
        self.assertEqual(calcular_area_trapecio(10, 6, 5), 40.0)
        self.assertEqual(calcular_area_trapecio(8, 4, 3), 18.0)
        self.assertEqual(calcular_area_trapecio(15, 10, 7), 87.5)

    def test_area_valores_decimales(self):
        """Prueba con valores decimales"""
        self.assertAlmostEqual(calcular_area_trapecio(10.5, 6.3, 5.2), 43.68, places=2)
        self.assertAlmostEqual(calcular_area_trapecio(7.1, 3.4, 4.2), 22.05, places=2)

    def test_area_base_mayor_menor_iguales(self):
        """Prueba cuando la base mayor y menor son iguales"""
        self.assertEqual(calcular_area_trapecio(5, 5, 4), 20.0)

    def test_area_con_cero(self):
        """Prueba cuando alguna entrada es cero"""
        self.assertEqual(calcular_area_trapecio(0, 6, 5), 0)
        self.assertEqual(calcular_area_trapecio(10, 0, 5), 0)
        self.assertEqual(calcular_area_trapecio(10, 6, 0), 0)

    def test_area_valores_negativos(self):
        """Prueba con valores negativos"""
        with self.assertRaises(ValueError):
            calcular_area_trapecio(-10, 6, 5)
        
        with self.assertRaises(ValueError):
            calcular_area_trapecio(10, -6, 5)

        with self.assertRaises(ValueError):
            calcular_area_trapecio(10, 6, -5)

if __name__ == "__main__":
    unittest.main()
