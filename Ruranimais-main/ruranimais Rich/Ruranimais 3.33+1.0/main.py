from rich import print as rprint
from rich.console import Console
console = Console()
from cadastro import *
#https://rich.readthedocs.io/en/stable/appendix/colors.html
import sqlite3
conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

def menu_inicial():

    while True:

        rprint("\n[#d74013]=====================[/#d74013]")
        rprint(":green_heart: :heart: [#719029]RURANIMAIS[/#719029] :heart: :green_heart:")
        rprint("[#d74013]=====================[/#d74013]")

        rprint("1 - Cadastrar usuário\n2 - Login\n3 - Sair\n\n[green1]Escolha uma opção: [/green1]\n")

        opcao = input("")

        if opcao == "1":

            cadastrar_usuario()

        elif opcao == "2":

            login()

        elif opcao == "3":

            print("\n👋 Até logo!")
            exit()

        else:

            print("\n❌ Opção inválida!")
menu_inicial()