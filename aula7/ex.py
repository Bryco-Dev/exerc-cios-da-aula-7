meses = ['JAN', 'FEV', 'MAR', 'ABRIL', 'MAIO', 'JULHO', 'AGO','SET', 'OUT', 'NOV', 'DEZ']
salarios = []

for i in range (12):
    #appen é adicionar as coisas sequencial
    salarios.append(float(input(f'Salario de {meses [i]}')))

soma = 0 

    #i dentro de um conjunto, ele pega um por um

for salario in salarios:
    soma += salario 

sal13 = soma / len (salarios)

ferias = sal13 * 1/3