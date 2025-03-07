ld1 = input("Digite o primeiro lado do triângulo: ")
ld2 = input("Digite o segundo  lado do triângulo: ")
ld3 = input("Digite o terceiro  lado do triângulo: ")

if ld1+ld2 > ld3 and ld1+ld3 > ld2 and ld2+ld3 > ld1:
    if ld1 == ld2 == ld3:
        print("As medidas formam um triângulo equilátero.")
    elif ld1 == ld2 or ld2 == ld3 or ld3 == ld1:
        print("As medidas formam um triângulo isósceles.")
    else:
        print("As medidas formam um triângulo escaleno.")
