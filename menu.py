import PySimpleGUI as sg
import sqlite3 as bbb

# faz conexão com o banco
conn = bbb.connect("clientes.db")
c = conn.cursor()

# criar layout do sistema de cadastro
layout = [
    [sg.Menu([
        ['Cadastro', ['Cadastro Clientes',
                      'Cadastro Fornecedores', 'Cadastro Transportadora']],
        ['Consulta', ['Consulta Clientes',
                      'Consulta Fornecedores', 'Consulta Transportadora']],
        ['Relatórios', ['Relatórios Clientes',
                        'Relatórios Fornecedores', 'Relatórios Transportadora']]

    ],
        tearoff=False)]
]

# cria janela principal para chamar os componentes desta janela
window_cliente = sg.Window("Sistema de cadastro de clientes 1.0",
                           layout, size=(600, 400))

# while do cadastro de clientes
while True:
    event, values = window_cliente.read()

    if event == sg.WINDOW_CLOSED:
        break




    elif event == "Cadastro Clientes":
        cadastro_layout_clientes = [
            [sg.Text("Nome")],
            [sg.InputText(key="Nome")],
            [sg.Text("CPF")],
            [sg.InputText(key="CPF")],
            [sg.Text("Endereço")],
            [sg.InputText(key="Endereço")],
            [sg.Text("Telefone")],
            [sg.InputText(key="Telefone")],
            [sg.Text("Cidade")],
            [sg.InputText(key="Cidade")],
            [sg.Text("Estado")],
            [sg.InputText(key="Estado")],
            [sg.Button("Cadastro"), sg.Button("Cancelar")]
        ]

        cadastro_clientes = sg.Window("Cadastro de Clientes", cadastro_layout_clientes, size=(400, 400))

        while True:
            event, values = cadastro_clientes.read()

            if event == sg.WINDOW_CLOSED or event == "Cancelar":
                cadastro_clientes.close()
                break

        c.execute("INSERT INTO clientes (Nome, CPF, Endereço, Telefone, Cidade, Estado) VALUES (?, ?, ?, ?, ?, ?)",
                  (values["Nome"], values["CPF"], values["Endereço"], values["Telefone"], values["Cidade"],
                   values["Estado"]))
        conn.commit()

        cadastro_clientes["Nome"].update("")
        cadastro_clientes["CPF"].update("")
        cadastro_clientes["Endereço"].update("")
        cadastro_clientes["Telefone"].update("")
        cadastro_clientes["Cidade"].update("")
        cadastro_clientes["Estado"].update("")

        sg.popup("Cadastro efetuado!")

        cadastro_clientes.close()
    # window_cliente.close()

    # while do cadastro de clientes

    elif event == "Cadastro Fornecedores":

        cadastro_layout_fornecedores = [
            [sg.Text("Nome")],
            [sg.InputText(key="nome")],
            [sg.Text("CPF")],
            [sg.InputText(key="cpf")],
            [sg.Text("Endereço")],
            [sg.InputText(key="endereço")],
            [sg.Text("Telefone")],
            [sg.InputText(key="telefone")],
            [sg.Text("Cidade")],
            [sg.InputText(key="cidade")],
            [sg.Text("Estado")],
            [sg.InputText(key="estado")],
            [sg.Button("Cadastro"), sg.Button("Cancelar")]
        ]

        cadastro_fornecedores = sg.Window("Cadastro de Fornecedores", cadastro_layout_fornecedores, size=(400, 400))

        while True:
            event, values = cadastro_fornecedores.read()

            if event == sg.WINDOW_CLOSED or event == "Cancelar":
                cadastro_fornecedores.close()
                break

        c.execute("INSERT INTO clientes (Nome, CPF, Endereço, Telefone, Cidade, Estado) VALUES (?, ?, ?, ?, ?, ?)", (values["Nome"], values["CPF"], values["Endereço"], values["Telefone"], values["Cidade"], values["Estado"]))
        conn.commit()

        """ cadastro_clientes["Nome"].update("")
        cadastro_clientes["CPF"].update("")
        cadastro_clientes["Endereço"].update("")
        cadastro_clientes["Telefone"].update("")
        cadastro_clientes["Cidade"].update("")
        cadastro_clientes["Estado"].update("") """

        sg.popup("Cadastro efetuado!")

    cadastro_fornecedores.close()

"""     
while True:
    event, values = window_fornecedor.read()

    if event == sg.WINDOW_CLOSED:
        break

    elif event == "Cadastro Fornecedores":
                fornecedor_layout = [
                [sg.Text("ID")],
                [sg.InputText(key="id_fornecedor")],
                [sg.Text("Nome")],
                [sg.InputText(key="Nome_fornecedor")],
                [sg.Text("Endereço")],
                [sg.InputText(key="Endereço")],
                [sg.Text("CEP")],
                [sg.InputText(key="CEP")],
                [sg.Text("Cidade")],
                [sg.InputText(key="Cidade")],
                [sg.Text("Estado")],
                [sg.InputText(key="Estado")],
                [sg.Text("País")],
                [sg.InputText(key="País")],
                [sg.Button("Cadastrof"), sg.Button("Cancelar")]

                ]
    cadastro_fornecedor = sg.Window(
        "Cadastro de Fornecedores", fornecedor_layout, size=(400, 400))
    while True:
        event, values = cadastro_fornecedor.read()

        if event == sg.WINDOW_CLOSED or event == "Cancelar":
                    fornecedor_layout.close()
                    break

        c.execute("INSERT INTO fornecedores (Id_fornecedor, Nome_fornecedor, Endereço, CEP, Cidade, Estado, País) VALUES (?, ?, ?, ?, ?, ?, ?)",
                        (values["Id_fornecedor"], values["Nome_fornecedor"], values["Endereço"], values["CEP"], values["Cidade"], values["Estado"], values["País"] ))
        conn.commit()

        cadastro_fornecedor["Id_fornecedor"].update("")
        cadastro_fornecedor["Nome_fornecedor"].update("")
        cadastro_fornecedor["Endereço"].update("")
        cadastro_fornecedor["CEP"].update("")
        cadastro_fornecedor["Cidade"].update("")
        cadastro_fornecedor["Estado"].update("")
        cadastro_fornecedor["País"].update("") 
        sg.popup("Cadastro efetuado!")


window_fornecedor.close()
 """

conn.close()