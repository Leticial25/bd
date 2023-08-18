import PySimpleGUI as sg
import sqlite3 as bbb

conn = bbb.connect("banco.db")
c = conn.cursor()

layout = [
    [sg.Menu([
        ['Cadastro', ['Cadastro Clientes', 'Cadastro Fornecedores', 'Cadastro Transportadora', 'Cadastro Produto']],
        ['Consulta', ['Consulta Clientes', 'Consulta Fornecedores', 'Consulta Transportadora', 'Consulta Produto']],
        ['Relatórios',
         ['Relatórios Clientes', 'Relatórios Fornecedores', 'Relatórios Transportadora', 'Relatório Produto']]
    ], tearoff=False)]
]

layout_window = sg.Window("Menu do Sistema 1.0", layout, resizable=True, size=(600, 400))

while True:
    event, values = layout_window.read()
    if event == sg.WIN_CLOSED:
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
            [sg.Button("Cadastrar"), sg.Button("Cancelar")]
        ]
        cadastro_clientes = sg.Window("Cadastro de clientes", cadastro_layout_clientes, resizable=True, size=(600, 400))
        while True:
            event, values = cadastro_clientes.read()
            if event == cadastro_clientes.close() or event == "Cancelar":
                cadastro_clientes.close()
                break

            c.execute("INSERT INTO clientes (Nome, CPF, Endereço, Telefone, Cidade, Estado) VALUES (?, ?, ?, ?, ?, ?)",
                      (values["Nome"], values["CPF"], values["Endereço"], values["Telefone"], values["Cidade"],
                       values["Estado"]))
            conn.commit()
            sg.popup("Cadastro realizado com sucesso!", title="Cadastro")

    elif event == "Consulta Clientes":
        consulta_layout_clientes = [
            [sg.Text("CPF")],
            [sg.InputText(key="CPF")],
            [sg.Button("Consultar"), sg.Button("Cancelar")],
            [sg.Table(values=[], headings=["Nome", "CPF", "Endereço", "Telefone", "Cidade", "Estado"],
                      display_row_numbers=False, auto_size_columns=False, num_rows=1, key="tabela")]
        ]
        consulta_clientes = sg.Window("Consulta de clientes", consulta_layout_clientes, resizable=True,
                                      size=(1000, 800))
        while True:
            event, values = consulta_clientes.read()

            if event == sg.WIN_CLOSED or event == "Cancelar":
                consulta_clientes.close()
                break

                # operações no banco de dados
            produto_busca = values["CPF"].upper()
            c.execute("SELECT Nome, CPF, Endereço, Telefone, Cidade, Estado FROM clientes WHERE UPPER(CPF) = ?",
                      (produto_busca,))
            registros = c.fetchall()

            # atualizar
            tabela = consulta_clientes["tabela"]
            tabela.update(values=registros)



    elif event == "Cadastro Fornecedores":
        cadastro_layout_fornecedores = [
            [sg.Text("Id_fornecedor")],
            [sg.InputText(key="Id_fornecedor")],
            [sg.Text("Nome_fornecedor")],
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
            [sg.Button("Cadastrar"), sg.Button("Cancelar")]
        ]
        cadastro_fornecedores = sg.Window("Cadastro de Fornecedores", cadastro_layout_fornecedores, resizable=True,
                                          size=(800, 400))
        while True:
            event, values = cadastro_fornecedores.read()
            if event == cadastro_fornecedores.close() or event == "Cancelar":
                cadastro_fornecedores.close()
                break
            c.execute(
                "INSERT INTO fornecedores (Id_fornecedor, Nome_fornecedor, Endereço, CEP, Cidade, Estado, País) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (
                values["Id_fornecedor"], values["Nome_fornecedor"], values["Endereço"], values["CEP"], values["Cidade"],
                values["Estado"], values["País"]))
            conn.commit()
            sg.popup("Cadastro realizado!", title="Cadastro")



    elif event == "Consulta Fornecedores":
        consulta_layout_fornecedores = [
            [sg.Text("Id_fornecedor")],
            [sg.InputText(key="Id_fornecedor")],
            [sg.Button("Consultar"), sg.Button("Cancelar")],
            [sg.Table(values=[],
                      headings=["Id_fornecedor", "Nome_fornecedor", "Endereço", "CEP", "Cidade", "Estado", "País"],
                      display_row_numbers=False, auto_size_columns=False, num_rows=1, key="tabela")]
        ]
        consulta_fornecedor = sg.Window("Consultar Fornecedores", consulta_layout_fornecedores, resizable=True,
                                        size=(800, 400))
        while True:
            event, values = consulta_fornecedor.read()
            if event == sg.WIN_CLOSED or event == "Cancelar":
                consulta_fornecedor.close()
                break

            produto_busca = values["Id_fornecedor"].upper()
            c.execute(
                "SELECT Id_fornecedor, Nome_fornecedor, Endereço, CEP, Cidade, Estado, País FROM fornecedores WHERE UPPER(Id_fornecedor) = ?",
                (produto_busca,))
            registros = c.fetchall()

            # atualizar
            tabela = consulta_fornecedor["tabela"]
            tabela.update(values=registros)


    elif event == "Cadastro Transportadora":
        cadastro_layout_transportadora = [
            [sg.Text("Id_transportadora")],
            [sg.InputText(key="Id_transportadora")],
            [sg.Text("Nome_transportadora")],
            [sg.InputText(key="Nome_transportadora")],
            [sg.Text("Telefone")],
            [sg.InputText(key="Telefone")],
            [sg.Button("Cadastro"), sg.Button("Cancelar")]
        ]
        cadastro_transportadora = sg.Window("Sistema de cadastramento de transportadora",
                                            cadastro_layout_transportadora, resizable=True, size=(800, 400))

        while True:
            event, values = cadastro_transportadora.read()
            if event == cadastro_transportadora.close() or event == "Cancelar":
                cadastro_transportadora.close()
                break

            c.execute("INSERT INTO transportadora (Id_transportadora, Nome_transportadora, Telefone) VALUES (?, ?, ?)",
                      (values["Id_transportadora"], values["Nome_transportadora"], values["Telefone"]))
            conn.commit()

            sg.popup("Cadastro realizado com sucesso!", title="Cadastro")

    elif event == "Consulta Transportadora":
        consulta_layout_transportadora = [
            [sg.Text("Id_transportadora")],
            [sg.InputText(key="Id_transportadora")],
            [sg.Button("Consultar"), sg.Button("Cancelar")],
            [sg.Table(values=[], headings=["Id_transportadora", "Nome_transportadora", "Telefone"],
                      display_row_numbers=False, auto_size_columns=False, num_rows=1, key="tabela")]
        ]
        consulta_transportadora = sg.Window("Consultar Transportadora", consulta_layout_transportadora, resizable=True,
                                            size=(1000, 800))
        while True:
            event, values = consulta_transportadora.read()

            if event == sg.WIN_CLOSED or event == "Cancelar":
                consulta_transportadora.close()
                break

                # operações no banco de dados
            produto_busca = values["Id_transportadora"].upper()
            c.execute(
                "SELECT Id_transportadora, Nome_transportadora, Telefone FROM transportadora WHERE UPPER(Id_transportadora) = ?",
                (produto_busca,))
            registros = c.fetchall()

            # atualizar
            tabela = consulta_transportadora["tabela"]
            tabela.update(values=registros)

    elif event == "Cadastro Produto":
        cadastro_layout_produto = [
            [sg.Text("Produto")],
            [sg.InputText(key="Produto")],
            [sg.Text("Valor")],
            [sg.InputText(key="Valor")],
            [sg.Button("Cadastro"), sg.Button("Cancelar")]
        ]
        cadastro_produto = sg.Window("Sistema de cadastramento de transportadora", cadastro_layout_produto,
                                     resizable=True, size=(800, 400))

        while True:
            event, values = cadastro_produto.read()
            if event == cadastro_produto.close() or event == "Cancelar":
                cadastro_produto.close()
                break

            c.execute("INSERT INTO vendas (Produto, Valor) VALUES (?, ?)", (values["Produto"], values["Valor"]))
            conn.commit()

            sg.popup("Cadastro realizado com sucesso!", title="Cadastro")

    elif event == "Consulta Produto":
        consulta_layout_produto = [
            [sg.Text("produto")],
            [sg.InputText(key="produto")],
            [sg.Button("Consultar"), sg.Button("Cancelar")],
            [sg.Table(values=[], headings=["Produto", "Valor"], display_row_numbers=False, auto_size_columns=False,
                      num_rows=1, key="tabela")]
        ]
        consulta_produto = sg.Window("Consultar produto", consulta_layout_produto, resizable=True, size=(1000, 800))
        while True:
            event, values = consulta_produto.read()

            if event == sg.WIN_CLOSED or event == "Cancelar":
                consulta_produto.close()
                break

                # operações no banco de dados
            produto_busca = values["produto"].upper()
            c.execute("SELECT Produto, Valor FROM vendas WHERE UPPER(Produto) = ?", (produto_busca,))
            registros = c.fetchall()

            # atualizar
            tabela = consulta_produto["tabela"]
            tabela.update(values=registros)

    elif event == "Relatório Produto":
        relatorio_layout_produto = [
            [sg.Text("Produto")],
            [sg.InputText(key="Produto")],
            [sg.Button("Gerar relatório"), sg.Button("Cancelar")],
        ]
        relatorio_produto = sg.Window("Relatório de produto", relatorio_layout_produto, resizable=True,
                                      size=(1000, 800))
        while True:
            event, values = relatorio_produto.read()

            if event == sg.WIN_CLOSED or event == "Cancelar":
                relatorio_produto.close()
                break

            # operações no banco de dados para obter o produto e gerar o relatório
            produto_busca = values["Produto"].upper()
            c.execute("SELECT * FROM vendas WHERE UPPER(Produto) = ?", (produto_busca,))
            registros = c.fetchone()

            if registros:

                with open("relatorio.html", "w") as f:
                    f.write("<html><head></head><body>")
                    f.write(f"<h1>relatorio</h1><table border='1'><tr><th>Produto</th><th>Valor</th></tr>")
                    f.write(f"<tr><th>{registros[0]}</th><th>{registros[1]}</th></tr>")
                    #f.write(f"<tr><td>{registros[0]}<tr><td>{registros[1]}<tr>")
                    f.write("</body></html>")
                sg.popup("Relatório criado!", title="Relatório")

            else:
                sg.popup("Produto não encontrado no banco de dados!", title="Relatório")

            relatorio_produto["Produto"].update("")

conn.close()