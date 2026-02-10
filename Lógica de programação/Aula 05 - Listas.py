# Listas
#         [20, 50, 100]
# indices  0    1    2  (ou seja 0 equivale a 20, 1 equivale a 50, 3 equivale a 100 e assim por diante...)
''''
nomes = ['gabriel', 'rafael', 'miguel']
 print(nomes[0]) # Exibiria gabriel neste caso

# Encontrar o indice de forma automatica
 print(nomes.index('miguel')) # nesse caso ele iria me exibir 2, que seria o indice do nome desejado

# Manipular listas - add novos itens
salarios = [2500, 4000, 9000]
salario_usuario = float(input('Qual é o seu salario?'))
salarios.append(salario_usuario) # nesse caso o "append" esta adicionando o salario que pedi ao usuario na lista inicial
print(salarios)
'''

# Problema Real - Gastos totais com pagamento de salarios.
# Dado uma lista de salarios, calcule o total pago a todos os funcionarios
salarios = [2100, 1620, 7000, 9000, 12000, 5400]
total = 0
for salario in salarios:
    total = total + salario # 2100 -> 2100 + 1620 -> 3720 + 7000...
print(total)