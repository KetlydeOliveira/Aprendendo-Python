# Definindo uma variável do tipo texto (string)
nome = ("Seu nome")




#Usando uma f-string para exibir uma mensagem personalizada na tela
print (f" E aí {nome}! Seu primeiro código está salvo")





#Condicional: O código faz uma pergunta e toma uma decisão baseada na resposta.

idade = int(input("Digite sua idade aqui:"))
if idade >= 18:    
    print("Acesso liberado")
else:
    print ("Acesso negado")    







#Tipos primitivos: São os tipos básicos de dado que o Python entende:

#tipo.        #descrição.                #exemplo

int.          número inteiro.            idade = 20
float.        número real (decimal).     altura = 1.75           
str.          texto (string).            nome = "Ana"
bool.         verdadeiro/falso.          ativo = "true"








#Simulador de Aprovação de Compra - Cartão de Crédito

# Definindo o limite disponível no cartão (tipo float para dinheiro) limite = 1000.00
# Recebendo o valor da compra e convertendo para número decimal compra = float(input("Valor da compra: "))
# Condicional: Verifica se o valor da compra cabe no limite disponível if compra <= limite: print("Compra aprovada!")


limite = 1000.00
compra = float(input("Valor da compra: "))    
if compra <= limite:
    print ("Compra aprovada!")
else:
     print ("Compra recusada!")








# PROJETO: Validador de Rotina com Lógica Booleana

# Pergunta se treinou e guarda a resposta
treinou_hoje = input("Voce treinou hoje? (sim/nao): ")

# Pergunta se comeu o pão e guarda a resposta
comeu_pao = input("Comeu seu pao frances? (sim/nao): ")

# Se treinou E comeu o pão, faz o que está abaixo
if treinou_hoje == "sim" and comeu_pao == "sim":
    
    # Mensagem caso as duas respostas sejam "sim"
    print("Status: Dia de vitoria! Meta batida. ✅")

# Caso contrário (se uma das respostas for "nao")
else:
    
    # Mensagem caso algo tenha faltado
    print("Status: Ops, faltou alguma coisa hoje. ❌")








#Sistema de Validação de Acesso com Limite de Tentativas.


import os # Importa a biblioteca para comandos do sistema

# Define a senha e as variáveis de controle
senha_correta = "fdksk"
tentativa = ""
erros = 0

# O while vai rodar enquanto a senha estiver errada E você não tiver errado 3 vezes
while tentativa != senha_correta and erros < 3:
    tentativa = input("Qual é a senha? ")
    
    # Se a senha digitada for diferente da correta, limpa a tela e soma 1 erro
    if tentativa != senha_correta:
        erros = erros + 1
        os.system('clear') # Limpa a tela do terminal
        print("Senha incorreta!")
        print("Erros: ", erros)

# Agora o código sai do while e verifica o que aconteceu:

if tentativa == senha_correta: # Se saiu porque a senha está certa
    print("Acesso concedido!")
else: # Se saiu porque o erro chegou a 3
    print("Número de tentativas excedido. Conta bloqueada!")
