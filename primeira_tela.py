import PySimpleGUI as sg
import sqlite3 as bbb
import PySimpleGUI as sg
import sqlite3 as bbb

# cria a conexão e interage com o banco
conn = bbb.connect("vendas.db")  # Conecta ao banco
c = conn.cursor()

# Criar o layout
layout = [

    # [MENU PRINCIPAL, [Submenu, Submenu, Submenu] ]
    [sg.Menu([
        ['Cadastro', ['Cadastro Clientes', 'Cadastro Fornecedores', 'Cadastro Transportadoras']],
        ['Consulta', ['Consulta Clientes', 'Consulta Fornecedores', 'Consulta Transportadoras']],
        ['Relatório', ['Relatório Clientes', 'Relatório Fornecedores', 'Relatório Transportadoras']]
    ],
        tearoff=False)]

]

# Criar a janela principal e chamar os componentes desta na janela
# WINDOW (nome da janela, componentes, tamanho da janela)
# MUDAR A FONTE E HABILITAR O BOTÃO MAXIMIZAR: font=font_programa,resizable=True
window = sg.Window("Sistema de vendas 1.0", layout, size=(600, 400))

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break

    # Acessa o submenu CADASTRO -> Cadastro clientes
    if event == 'Cadastro Clientes':

        cadastro_layout_clientes = [
            [sg.Text("Nome:")],
            [sg.InputText(key="nome")],
            [sg.Text("E-mail:")],
            [sg.InputText(key="email")],
            [sg.Text("Telefone:")],
            [sg.InputText(key="telefone")],
            [sg.Button('Cadastrar', size=(30, 1), button_color=('#FF69B4'), border_width=(5))],
            [sg.Button('Cancelar', size=(30, 1), button_color=('#FF69B4'), border_width=(5))]
        ]

        cadastro_clientes = sg.Window("Cadastro de clientes", cadastro_layout_clientes, size=(400, 200))

        while True:
            event, values = cadastro_clientes.read()

            if event == sg.WIN_CLOSED or event == "Cancelar":
                cadastro_layout_clientes.close()
                break

            # Operações no Banco de dados
            c.execute("INSERT INTO clientes (nome, email, telefone) VALUES (?, ?, ?)",
                      (values["nome"], values["email"], values["telefone"]))
            conn.commit

        # Limpa os campos após efetuar o cadastro
        cadastro_layout_clientes["nome"].update("")
        cadastro_layout_clientes["email"].update("")
        cadastro_layout_clientes["telefone"].update("")

        # Mostrar pop-up após o cadastro
        sg.popup("Cadastro do cliente realizado com sucesso!")

    cadastro_layout_clientes.close()

# Fecha a tela principal. Penúltima ação do código. Lembrem-se de colocar no final do código
window.close()

# Fecha a conexão com o BD. Última ação do código. Lembrem-se de colocar no final do código
conn.close()




"""sg.theme_background_color('#FFE4C4')
layout = [
    [sg.Button('Cadastrar', size=(30,1), button_color=('#FF69B4'), border_width=(5))],
    [sg.Button('Consulta', size=(30, 1), button_color=('#DB7093'), border_width=(5))],
    [sg.Button('Relatórios', size=(30, 1), button_color=('#F08080'), border_width=(5))],
    [sg.Button('Fornecedores', size=(30, 1), button_color=('#DB7093'), border_width=(5))],
    [sg.Button('Transportadora', size=(30, 1), button_color=('#FF69B4'), border_width=(5))]

]

font_programa = ('Arial', 25)

# tela principal, chamandoi os componentes desta janela
# janela (nome da janela, componentes, tamanho da janela)

janela = sg.Window('Sistema de vendas 1.0', layout, size=(600, 400), font= font_programa, resizable=True)

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
            [sg.Button('Cadastrar', size=(30,1), button_color=('#FF69B4'), border_width=(5))],
            [sg.Button('Cancelar', size=(30,1), button_color=('#FF69B4'), border_width=(5))]
        ]

        cadastroJanela = sg.Window('Sistema de vendas 1.0', cadastroLayout, size=(400, 425), font= font_programa, resizable=True)

        while True:
            event, values = cadastroJanela.read()

            if event == sg.WINDOW_CLOSED or event == 'Cancelar':
                cadastroJanela.close()
                break

            # interagindo com o banco
            c.execute('INSERT INTO vendas (produto, valor) VALUES(?, ?)', (values['produto'], values['valor']))
            conn.commit()

            #Limpa depois do cadastro
            cadastroJanela["produto"].update("")
            cadastroJanela["valor"].update("")

            # confirmar cadastro
            sg.popup('Cadastro realizado com sucesso!', title='Cadastro')

            cadastroJanela.close()

    elif event == "Consulta":

            # criar layout
            consulta_layout = [
                [sg.Text("Produto")],
                [sg.InputText(key="produto")],
                [sg.Button("Consultar")],
                [sg.Button("Cancelar")],
                [sg.Table(values=[], headings=["ID", "produto", "valor"], display_row_numbers=False, auto_size_columns=False, num_rows=10, key="tabela")]
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
                c.execute("SELECT ID, produto, valor FROM vendas WHERE UPPER(produto) = ?", (produto_busca,))
                registros = c.fetchall()

                # atualizar
                tabela = consulta_window["tabela"]
                tabela.update(values=registros)

            consulta_window.close()

    conn = bbb.connect('Fornecedores.db')  # conecta ao banco
    c = conn.cursor()

    elif event == "cadastro fornecedor":

        #Criar layout
        Consulta_layout_fornecedor = [
            [sg.Text("Nome")],
            [sg.InputText(key="nome")]
            [sg.Text("CPF")],
            [sg.InputText(key="cpf")]
            [sg.Text("Telefone")],
            [sg.InputText(key="telefone")]
            [sg.Text("Email")],
            [sg.InputText(key="email")]
            [sg.Text("Endereço")],
            [sg.InputText(key="endereço")]
            [sg.Text("cidade")],
            [sg.InputText(key="cidade")]
            [sg.Text("Estado")],
            [sg.InputText(key="estado")]
            [sg.Text("País")],
            [sg.InputText(key="país")]
            [sg.Button('Cadastrar', size=(30, 1), button_color=('#FF69B4'), border_width=(5))],
            [sg.Button('Cancelar', size=(30, 1), button_color=('#FF69B4'), border_width=(5))]
           ]
        while True:
            event, values = cadastroLayout


            if event == sg.WINDOW_CLOSED or event == 'Cancelar':
                cadastroJanela.close()
                break

            # interagindo com o banco
            c.execute('INSERT INTO vendas (Nome, CPF, Telefone, Email, Endereço, Cidade, Estado, País) VALUES(?, ?, ?, ?, ?, ?, ?, ?)', (values['Nome'], values['CPF'], values['Telefone'], values['Email'], values['Endereço'], values['Cidade'], values['Estado'], values['País']))
            conn.commit()

            #Limpa depois do cadastro
            cadastroJanela["Nome"].update("")
            cadastroJanela["CPF"].update("")
            cadastroJanela["Telefone"].update("")
            cadastroJanela["Email"].update("")
            cadastroJanela["Endereço"].update("")
            cadastroJanela["Cidade"].update("")
            cadastroJanela["Estado"].update("")
            cadastroJanela["País"].update("")

            # confirmar cadastro
            sg.popup('Cadastro realizado com sucesso!', title='Cadastro')

            cadastroJanela.close()
"""


#conn.close()