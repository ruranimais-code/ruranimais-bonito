usuarios = {}
import sqlite3
conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()
from rich import print as rprint
import os

def cadastrar_usuario():
    cursor.execute("""CREATE TABLE IF NOT EXISTS contas_ruranimais (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    email TEXT NOT NULL,
                    senha TEXT NOT NULL UNIQUE
                    )""")

    rprint("\n[#d74013]=============================[/#d74013]")
    rprint(":green_heart: :heart: [#719029][bold]CADASTRO DE USUÁRIO[/bold][/#719029] :heart: :green_heart:")
    rprint("[#d74013]=============================[/#d74013]\n")
#adicionar campo do cpf ---
    while True:
        nome = input("Nome: ")
        if len(nome) > 12:
            rprint("[#d74013]❌ Nome inválido. Digite um nome com no máximo 12 caracteres.[/#d74013]")
        elif len(nome) < 3:
            rprint("[#d74013]❌ Nome inválido. Digite um nome com pelo menos 3 caracteres.[/#d74013]")
        else:
            break
    while True:
        email = input("E-mail: ")
        if "@" not in email or "." not in email:
            rprint("[#d74013]❌ E-mail inválido. Email não contém @ ou endereço válido.[/#d74013]")
        elif email.endswith ("@ufrpe.br") == False:
            rprint("[#d74013]❌ E-mail inválido. Digite um e-mail institucional da UFRPE.[/#d74013]")
        else:
            break
    senha = input("Senha: ")

    cursor.execute("""INSERT INTO contas_ruranimais
                   (nome, email, senha)VALUES
                   (?,?,?)""", (nome, email, senha))
    cursor.execute("""SELECT * FROM contas_ruranimais""")
    
    contas = cursor.fetchall()
    print(contas)
    for conta in contas:
           id, nome, email, senha = conta
           print(f"id:{id}")
           print(f"nome:{nome}")
           print(f"email:{email}")
           print(f"senha:{senha}")
    conexao.commit()
    print("\n✅ Usuário cadastrado com sucesso!")


def login():
    os.system("clear")
    rprint("\n[#d74013]================[/#d74013]")
    rprint(":green_heart: :heart: [#719029][bold]LOGIN[/bold][/#719029] :heart: :green_heart:")
    rprint("[#d74013]================[/#d74013]")

    email = input("E-mail: ")
    senha = input("Senha: ")

    cursor.execute(
        "SELECT nome, email, senha FROM contas_ruranimais WHERE email = ? AND senha = ?",
        (email, senha)
    )
    usuario = cursor.fetchone()

    if usuario:
        nome, _, _ = usuario
        print(f"\n✅ Bem-vindo(a), {nome}!")
        return {"nome": nome, "email": email, "senha": senha}

    print("\n❌ E-mail ou senha incorretos.")
    return None