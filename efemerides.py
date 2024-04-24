# Toda fecha tiene sucesos importantes ¿cómo recordarlos? Las efemérides son conjunto de 
# acontecimientos importantes ocurridos en una misma fecha, por lo que aquí intentaremos 
# utilizar lo aprendido para almacenar eventos importantes y consultarlos.
# Supongamos los siguientes eventos:
# ● 1 de Enero: Año Nuevo
# ● 27 de Febrero: Terremoto en Chile
# ● 8 de Marzo: Día de la mujer
# ● 21 de Mayo: Glorias Navales
# ● 18 de Septiembre: Fiestas Patrias
# ● 19 de Septiembre: Glorias del Ejército
# ● 25 de Diciembre: Navidad

# 2. Disponibilizar estos elementos en Python
# Notamos que queremos almacenar varios elementos en Python, naturalmente esto 
# nos indica que requerimos una estructura de datos, ¿pero cuál?
# Cualquiera sirve para almacenar pero los requerimientos piden también consultarlos.
# Las listas y las tuplas requieren índices por lo que no serían lo más apropiado, por lo 
# que la opción que nos queda son los Diccionarios:

efemerides = {
    "1 de Enero": "Año Nuevo",
    "27 de Febrero": "Terremoto en Chile",
    "8 de Marzo": "Día de la mujer",
    "21 de Mayo": "Glorias Navales",
    "18 de Septiembre": "Fiestas Patrias",
    "19 de Septiembre": "Glorias del Ejército",
    "25 de Diciembre": "Navidad"
}

# 3. Consultar la Fecha
# Mediante input() se puede solicitar al usuario que ingrese la fecha a consultar.

fecha = input('Ingrese una Fecha:').lower()
print("Fecha ingresada", fecha)
for clave, valor in efemerides.items():
    if clave.lower() == fecha:
        print(f"La fecha ingresada celebra: {valor}")
        break

