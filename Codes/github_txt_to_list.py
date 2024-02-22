# -*- coding: utf-8 -*-
"""
File generated by Douglas Souza
douglas@ufv.br

"""

#Carregar o arquivo de frases gravado no GitHub e trasnformar em uma lista de frases
#Insira o link raw do arquivo TXT
arquivo_frases = requests.get("seulinkaqui").text

def converter_para_lista_de_frases(conteudo):
    if conteudo is not None:
        # Dividir o conteúdo em linhas e remover espaços em branco desnecessários
        linhas = [linha.strip() for linha in conteudo.splitlines()]

        # Remover linhas em branco
        linhas = [linha for linha in linhas if linha]

        return linhas
    else:
        return None

lista_de_frases = converter_para_lista_de_frases(arquivo_frases)
