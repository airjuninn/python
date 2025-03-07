login = input("Usuário: ")
senha = input("Senha: ")

if login == "" and senha == "":
    print("Campos vazios")
elif len(senha) < 6:
    print("Senha muito curta, tem apenas ", len(senha), " caracteres")
elif login == "zezin" and senha == "ighostthedowncool":
    print("Login efetuado com sucesso!")
else:
    print("Login ou senha inválidos!")