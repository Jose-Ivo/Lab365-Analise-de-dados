import csv

with open("vendas.csv", "r", encoding="utf-8") as arq:
    leitor = csv.DictReader(arq)
    dados = []

    for l in leitor:
        quantidade = int(l['quantidade'])
        valor = float(l['valor'])
        total = quantidade * valor
        l['total'] = total
        dados.append(l)

nome_colunas = list(dados[0].keys())


with open("vendas_completo.csv", "w", newline="", encoding="utf-8") as arq:
    escritor = csv.DictWriter(arq, fieldnames=nome_colunas)
    escritor.writeheader()
    escritor.writerows(dados)

	