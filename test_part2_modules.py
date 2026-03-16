# Importamos las clases que se van a usar
from modules.discount import DiscountEngine
from modules.order import OrderCalculator

# Test para revisar si el cálculo del total funciona bien
def test_order_calculator_uses_discount_engine():

    # Creamos el motor de descuentos
    de = DiscountEngine()

    # Creamos la calculadora de órdenes
    calc = OrderCalculator(de)

    # Probamos algunos valores para ver si el total final es correcto
    assert calc.final_total(120.0, 0.19) == 128.52
    assert calc.final_total(60.0, 0.19) == 67.83
    assert calc.final_total(40.0, 0.19) == 47.6
    assert calc.final_total(40.0, 0.19) == 47.6
    # Caso nuevo: subtotal mayor o igual a 200 (15% de descuento)
    assert calc.final_total(200.0, 0.19) == 202.3
# El test sirve para comprobar que el cálculo del total de la orden funciona bien.

# Se usan diferentes precios para probar varios casos.

# Si todos los assert pasan, significa que el cálculo con descuento e impuesto está correcto.

# Respuesta:

# Es una prueba de integración porque estamos probando cómo el OrderCalculator usa el DiscountEngine para calcular el total final.