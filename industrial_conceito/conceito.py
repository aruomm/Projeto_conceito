# Textos do orçamento
texto_orcamento = input("Informe o serviço a ser realizado: ")

empresa = input("Informe a empresa onde o serviço será realizado: ")
solicitante = input("Informe o nome do solicitante do orçamento: ")

data = input("Informe a data para realização do serviço (no fomato dd/mm/aa): ")


print(f"\nOrçamento referente a {texto_orcamento} a ser realizado na data {data} na empresa {empresa} ")

print(f"Aos cuidados de {solicitante}.\n")

# Valor da hora inserida pelo usuário
hora_normal = float(input("Informe o valor da hora normal: "))
hora_50 = hora_normal * 1.5
hora_100 = hora_normal * 2

print(f"\nValor hora normal: R${hora_normal:.2f}")
print(f"Valor hora 50%: R${hora_50:.2f}")
print(f"Valor hora 100%: R${hora_100:.2f}\n")

# Listas vazias para armazenar as informações
funcionarios = []
qtd_hora_normal = []
qtd_hora_50 = []
qtd_hora_100 = []

# Quantidade de funcionários inserida pelo usuário
num_funcionarios = int(input("Informe a quantidade de funcionários: "))

# Inserção das informações de cada funcionário
for i in range(num_funcionarios):
    nome_funcionario = input(f"Informe o nome do funcionário {i + 1}: ")
    horas_normais_func = float(input(f"Informe as horas normais para {nome_funcionario}: "))
    horas_50_func = float(input(f"Informe as horas com adicional de 50% para {nome_funcionario}: "))
    horas_100_func = float(input(f"Informe as horas com adicional de 100% para {nome_funcionario}: "))

    # Adicione as informações às listas
    funcionarios.append(nome_funcionario)
    qtd_hora_normal.append(horas_normais_func)
    qtd_hora_50.append(horas_50_func)
    qtd_hora_100.append(horas_100_func)


# Cálculo do orçamento

# Código anterior...

# Calcula o valor total para cada funcionário
valor_total_funcionario = []
for i in range(num_funcionarios):
    valor_total = (qtd_hora_normal[i] * hora_normal) + (qtd_hora_50[i] * hora_50) + (qtd_hora_100[i] * hora_100)
    valor_total_funcionario.append(valor_total)

# Exibe os valores individuais e o valor total do orçamento
print("\nResumo das informações:")
total_orcamento = 0
for i in range(num_funcionarios):
    print(f"Funcionário: {funcionarios[i]}")
    print(f"Horas Normais: {qtd_hora_normal[i]}")
    print(f"Horas 50%: {qtd_hora_50[i]}")
    print(f"Horas 100%: {qtd_hora_100[i]}")
    print(f"Valor Total: R${valor_total_funcionario[i]:.2f}\n")
    total_orcamento += valor_total_funcionario[i]

print(f"Valor Total do Orçamento: R${total_orcamento:.2f}")

lucro = float(input("Insira a porcentagem de lucro desejada: "))
total_orcamento_lucro = total_orcamento + total_orcamento * (lucro/100)

print(f"Valor total do orçamento com lucro: R${total_orcamento_lucro}")

