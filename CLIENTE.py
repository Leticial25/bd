import PySimpleGUI as sg
import sqlite3 as bbb

# cria a conexão e interage com o banco DE DADOS
conn = bbb.connect("Cliente.db")  #Conecta ao banco
c = conn.cursor()

# Cria o layout
layout = [
    [sg.Button('Cadastrar', size=(30,2), button_color=('#FF69B4'), border_width=(5))]
    [sg.Button('Consulta', size=(30,2), button_color=('#DB7093'), border_width=(5))]
    [sg.Button('Relatórios', size=(30,2), button_color=('#F08080'), border_width=(5))]


]
font_programa = ('Arial', 25)

# Criar a janela principal e chama os componentes desta na janela
# WINDOW (nome da janela, componentes, tamanho da janela)
# MUDAR A FONTE E HABILITAR O BOTÃO MAXIMIZAR: font=font_programa,resizable=True
window = sg.Window("Sistema de cadastro do cliente 1.0", layout, size=(400, 400), resizable=True)

# Se o programa for executado, abra a janela
# While janela principal
while True:
    event, values = window.read()

    # SE a janela for fechada
    if event == sg.WINDOW_CLOSED:
        break

    if event == "Cadastrar":

        # criar layout
        cadastro_layout = [
            [sg.Text("NOME")],
            [sg.InputText(key="NOME")],
            [sg.Text("CPF")],
            [sg.InputText(key="CPF")],
            [sg.Text("ENDERECO")],
            [sg.InputText(key="ENDERECO")],
            [sg.Text("TELEFONE")],
            [sg.InputText(key="TELEFONE")],
            [sg.Text("CIDADE")],
            [sg.InputText(key="CIDADE")],
            [sg.Text("ESTADO")],
            [sg.InputText(key="ESTADO")],
            [sg.Button("Cadastrar")],
            [sg.Button("Cancelar")]
        ]

        cadastro_window = sg.Window("Cadastro de clientes", cadastro_layout, size=(400, 400))

        # While do cadastro
        while True:
            event, values = cadastro_window.read()

            if event == sg.WINDOW_CLOSED or event == "Cancelar":
                cadastro_window.close()
                break

            # interagindo com o banco
            c.execute("INSERT INTO cliente (NOME, CPF, ENDERECO, TELEFONE, CIDADE, ESTADO) VALUES (?, ?, ?, ?, ?, ?)",  (values["NOME"], values["CPF"], values["ENDERECO"], values["TELEFONE"], values["CIDADE"], values["ESTADO"]))
            conn.commit()

            # Limpar iputs após o cadastro
            cadastro_window["NOME"].update("")
            cadastro_window["CPF"].update("")
            cadastro_window["ENDERECO"].update("")
            cadastro_window["TELEFONE"].update("")
            cadastro_window["CIDADE"].update("")
            cadastro_window["ESTADO"].update("")

            # Confirmar o cadastro
            sg.popup("Cadastro realizado com sucesso!", title="Cadastro")

        cadastro_window.close()


conn.close()