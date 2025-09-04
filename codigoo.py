# Reto 2 - Agua en un edificio
# Programa con las preguntas del taller

# Pedir datos al usuario
consumo_por_persona = float(input("¿Cuál es el consumo promedio de agua por persona en litros/día?: "))
personas = int(input("¿Cuántas personas viven en el edificio?: "))
capacidad_tanque = float(input("¿Cuál es la capacidad de cada tanque en litros?: "))
eficiencia = float(input("¿Cuál es la eficiencia del tanque en %?: ")) / 100
dias_inactivos = int(input("¿Cuántos días al año está inactivo el sistema por mantenimiento?: "))
area_por_tanque = float(input("¿Cuántos metros cuadrados ocupa un tanque?: "))
area_disponible = float(input("¿Cuál es el área total disponible en metros cuadrados?: "))

# Cálculos
consumo_diario = consumo_por_persona * personas
consumo_anual = consumo_diario * 365
consumo_total = consumo_anual + (consumo_diario * dias_inactivos)
capacidad_util = capacidad_tanque * eficiencia
tanques = consumo_total / capacidad_util
area_total = tanques * area_por_tanque
autonomia = (tanques * capacidad_util) / consumo_diario
litros_por_persona = (tanques * capacidad_util) / (personas * 30)

# Resultados
print("\n=== Resultados del Taller ===")
print("Consumo diario del edificio:", consumo_diario, "litros")
print("Consumo anual del edificio:", consumo_anual, "litros")
print("Consumo total con días extra:", consumo_total, "litros")
print("Capacidad útil de un tanque:", capacidad_util, "litros")
print("Número de tanques necesarios (aprox):", tanques)
print("Área total requerida:", area_total, "m2")
print("Área disponible:", area_disponible, "m2")
print("Autonomía del sistema (días):", autonomia)
print("Litros por persona en 30 días de sequía:", litros_por_persona)
