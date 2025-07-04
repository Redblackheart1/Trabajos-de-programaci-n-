# 1) Factorial recursivo y mostrar factoriales hasta número dado
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Ingrese un número entero positivo para factoriales: "))
for i in range(1, num + 1):
    print(f"Factorial de {i}: {factorial(i)}")


# 2) Fibonacci recursivo y mostrar la serie hasta posición dada
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

pos = int(input("\nIngrese la posición hasta la que quiere la serie Fibonacci: "))
print("Serie Fibonacci hasta posición", pos)
for i in range(pos + 1):
    print(fibonacci(i), end=" ")
print()


# 3) Potencia recursiva (base^exponente)
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

b = float(input("\nIngrese la base: "))
e = int(input("Ingrese el exponente (entero positivo): "))
print(f"{b} elevado a {e} es {potencia(b, e)}")


# 4) Decimal a binario recursivo (devuelve string)
def decimal_a_binario(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

num_decimal = int(input("\nIngrese un número entero positivo para convertir a binario: "))
print(f"Binario: {decimal_a_binario(num_decimal)}")


# 5) Función recursiva para verificar si una palabra es palíndromo
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

palabra_input = input("\nIngrese una palabra (sin espacios ni tildes) para verificar palíndromo: ")
print("¿Es palíndromo?", es_palindromo(palabra_input))


# 6) Suma recursiva de dígitos sin convertir a string
def suma_digitos(n):
    if n == 0:
        return 0
    else:
        return n % 10 + suma_digitos(n // 10)

num_suma = int(input("\nIngrese un número entero positivo para sumar sus dígitos: "))
print("Suma de dígitos:", suma_digitos(num_suma))


# 7) Contar bloques para la pirámide recursiva
def contar_bloques(n):
    if n <= 1:
        return n
    else:
        return n + contar_bloques(n - 1)

niveles = int(input("\nIngrese la cantidad de bloques del nivel más bajo: "))
print("Total bloques en la pirámide:", contar_bloques(niveles))


# 8) Contar cuántas veces aparece un dígito en un número entero
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        return (1 if numero % 10 == digito else 0) + contar_digito(numero // 10, digito)

numero_buscar = int(input("\nIngrese un número entero positivo: "))
digito_buscar = int(input("Ingrese el dígito a buscar (0-9): "))
print(f"El dígito {digito_buscar} aparece {contar_digito(numero_buscar, digito_buscar)} veces en {numero_buscar}.")

