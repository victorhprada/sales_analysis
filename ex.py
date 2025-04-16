lista_de_listas = [[4,6,5,9], [1,0,7,2], [3,4,1,8]]

def soma(lista: list[0]) -> float:

    total = sum(lista)

    return total

calcula_soma = [round(soma(lista_de_listas), 1) for lista_de_listas in lista_de_listas]
print(calcula_soma)

lista_de_tuplas = [('Pedro', 1.74, 81), ('Júlia', 1.65, 67), ('Otávio', 1.81, 83)]

peso = [peso[2] for peso in lista_de_tuplas]
print(peso)

lista = ['Pedro', 'Júlia', 'Otávio', 'Eduardo']
new_list = list(enumerate(lista))
print(new_list)

aluguel = [('Apartamento', 1700), ('Apartamento', 1400), ('Casa', 2150), ('Apartamento', 1900), ('Casa', 1100)]
tipo_domicilio = [tipo[0] for tipo in aluguel]
valor_aluguel = [valor[1] for valor in aluguel]

new_aluguel = list(zip(tipo_domicilio, valor_aluguel))

aluguel_apartamento = [valor for tipo, valor in new_aluguel if tipo == 'Apartamento']

print(aluguel_apartamento)

meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
despesa = [860, 490, 1010, 780, 900, 630, 590, 770, 620, 560, 840, 360]

despesa_mensal = {meses[i]: despesa[i] for i in range(len(despesa))}
print(despesa_mensal)

vendas = [('2023', 4093), ('2021', 4320), ('2021', 5959), ('2022', 8883), ('2023', 9859), ('2022', 5141), 
          ('2022', 7688), ('2022', 9544), ('2023', 4794), ('2021', 7178), ('2022', 3030), ('2021', 7471), 
          ('2022', 4226), ('2022', 8190), ('2021', 9680), ('2022', 5616)]

ano_vendas = [ano[0] for ano in vendas]
vendas_ano = [vendas_a[1] for vendas_a in vendas]

new_vendas = list(zip(ano_vendas, vendas_ano))

ano_vendas_final = [vendas_ano for ano_vendas, vendas_ano in new_vendas if ano_vendas == '2022' and vendas_ano > 6000]
print(ano_vendas_final)

glicemia = [129, 82, 60, 97, 101, 65, 62, 167, 87, 53, 58, 92, 66, 120, 109, 62, 86, 96, 103, 88, 155, 52, 89, 73]
