import pyautogui as pa
import pandas as pd
from time import sleep

#Passo 1: entrar no sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

pa.PAUSE = 0.3 # Define o tempo de espera entre os comandos

pa.press('win')
pa.write('Crhome')
pa.press('enter')
pa.click(x=685, y=499)
pa.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pa.press('enter')
sleep(5) # Eperar um tempo maior para carregar o site 


#Passo 2: Fazer Login
pa.click(x=728, y=373)
pa.write('victor@gmail')
pa.press('tab')
pa.write('senha123')
pa.press('tab')
pa.press('enter')

#Passo 3: Abrir base de dados
tabela = pd.read_csv('produtos.csv')

#Passo 4: cadastrar Produtos
    # Repeir o passo 4 até o fim da lista de produtos
for linha in tabela.index:
    #Codigo do produto
    pa.click(x=723, y=259)
    codigo = str(tabela.loc[linha,'codigo'])
    pa.write(codigo)
    pa.press('tab')

    #Marca do produto
    marca = str(tabela.loc[linha, 'marca'])
    pa.write(marca)
    pa.press('tab')

    #Tipo do produto
    tipo = str(tabela.loc[linha, 'tipo'])
    pa.write(tipo)
    pa.press('tab')

    #Categoria do produto
    categoria = str(tabela.loc[linha, 'categoria'])
    pa.write(categoria)
    pa.press('tab')

    #Preço do produto
    preco = str(tabela.loc[linha, 'preco_unitario'])
    pa.write(preco)
    pa.press('tab')

    #Custo do produto
    custo = str(tabela.loc[linha, 'custo'])
    pa.write(custo)
    pa.press('tab')

    #OBS do produto
    obs = str(tabela.loc[linha, 'obs'])
    if obs != 'nan':
        pa.write(obs)
    pa.press('tab')
    pa.press('enter')
    pa.scroll(5000)


