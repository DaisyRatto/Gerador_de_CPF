import random

nove_digitos = ""

for i in range(9):
    nove_digitos += str(random.randint(0, 9))

multiplicacao = 10
multiplicacao_1 = 11
resultado_1 = 0
resultado_2 = 0


for digito in nove_digitos:
    resultado_1 += int(digito) * multiplicacao
    multiplicacao -= 1
    digito_1 = (resultado_1 * 10) % 11

dez_digitos = nove_digitos + str(digito_1)

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

print(cpf_criado_pelo_calculo)