#1009 - Salário com Bônus
nome = input()
salario = float(input())
vendas = float(input())

total = salario + vendas * 15 / 100

print(f'TOTAL = R$ {total:.2f}')
