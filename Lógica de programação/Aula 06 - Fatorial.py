# Projeto 1 - Fatorial de um numero
# Crie um programa que recebe um numero e imprime o fatorial dele

numero = int(input('Digite o numero, que voce quer saber o fatorial: '))
if numero > 0 and type(numero) == int:
    fatorial = 1 # inicia com 1 pois nesse caso estamos fazendo o fatorial de um numero do primeiro ate o numero que queremos
    for item in range(1, numero+1):
        print(f'{fatorial} * {item}')
        fatorial = fatorial * item
        print(f'{fatorial}')
    print(f'o fatorial de {numero} é {fatorial}')
else:
    print ('favor informe um numero inteiro e positivo')
