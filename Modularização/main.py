from funcoes_calculo import somar, subtrair, multiplicar, dividir
from funcoes_data import data_atual, formatar_data, dias_ate
from datetime import date

print("=== Operações Matemáticas ===")
print("5 + 3 =", somar(5, 3))
print("9 - 2 =", subtrair(9, 2))
print("4 * 7 =", multiplicar(4, 7))
print("10 / 2 =", dividir(10, 2))

print("\n=== Operações com Datas ===")
hoje = data_atual()
print("Data atual:", formatar_data(hoje))

data_futura = date(2025, 12, 31)
print("Dias até o fim de 2025:", dias_ate(data_futura))
