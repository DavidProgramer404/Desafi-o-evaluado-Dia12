import sys

# Verificar si se proporcionó el nombre del archivo como argumento
if len(sys.argv) != 2:
    print("Uso: python word_count.py <texto_txt>")
    sys.exit(1)

# Obtener el nombre del archivo del argumento de línea de comandos
texto_txt = sys.argv[1]

# Inicializar listas para contar caracteres y palabras distintas
caracteres_distintos = []
palabras_distintas = []

# Leer el contenido del archivo
with open(texto_txt, "r") as file:
    texto = file.read()

# Contar caracteres distintos
for caracter in texto:
    if caracter not in caracteres_distintos:
        caracteres_distintos.append(caracter)

# Contar palabras distintas
palabras = texto.split()
for palabra in palabras:
    if palabra not in palabras_distintas:
        palabras_distintas.append(palabra)

# Mostrar resultados
print(f"El número de caracteres distintos es: {len(caracteres_distintos)}")
print(f"El número de palabras distintas es: {len(palabras_distintas)}")
# python word_count.py lorem_ipsum.txt
"""

"""