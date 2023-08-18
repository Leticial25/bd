import PySimpleGUI as sg
import sqlite3 as bbb


#Teste de conexão com o banco
try:

#faz conexão com o banco
    conn = bbb.connect("vendas.db")

#interage com o banco
    c = conn.cursar()

    c.execute("SELECT sqlite_version();") #executar o query
    version = c.fetchone() #guarda resultado da query

    if version: 
        print("Conexão realizada com sucesso!")
    else: 
       print("Falha na conexão:")


except: bbb.error as erro:
      print("Falha na conexão: {erro}") # guarda na variável o erro encontrado

finally:

     conn.close() #Fecha a conexão
