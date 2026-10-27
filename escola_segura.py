
import os
import getpass
from datetime import datetime

# Dados ficticios dos alunos
alunos = [
    {"nome": "Ana Silva", "turma": "2API", "ocorrencias": 1},
    {"nome": "Pedro Costa", "turma": "2API", "ocorrencias": 3},
    {"nome": "Maria Santos", "turma": "2API", "ocorrencias": 0}
]

# DESAFIO A - Proteger a palavra-passe
password_admin = os.getenv("ESCOLASEGURA_PASSWORD")

if not password_admin:
    print("Configuracao de acesso indisponivel.")
    raise SystemExit

# DESAFIO D - Registar os acessos
def registar_acesso(resultado):
    data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("acessos.log", "a", encoding="utf-8") as ficheiro:
        ficheiro.write(f"{data_hora} - {resultado}\n")


print("=== SISTEMA ESCOLASEGURA ===")

# DESAFIO B - Limitar tentativas
tentativas = 0
acesso_autorizado = False

while tentativas < 3:

    password = getpass.getpass("Introduza a palavra-passe: ")

    if password == password_admin:
        print("Acesso autorizado!")
        registar_acesso("sucesso")
        acesso_autorizado = True
        break

    else:
        print("Acesso negado.")
        registar_acesso("falha")
        tentativas += 1

        restantes = 3 - tentativas

        if restantes > 0:
            print(f"Tentativas restantes: {restantes}")

if not acesso_autorizado:
    print("Acesso bloqueado. Limite de tentativas atingido.")
    raise SystemExit

# DESAFIO C - Validar o menu
while True:

    print("\n1 - Consultar alunos")
    print("2 - Consultar ocorrencias")
    print("3 - Terminar")

    opcao = input("Escolha uma opcao: ").strip()

    if opcao == "1":

        for aluno in alunos:
            print(aluno["nome"], aluno["turma"])

    elif opcao == "2":

        for aluno in alunos:
            print(aluno["nome"], aluno["ocorrencias"])

    elif opcao == "3":

        print("Programa terminado.")
        break

    else:

        print("Opcao invalida. Escolha 1, 2 ou 3.")
