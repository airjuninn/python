#q1
'''dados = {}
dados["nome"] = input("Digite seu nome: ")
dados["idade"] = int(input("Digite sua idade: "))
dados["cidade"] = input("Digite a sua cidade: ")

for chave, valor in dados.items():
     print(f"{chave}: {valor}")'''
######################################################################
#q2
'''
frase = input("Digite uma frase: ")

palavras = frase.split()

cont_palav = {}

for palavra in palavras:
    if palavra in cont_palav:
        cont_palav[palavra] += 1
    else:
        cont_palav[palavra] = 1

# Exibe o resultado
print("Contagem de palavras:")
for palavra, cont in cont_palav.items():
    print(f"'{palavra}': {cont}")
'''
######################################################################
#q3
'''
dados = {}

for a in range(3):
    nome = input(f"Digite o nome do aluno {a + 1}: ")

    notas = []
    for b in range(3):
        nota = float(input(f"Digite a nota {b + 1} de {nome}: "))
        notas.append(nota)

        dados[nome] = notas

print("\nMédia das notas de cada aluno: ")
for nome, notas in dados.items():
    med = sum(notas) / len(notas)
    print(f"{nome}: {med:.2f}")
'''
######################################################################
'''print(dados["nome"])
print(dados.get("idade"))'''

#modificando valores e adicionando chaves e valores
''' dados["idade"] = 26
dados["profissão"] = "Engenheira"
print(dados)'''

#removendo itens
#remove a chave e o valor
# del dados["cidade"]
#remove e retorna o valor de "idade"
# idade = dados.pop("idade")

#percorrendo um dicionário
''' for chave, valor in dados.items():
     print(f"{chave}: {valor}")'''

#adicionar e atualizar elementos
# dados.update({"cidade": "Rio de Janeiro", "idade": 27})
# print(dados)

#remove "idade"
'''idade = dados.pop("idade")
print(dados)

#remove o último elemento inserido
ultimo_item = dados.popitem()
print(ultimo_item) '''

######################################################################

