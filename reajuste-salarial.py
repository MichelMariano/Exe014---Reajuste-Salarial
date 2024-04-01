#Faça um algoritmo que leia o Salário de um funcionário e mostre seu novo salário.
#Com 15% de aumento

func = input('Digite o nome do Funcionário: ')
salário = float(input('Digite o Salário do Funcionário: R$ '))
novo = salário + (salário * 15 / 100)

print('O funcionário {} recebeu um aumento de 15% e seu Novo Salário é de R$ {:.2f} '.format(func, novo))
