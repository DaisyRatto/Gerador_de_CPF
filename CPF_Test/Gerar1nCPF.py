import re

import sys
'''cpf = input("Digite seu CPF sem nenhuma pontuação: ") \
    .replace(" ", "") \
    .replace("-", "") \
    .replace(".", "")'''

entrada = input("Digite seu CPF: ")
cpf = re.sub(
    r"[^0-9]",
    "",
    entrada
)
nove_digitos = cpf[:9]
dez_digitos = cpf[:10]
multiplicacao = 10
multiplicacao_1 = 11
resultado_1 = 0
resultado_2 = 0

entrada_sequencial = entrada == entrada[0] * len(entrada)

if entrada_sequencial:
    print("Você digitou seu CPF sequencial.")
    sys.exit()


for digito in nove_digitos:
    resultado_1 += int(digito) * multiplicacao
    multiplicacao -= 1
    digito_1 = (resultado_1 * 10) % 11

for digito in dez_digitos:
    resultado_2 += int(digito) * multiplicacao_1
    multiplicacao_1 -= 1
    digito_2 = (resultado_2 * 10) % 11

if digito_1 <= 9:
    ...
else:
    digito_1 = 0


if digito_2 <= 9:
    ...
else:
    digito_2 = 0


cpf_criado_pelo_calculo = f"{nove_digitos}{digito_1}{digito_2}"

if cpf == cpf_criado_pelo_calculo:
    print(f"CPF: {cpf_criado_pelo_calculo} está correto!")
else:
    print("CPF inválido!")