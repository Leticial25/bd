import PySimpleGUI as sg
import sqlite3 as bbb

# Criar a conexão e interage com o banco

conn = bbb.connect('SQLite.db')  # conecta ao banco
c = conn.cursor()

# Criar layout
sg.theme('Reddit')
sg.theme_background_color('#FFE4C4')
layout = [
    [sg.Button('Cadastrar', size=(30, 1), button_color=('#F08080'), border_width=(5))],
    [sg.Button('Consulta', size=(30, 1), button_color=('#F08080'), border_width=(5))],
    [sg.Button('Relatórios', size=(30, 1), button_color=('#F08080'), border_width=(5))],
]

font_programa = ('Arial', 25)

# tela principal, chamando os componentes desta janela
# janela (nome da janela, componentes, tamanho da janela)

janela = sg.Window('Sistema de vendas 1.0', layout, size=(600, 400), font=font_programa, resizable=True)

# while para manter a janela constante enquanto não for fechada

while True:
    event, values = janela.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == 'Cadastrar':

        # Criar layout
        cadastroLayout = [
            [sg.Text('Produto')],
            [sg.InputText(key='produto')],
            [sg.Text('Valor')],
            [sg.InputText(key='valor')],
            [sg.Button('Cadastrar', size=(30, 1), button_color=('#00FF7F'), border_width=(10))],
            [sg.Button('Cancelar', size=(30, 1), button_color=('#E0FFFF'), border_width=(10))]
        ]

        cadastroJanela = sg.Window('Sistema de vendas 1.0', cadastroLayout, size=(400, 200), font=font_programa,
                                   resizable=True)

        while True:
            event, values = cadastroJanela.read()

            if event == sg.WINDOW_CLOSED or event == 'Cancelar':
                cadastroJanela.close()
                break

            # interagindo com o banco

            c.execute('INSERT INTO vendas (produto, valor) VALUES(?, ?)', (values['produto'], values['valor']))
            conn.commit()

            # limpar inputs após o cadastro
            cadastroJanela["produto"].update("")
            cadastroJanela["valor"].update("")

            # confirmar cadastro
            sg.popup('Cadastro realizado com sucesso!', title='Cadastro')



    elif event == "Consulta":

        # criar layout
        consulta_layout = [
            [sg.Text("Produto")],
            [sg.InputText(key="Produto")],
            [sg.Button("Consultar")],
            [sg.Button("Consultar")],
            [sg.Button("Cancelar")],
            [sg.Table(values=[], headings=["produto", "valor"], display_row_numbers=False, auto_size_columns=False,
                      num_rows=10, key="tabela")]
        ]

        consulta_window = sg.Window("Consulta de produtos", consulta_layout, resizable=True)

        # loop de eventos
        while True:
            event, values = consulta_window.read()

            if event == sg.WIN_CLOSED or event == "Cancelar":
                consulta_window.close()
                break

            # operações no banco de dados
            produto_busca = values["produto"].upper()
            c.execute("SELECT produto, valor FROM vendas WHERE UPPER(produto) = ?", (produto_busca,))
            registros = c.fetchall()

            # atualizar
            tabela = consulta_window["tabela"]
            tabela.update(values=registros)

        consulta_window.close()