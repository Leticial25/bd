from distutils.util import execute
import PySimpleGUI as sg
import sqlite3 as banco
# INICIANDO A CONEXÂO COM O BANCO DE DADOS
conn = banco.connect("clientes.db")
c = conn.cursor()


# BOTÂO DO MENU PRINCIPAL COM A OPÇÂO DE CADASTRAR
sg.theme("DarkTeal12")
layout = [
    [sg.Button("Cadastrar", size=(20, 2), font=("Arial", 12))],
    [sg.Button("Cadastrar_Fornecedor", size=(20, 2), font=("Arial", 12))],
    [sg.Button("Cadastrar_Transportadora", size=(20, 2), font=("Arial", 12))],
    [sg.Button("Consultar", size=(20, 2), font=("Arial", 12))]
]

# NOME QUE APARECE NO SISTEMA E DEFINIÇÂO DO TAMANHO DA TELA  
window = sg.Window("Sistema de Cadastro Vs.1.0",layout,size=(230,200)) 

while True:
    event, values = window.read()

    #SE a janela for fechada Encerra o Processo de cadastro
    if event == sg.WINDOW_CLOSED:
        break







    #CADASTRO DE CLIENTES

    if event == "Cadastrar":

        #criar layout da seguna tela que aparece quando clica em cadastrar cliente
        cadastro_layout = [
            [sg.Text("Nome")],      
            [sg.InputText(key="nome")],
            [sg.Text("CPF")],      
            [sg.InputText(key="cpf")],
            [sg.Text("Endereço")],      
            [sg.InputText(key="endereco")],
            [sg.Text("Telefone")],      
            [sg.InputText(key="telefone")],
            [sg.Text("Cidade")],      
            [sg.InputText(key="cidade")],
            [sg.Text("Estado")],      
            [sg.InputText(key="estado")],                       
            [sg.Button("Cadastrar")],
            [sg.Button("Cancelar")]
        ]
            

        cadastro_window = sg.Window("Cadastro de Clientes", cadastro_layout, size=(400,500))

         #While da janela de  cadastro de clientes
        while True:
            event, values = cadastro_window.read()
     
            if event == sg.WINDOW_CLOSED or event == "Cancelar":
                cadastro_window.close()
                break


            #interagindo com o banco
            c.execute("INSERT INTO clientes (nome, cpf, endereco, telefone, cidade, estado) VALUES (?, ?, ?, ?, ?, ?)", (values["nome"], values["cpf"],values["endereco"],values["telefone"],values["cidade"],values["estado"]))
            conn.commit()

            #Limpar iputs após o cadastro
            cadastro_window["nome"].update("")
            cadastro_window["cpf"].update("")
            cadastro_window["endereco"].update("")
            cadastro_window["telefone"].update("")
            cadastro_window["cidade"].update("")
            cadastro_window["estado"].update("")

            #Confirmar o cadastro
            sg.popup("Cadastro realizado com sucesso!", title="Cadastro")

        cadastro_window.close()





#CADASTRO DE FORNECEDORES

    elif event == "Cadastrar_Fornecedor":

        #criar layout da seguna tela que aparece quando clica em cadastrar cliente
        fornecedor_layout = [
            [sg.Text("Nome")],      
            [sg.InputText(key="nome")],
            [sg.Text("CNPJ")],      
            [sg.InputText(key="cnpj")],
            [sg.Text("Endereço")],      
            [sg.InputText(key="endereco")],
            [sg.Text("Telefone")],      
            [sg.InputText(key="telefone")],
            [sg.Text("Cidade")],      
            [sg.InputText(key="cidade")],
            [sg.Text("Estado")],      
            [sg.InputText(key="estado")],                       
            [sg.Button("Cadastrar")],
            [sg.Button("Cancelar")]
        ]
    

        fornecedor_window = sg.Window("Cadastro de Fornecedores", fornecedor_layout, size=(400,500))

         #While da janela de  cadastro de fornecedores
        while True:
            event, values = fornecedor_window.read()
     
            if event == sg.WINDOW_CLOSED or event == "Cancelar":
                fornecedor_window.close()
                break


            #interagindo com o banco esalvando os dados
            c.execute("INSERT INTO fornecedor (nome, cnpj, endereco, telefone, cidade, estado) VALUES (?, ?, ?, ?, ?, ?)", (values["nome"], values["cnpj"],values["endereco"],values["telefone"],values["cidade"],values["estado"]))
            conn.commit()

            #Limpar iputs após o cadastro
            fornecedor_window["nome"].update("")
            fornecedor_window["cnpj"].update("")
            fornecedor_window["endereco"].update("")
            fornecedor_window["telefone"].update("")
            fornecedor_window["cidade"].update("")
            fornecedor_window["estado"].update("")

            #Confirmar o cadastro
            sg.popup("Fornecedor Cadastrado com sucesso!", title="Cadastro")

        fornecedor_window.close()





    elif event == "Cadastrar_Transportadora":

        #criar layout da seguna tela que aparece quando clica em cadastrar Transportadora
        transp_layout = [
            [sg.Text("Nome")],      
            [sg.InputText(key="nome")],
            [sg.Text("CNPJ")],      
            [sg.InputText(key="cnpj")],
            [sg.Text("Endereço")],      
            [sg.InputText(key="endereco")],
            [sg.Text("Telefone")],      
            [sg.InputText(key="telefone")],
            [sg.Text("Cidade")],      
            [sg.InputText(key="cidade")],
            [sg.Text("Estado")],      
            [sg.InputText(key="estado")],                       
            [sg.Button("Cadastrar")],
            [sg.Button("Cancelar")]
        ]
    

        transp_window = sg.Window("Cadastro de Transportadoras", transp_layout, size=(400,500))

         #While da janela de  cadastro de fornecedores
        while True:
            event, values = transp_window.read()
     
            if event == sg.WINDOW_CLOSED or event == "Cancelar":
                transp_window.close()
                break


            #interagindo com o banco esalvando os dados
            c.execute("INSERT INTO transport (nome, cnpj, endereco, telefone, cidade, estado) VALUES (?, ?, ?, ?, ?, ?)", (values["nome"], values["cnpj"],values["endereco"],values["telefone"],values["cidade"],values["estado"]))
            conn.commit()

            #Limpar iputs após o cadastro
            transp_window["nome"].update("")
            transp_window["cnpj"].update("")
            transp_window["endereco"].update("")
            transp_window["telefone"].update("")
            transp_window["cidade"].update("")
            transp_window["estado"].update("")


    elif event == "Consultar":
    
            consulta_layout =[
                [sg.Text("Clientes")],
                [sg.InputText(key="clientes")],
                [sg.Button("Consultar")],
                [sg.Button("Cancelar")],
                [sg.Table(values=[], headings=["nome","cpf"], display_row_numbers=False, auto_size_columns=False, num_rows=10, key="tabela")]
            ]    
            consulta_window = sg.Window("Consulta de Clientes", consulta_layout, resizable=True)

        #loop eventos
        
            while True:
                event, values = consulta_window.read()
            
                if event == sg.WIN_CLOSED or event == "Cancelar":
                    consulta_window.close()
                    break

                # operações no banco de dados
                produto_busca = values["clientes"].upper()
                c.execute( "SELECT nome, cpf FROM clientes WHERE UPPER(nome) = ?",(produto_busca,))
                registros = c.fetchall()

                # ATUALIZAR
                tabela = consulta_window["tabela"]
                tabela.update(values=registros)     
                       
            consulta_window.close()                        


conn.close() 