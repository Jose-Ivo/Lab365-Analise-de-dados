from datetime import datetime

entrada = input("Insira a data (DD/MM/AAAA): ")
try:
    data_user = datetime.strptime(entrada, "%d/%m/%Y")
except ValueError:
    print("Formato inválido. Use (DD/MM/AAAA)")
    exit()  

data_final_ano = datetime(data_user.year, 12, 31)
dia_semana = data_user.strftime('%A')

dias_semana_pt = {
    "Monday": "segunda-feira",
    "Tuesday": "terça-feira",
    "Wednesday": "quarta-feira",
    "Thursday": "quinta-feira",
    "Friday": "sexta-feira",
    "Saturday": "sábado",
    "Sunday": "domingo"
}

dia_semana_pt = dias_semana_pt[dia_semana]
dias_restantes = (data_final_ano - data_user).days

print(f"Hoje é {dia_semana_pt} e faltam {dias_restantes} dias para o final do ano")
