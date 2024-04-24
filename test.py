efemerides = {
    "1 de Enero": "Año Nuevo",
    "27 de Febrero": "Terremoto en Chile",
    "8 de Marzo": "Día de la mujer",
    "21 de Mayo": "Glorias Navales",
    "18 de Septiembre": "Fiestas Patrias",
    "19 de Septiembre": "Glorias del Ejército",
    "25 de Diciembre": "Navidad"
}

fecha = input('Ingrese una Fecha:').lower()

# Lista de posibles formatos de la fecha
posibles_fechas = list(efemerides.keys())

# Buscar el evento asociado a la fecha ingresada

for fecha_posible in posibles_fechas:
    if fecha in fecha_posible.lower():
        evento = efemerides[fecha_posible]
        break

if evento:
    print(f'Efemérides: {evento}')
else:
    print('No hay eventos para esta fecha.')