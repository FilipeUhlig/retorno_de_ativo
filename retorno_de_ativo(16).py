"""
Programa: Calculadora de retorno de um ativo
Descrição: Este programa calcula o retorno esperado de um ativo.
Autor: Filipe
Data: 06/06/2023
Versão: 0.0.1
"""
#Atribuição de variáveis


#Entrada de dados
Rf = float(input("Qual o valor do retorno do ativo sem risco? "))
Rm = float(input("Qual o valor do retorno da carteira de mercado? "))
βi = float(input("Qual o valor do coeficiente de sensibilidade do retorno do ativo a variações no prêmio de risco do mercado? "))


#Processamento de dados

E = ((Rf + (βi*(Rm - Rf))))


#Saida de dados
print(f"O Retorno esperado do ativo é de {E}.")
