# Cenário Real - Gerenciador de login simples 

'''
Crie um gerenciador de login simples, com o maximo de 3 tentativas.
(teremos apenas um unico usuario e senha permitido)

usurio - gabriel
senha senha123

Após 3 tentativas, se o usuario estiver errado exibir:
"Aguarde 30 mins antes de tentar novamente!"

Se o usuario acertar o usuario e senha antes disso, exibir: "Login feito com sucesso!"
---
 5Q's para montar um algoritimo
 Analise criticamente o problema e descubra:
 (Tente explicar este problema para voce mesmo em voz alta e peca mais 
 informacoes/investigue maist ate voce compreender completamente o problema.)

 1. Quais são os dados de entrada necesserios?
 R: Preciso pedir ao usurio que insira um usuario e senha

 2. O que devo fazer com esses dados?
 R: Verificar se o usuario e senha que o usuario me passou esta correto, se estiver exibir:
 Login feito com sucesso! Caso o usuario insira o login e senha incorretamente mais de 3 vezes exibir:
  Aguarde 30 mins antes de tentar novamente!

 3. Quais são as restrições deste problema
 R: Devo receber do usuario o login e senha, e nao permitir o usuario ultrapasser 3 tentativas de login 

 4. Qual é o resultado esperado?
 R: Exibir Login feito com sucesso! se os dados inseridos pelo usuario forem corretos,
 ou exibir Aguarde 30 mins antes de tentar novamente!, caso o usuario ultrapasse 3 tentativas erradas de login

 5. Qual a sequencia de passos a ser feita para chegar no resultado esperado?
 - receber um usuario
 - receber uma senha 
 - verificar se ambas informacoes, estao corretas
 - se estiverem corretas exibir: Login feito com sucesso!
 - se o usurio inserir as informacoes incorretas mais de 3 vezes exibir: Aguarde 30 mins antes de tentar novamente!
'''

usuario =''
senha = ''
tentativas = 0

while (usuario != 'gabriel' or senha != 'senha123') and tentativas < 3:
    usuario = input("Digite seu nome de usuario: ")
    senha = input("Digite sua senha: ")
    tentativas += 1

if usuario == 'gabriel' and senha == 'senha123':
    print ('Login feito com sucesso!')
else: 
    print ('Aguarde 30 mins antes de tentar novamente!')