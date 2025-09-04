# Reto 2 - Calculo de agua en un edificio

# Datos de entrada
consumo_por_persona = 150   # litros por día
personas = 80
capacidad_tanque = 10000    # litros
eficiencia = 0.9            # 90 %
dias_inactivos = 10
area_por_tanque = 2.5     
area_disponible = 300     

# Cálculos
consumo_diario = consumo_por_persona * personas
consumo_anual = consumo_diario * 365
consumo_total = consumo_anual + (consumo_diario * dias_inactivos)
capacidad_util = capacidad_tanque * eficiencia
tanques = -(-consumo_total // capacidad_util) 
area_total = tanques * area_por_tanque
autonomia = (tanques * capacidad_util) / consumo_diario
litros_por_persona = (tanques * capacidad_util) / (personas * 30)

# Resultados
print("Consumo diario:", consumo_diario, "L")
print("Consumo anual:", consumo_anual, "L")
print("Consumo total:", consumo_total, "L")
print("Capacidad útil por tanque:", capacidad_util, "L")
print("Tanques necesarios:", tanques)
print("Área requerida:", area_total, "m2")
print("Área disponible:", area_disponible, "m2")
print("Autonomía:", autonomia, "días")
print("Litros por persona en 30 días de sequía:", litros_por_persona, "L/día")
