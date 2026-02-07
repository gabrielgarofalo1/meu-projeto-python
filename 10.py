# Variáveis 
internet_speed = 500
# print (internet_speed)
# Números inteiros (int)
idade = 15
# Números decimais (float)
nota = 8.5
# String (textos) (str)
nome_completo = "gabriel garofalo silva"
# Booleanos (decisões: True or False) (bool)
can_enter = True

# print (type (nome_completo))





# Problema 1  Valor hora 
# Escreva um program que retorna o valor hora de um funcionario
# com base no seu salario mensal e horas trabalhadas por mês
''' 
 q1= total de horas trabalhadas por mes salario mensal 

 q2= devo pegar o valor do salario mensal do funcionario e devo dividir com o valor das horas totais trabalhadas

 q3= 
    - Salário mensal
    - Horas trabalhadas por mes 

 q4= Exibir o valor hora do funcionario no mês

 q5= 
 receber o salario mensal
 recebre o total de horas trabalhadas por mes
 valor hora = salario mensal / quantidade de horas trabalhadas por mes
 exbir o valor hora



# salario_mensal = input ('Qual é seu salario mensal?')
# horas_trabalhadas = input ('Quantas horas voce trabalha por mes?')
# valor_hora = float (salario_mensal)/ int (horas_trabalhadas) # Aqui é preciso colocar o float e o int antes das duas variaveis, pois não é possivel fazer calculos de textos, fazendo assim elas virarem dois números.
# print (valor_hora)


# Condicionais - if elif else
# "== compara igualdade"


E ae gabriel, bora dar uma saida hoje?
Se eu terminar de estudar eu consigo


estudo_terminado = False
if estudo_terminado == True:
    print ("Bora!")
else:
    print ("Não vai dar mano, não terminei de estudar ainda.")


sytaxe
if condicao:
    # código se verdadeiro
else:
    # código em qualquer outro caso
    

  Exemplo 2
 
Ei, Voce consegue me ajudar a mover essas caixas la para fora hoje a tarde?
Se eu estiver livre, sim. Mas se nao der pede meu irmão para te ajudar.


estou_livre = True
if estou_livre == True:
    print ("Ok, bora la, estou livre vou te ajudar a levar as caixas.")
else:
    print ("Pede ao meu irmão, para te ajudar, agora não posso.")


# Como lidar com mais que 2 condicoes? Usando elif

# Eu cheguei atrasado na aula. Ainda posso entrar?

Se for a primeira ou segundo vez que voce chega atrasado, pode sim.
Mas se for a terceira vez, nao podera entrar mais.


atrasos = int(input("Quantas vezes voce ja chegou atrasado na aula? "))
if atrasos >= 3:
    print ("Voce nao pode mais entrar na aula, ja chegou atrasado 3 vezes.")
elif atrasos == 2:
        print ("Voce pode entrar, mas essa é sua ultima chance, ja chegou atrasado 2 vezes.")
elif atrasos == 1:
        print ("Voce pode entrar, mas tome cuidado, ja chegou atrasado 1 vez.")     
else:
        print ("Voce pode entrar, seja bem vindo!") 

        # problema
        crie um programa que recebe dois valores e exibe qual é o maior
q1= dois valores
q2= comparar os dois valores e exibir o maior
q3= 
    - valor 1
    - valor 2
q4= exibir o maior valor
q5= 

input_valor1 = int(input ("Digite o primeiro valor: "))
input_valor2 = int(input ("Digite o segundo valor: "))
if input_valor1 > input_valor2:
    print (f"O maior valor é: {input_valor1}")
elif input_valor2 > input_valor1:
    print (f"O maior valor é: {input_valor2}")
else:
    print ("Os valores são iguais.")        
    

# Laços de repetição - loops
# for e while
for i in range (2,11,2): # range (5) significa que o loop vai de 0 a 4, ou seja, 5 vezes.
    print (f"Repetição número {i}") 
    

# Lista de nomes
nomes = ["Gabriel", "Ana", "João", "Maria"]
dados = [15, 8.5, "gabriel garofalo silva", True]
idades = [12, 15, 18, 20, 25, 30]
for nome in nomes:
    print (f"Olá, {nome}!")
for dado in dados:
    print (f"Dado: {dado}")
for idade in idades:
    if idade >= 18:
        print (f"Idade {idade}: Maior de idade")
    else:
        print (f"Idade {idade}: Menor de idade")
        
# Problema faca um sista que precisa verificar se todas as senha digitads por usuarios sao validas  
# para ela ser valida ele deve contem ao menos 6 caracteres.
q1= senha digitada pelo usuario
q2= verificar se a senha tem ao menos 6 caracteres  
q3= 
    - senha
q4= exibir se a senha é valida ou invalida
q5= 
receber a senha
verificar se ela possui ao menos 6 caracteres
exibir se a senha é valida ou invalida   

len(variavel) # função que retorna a quantidade de caracteres de uma string
len(senha) # retorna a quantidade de caracteres da variavel senha


senhas = ["abc123", "minha_senha", "123", "senha_segura_2024", "pwd"]
for senha in senhas:
     if len(senha) >= 6:
         print (f"Senha '{senha}' é válida.")
     else:
         print (f"Senha '{senha}' é inválida.")
while condicao:
código enquanto a condição for verdadeira
  
  Criar um programa que permite 3 tentativas de login
q1= tentativas de login 
q2= permitir 3 tentativas de login
q3= 
    - usuario
    - senha
q4= permitir 3 tentativas de login
q5= 
receber usuario e senha
permitir 3 tentativas de login

  '''
tentativas = 3
while tentativas > 0:
    input_usuario = input ("Digite seu usuario: ")
    input_senha = input ("Digite sua senha: ")
    if input_usuario == "admin" and input_senha == "12345":
        print ("Login bem sucedido!")
        break
    else:
        tentativas -= 1
        print (f"Login falhou. Voce tem {tentativas} tentativas restantes.")
        