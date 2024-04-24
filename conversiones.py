import sys

# Crea los siguientes programas:
# 1. Crear un archivo conversiones.py y una estructura de datos apropiada que permita ingresar tasas de conversión. Las distintas tasas de conversión se deben ingresar mediante sys.argv en el siguiente orden: Sol, Peso Argentino, Dólar Americano. (4 Puntos)
# Para ello considere las siguientes tasas de conversión de Peso Chileno:
# ● a Sol peruano: 0.0046 ● a Peso Argentino: 0.093 ● a Dólar Americano: 0.00013.

# Obtener tasas de conversión
tasa_sol = float(input("Ingrese la tasa de conversión de Peso Chileno a Sol peruano: "))
tasa_peso_arg = float(input("Ingrese la tasa de conversión de Peso Chileno a Peso Argentino: "))
tasa_dolar = float(input("Ingrese la tasa de conversión de Peso Chileno a Dólar Americano: "))

# Obtener valor en pesos chilenos a convertir
valor_pesos_chilenos = float(input("Ingrese el valor en pesos chilenos a convertir: "))

# Realizar conversiones
valor_soles = valor_pesos_chilenos * tasa_sol
valor_peso_argentino = valor_pesos_chilenos * tasa_peso_arg
valor_dolar = valor_pesos_chilenos * tasa_dolar

# Mostrar resultados
print(f"Los {valor_pesos_chilenos:.1f} pesos equivalen a:")
print(f"{valor_soles:.1f} Soles")
print(f"{valor_peso_argentino:.1f} Pesos Argentinos")
print(f"{valor_dolar:.1f} Dólares")
