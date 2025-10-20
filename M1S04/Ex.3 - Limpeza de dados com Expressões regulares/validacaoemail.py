import re

def validar_email(email):
    padrao = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(padrao, email) is not None

def salvar_em_arquivo(nome_arquivo, lista_emails):
    with open(nome_arquivo, 'w') as arquivo:
        for email in lista_emails:
            arquivo.write(email + '\n')

def separar_emails(lista_emails):
    validos = []
    invalidos = []
    for email in lista_emails:
        if validar_email(email):
            validos.append(email)
        else:
            invalidos.append(email)
    return validos, invalidos 

emails = [
    "joao.silva@gmail.com",
    "maria_oliveira123@yahoo.com.br",
    "contato@empresa.com",
    "vendas@lojaonline.com.br",
    "suporte.tech@dominio.net",
    "lucas-pereira@outlook.com",
    "aline.teste@faculdade.edu.br",
    "dev.python@projetos.io",
    "user+marketing@gmail.com",
    "teste.email@exemplo.co",
    "joao.silva@gmail",             
    "maria_oliveira123@.com",       
    "contato@empresa",              
    "vendas@lojaonline..com",       
    "@outlook.com",                 
    "lucas-pereira@",               
    "aline.teste@faculdade,edu.br", 
    "dev.python@projetos .io",      
    "user+marketinggmail.com",      
    "teste.email@exemplo.c"
]

validos, invalidos = separar_emails(emails)

salvar_em_arquivo('emails_validos.txt', validos)
salvar_em_arquivo('emails_invalidos.txt', invalidos)

print('Arquivos gerados!!')
