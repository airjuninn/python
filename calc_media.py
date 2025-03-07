nome = input("Digite o nome do aluno: \n")

while not nome.isalpha():
    print("O nome deve conter apenas letras.")
    nome = input("Digite o nome do aluno: \n")

# Laço para garantir que o número esteja entre 0 e 10
def obter_nota(ordem):
    while True:
        try:
            nota = float(input(f"Digite a {ordem}ª nota: \n"))
            if 0 <= nota <= 10:
                return nota
            else:
                print("A nota deve estar entre 0 e 10. Tente novamente.")
        except ValueError:
            print("Por favor, digite um número válido.")

# Usando a função para obter as 3 notas
n1 = obter_nota("primeira")
n2 = obter_nota("segunda")
n3 = obter_nota("terceira")
# Calculando a média das notas
media = (n1+n2+n3)/3

print(f"A média do aluno {nome} é: {media:.2f}")  #:.2f é usado para mostrar apenas duas casas dec  
if media <= 5.9:
    status = "Reprovado"
elif media >= 6.0 and media <= 6.9:
    status = "de Recuperação"
elif media >= 7.0:
    status = "Aprovado"

print(f"O aluno {nome} está {status}.")  #f é usado para concatenar strings e vari