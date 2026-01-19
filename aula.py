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
