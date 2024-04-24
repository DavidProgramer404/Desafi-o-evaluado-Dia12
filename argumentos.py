import sys


# 3. Dentro de este módulo, llamaremos a la propiedad argv, la cual corresponde a la lista de los argumentos introducidos en el terminal.
# El primer argumento (cuando se ejecuta un script) es el nombre del mismo, y se encuentra ubicado en la posición 0 de la lista de argumentos.
# Todo lo que se escriba después del nombre del script, corresponderá a los argumentos siguientes.
# Crearemos una variable nombre, a la cual le asignaremos el argumento en la posición 1 de la lista de argumentos y la variable apellido con la posición 2, de la siguiente forma:

nombre = sys.argv[1]
apellido = sys.argv[2]
edad = sys.argv[3]

# 4. Ahora visualicemos los resultados ingresados agregando lo siguiente:

print(f'Mi nombres es : {nombre}')
print(f'Mi apellido es : {apellido}')
print(f'y mi edad es : {edad}')
print(f'nombre de este archivo es {sys.argv[0]}')


# 5. Para ejecutar este script, se debe ingresar en la terminal el siguiente comando: py argumento.py Carlos Santana

# Ejecutamos type para que veamos las listas se aplicaran en el sys.argv

print(type(sys.argv))
