num1 = input("Digite um Número: ")
try:
    num1conv = int(num1)
    if num1conv > 0:
        print(f"O Número {num1conv} é Positivo")
    elif num1conv < 0:
        print(f"O Número {num1conv} é Negativo")
    else:
        print(f"O Número {num1conv} é Neutro")
except ValueError:
        print("Por favor, digite um número válido.")


