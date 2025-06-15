# 1) Añadir frutas al diccionario
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

# 2) Actualizar precios
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

# 3) Crear lista solo con nombres de frutas
frutas = list(precios_frutas.keys())
print("Frutas:", frutas)

# 4) Agenda de contactos
contactos = {}
for i in range(5):
    nombre = input("Ingrese nombre del contacto: ")
    numero = input("Ingrese número de teléfono: ")
    contactos[nombre] = numero
consulta = input("Ingrese el nombre a consultar: ")
print("Teléfono:", contactos.get(consulta, "No encontrado"))

# 5) Palabras únicas y conteo de frecuencia
frase = input("Ingrese una frase: ").lower()
palabras = frase.split()
palabras_unicas = set(palabras)
recuento = {}
for palabra in palabras:
    recuento[palabra] = recuento.get(palabra, 0) + 1
print("Palabras únicas:", palabras_unicas)
print("Recuento:", recuento)

# 6) Promedios de alumnos
alumnos = {}
for i in range(3):
    nombre = input("Nombre del alumno: ")
    notas = tuple(int(input(f"Nota {j+1}: ")) for j in range(3))
    alumnos[nombre] = notas
for alumno, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{alumno}: promedio = {promedio:.2f}")

# 7) Estudiantes aprobados en parciales
parcial1 = {"Ana", "Luis", "Juan"}
parcial2 = {"Luis", "Marta", "Juan"}
print("Ambos parciales:", parcial1 & parcial2)
print("Solo uno de los dos:", parcial1 ^ parcial2)
print("Al menos uno:", parcial1 | parcial2)

# 8) Manejo de stock
stock = {"leche": 10, "pan": 5}
producto = input("Consultar/Agregar producto: ")
if producto in stock:
    unidades = int(input("Agregar unidades: "))
    stock[producto] += unidades
else:
    nuevo_stock = int(input("Nuevo producto. Ingrese stock inicial: "))
    stock[producto] = nuevo_stock
print(f"Stock de {producto}: {stock[producto]}")

# 9) Agenda con tuplas como claves
agenda = {
    ("lunes", "10:00"): "reunion",
    ("martes", "15:00"): "clases de ingles"
}
dia = input("Ingrese el día: ")
hora = input("Ingrese la hora: ")
print("Actividad:", agenda.get((dia, hora), "No hay actividades"))

# 10) Invertir diccionario de países y capitales
original = {"argentina": "buenos aires", "chile": "santiago"}
invertido = {capital: pais for pais, capital in original.items()}
print("Invertido:", invertido)
