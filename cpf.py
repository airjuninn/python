import os

def calcular_dv(cpf):
    # Cálculo do primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto = soma % 11
    dv1 = 0 if resto < 2 else 11 - resto

    # Cálculo do segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(9)) + dv1 * 2
    resto = soma % 11
    dv2 = 0 if resto < 2 else 11 - resto

    return dv1, dv2

def validar_cpf(cpf):
    # Remove caracteres não numéricos
    cpf = ''.join(filter(str.isdigit, cpf))
    
    # Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11 or cpf == cpf[0] * len(cpf):
        return False
    dv1, dv2 = calcular_dv(cpf)

    # Verifica se os dígitos verificadores estão corretos
    return cpf[-2] == str(dv1) and cpf[-1] == str(dv2)

def main():
    nome = input("Digite o seu nome: ")
    cpf = input("Digite o seu CPF (apenas números): ")
    cpf_form = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    def limpar_terminal():
        if os.name == 'nt':  # Windows
            os.system('cls')
        else:  # Unix/Linux/Mac
            os.system('clear')
    
    
    
    if validar_cpf(cpf):
        limpar_terminal()
        print(f"O CPF {cpf_form} de {nome} é válido.")
    else:
        limpar_terminal()
        print(f"O CPF {cpf_form} de {nome} é inválido.")
if __name__ == "__main__":
    main()