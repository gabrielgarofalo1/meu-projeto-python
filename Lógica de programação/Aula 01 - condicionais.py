# Condicionais - if elif else
# "== compara igualdade"

# E ae gabriel, bora dar uma saida hoje?
# Se eu terminar de estudar eu consigo


estudo_terminado = False
if estudo_terminado == True:
    print ("Bora!")
else:
    print ("Não vai dar mano, não terminei de estudar ainda.")


'''sytaxe
if condicao:
     código se verdadeiro
else:
     código em qualquer outro caso
    '''


  #  Exemplo 2
 
# Ei, Voce consegue me ajudar a mover essas caixas la para fora hoje a tarde?
# Se eu estiver livre, sim. Mas se nao der pede meu irmão para te ajudar.


estou_livre = True
if estou_livre == True:
    print ("Ok, bora la, estou livre vou te ajudar a levar as caixas.")
else:
    print ("Pede ao meu irmão, para te ajudar, agora não posso.")
    

  # Como lidar com mais que 2 condicoes? Usando elif

# Eu cheguei atrasado na aula. Ainda posso entrar?
#Se for a primeira ou segundo vez que voce chega atrasado, pode sim.
#Mas se for a terceira vez, nao podera entrar mais.


atrasos = int(input("Quantas vezes voce ja chegou atrasado na aula? "))
if atrasos >= 3:
    print ("Voce nao pode mais entrar na aula, ja chegou atrasado 3 vezes.")
elif atrasos == 2:
        print ("Voce pode entrar, mas essa é sua ultima chance, ja chegou atrasado 2 vezes.")
elif atrasos == 1:
        print ("Voce pode entrar, mas tome cuidado, ja chegou atrasado 1 vez.")     
else:
        print ("Voce pode entrar, seja bem vindo!") 
'''
        # problema
        crie um programa que recebe dois valores e exibe qual é o maior
q1= dois valores
q2= comparar os dois valores e exibir o maior
q3= 
    - valor 1
    - valor 2
q4= exibir o maior valor
q5= 
'''
input_valor1 = int(input ("Digite o primeiro valor: "))
input_valor2 = int(input ("Digite o segundo valor: "))
if input_valor1 > input_valor2:
    print (f"O maior valor é: {input_valor1}")
elif input_valor2 > input_valor1:
    print (f"O maior valor é: {input_valor2}")
else:
    print ("Os valores são iguais.") 