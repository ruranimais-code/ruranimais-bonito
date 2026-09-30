from rich import print as rprint
from rich.console import Console
console = Console()
from cadastro import *
#https://rich.readthedocs.io/en/stable/appendix/colors.html
import sqlite3
conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()
import os

def menu_inicial():

    while True:

        rprint("\n[#d74013]=====================[/#d74013]")
        rprint(":green_heart: :heart: [#719029][bold]RURANIMAIS[/bold][/#719029] :heart: :green_heart:")
        rprint("[#d74013]=====================\n[/#d74013]")

        rprint("1 - Cadastrar usuário\n2 - Login\n3 - Sair\n\n[#eea103][bold]Escolha uma opção: [/bold][/#eea103]\n")

        opcao = input("")

        if opcao == "1":
            os.system("clear")

            cadastrar_usuario()

        elif opcao == "2":

            login()

        elif opcao == "3":
            os.system("clear")
            rprint("\n\n\n[#eea103]👋 [bold]Até logo![/bold][/#eea103]\n\n\n")
            exit()

        else:
            os.system("clear")
            rprint("[#d74013]=====================[/#d74013]\n\n[bold][#d74013]❌ Opção inválida![/#d74013][/bold]")
            

menu_inicial()