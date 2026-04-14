estoque = {
    1 : {'nome': 'notebook', 'preco': 3500, 'qtd':12},
    2 : {'nome': 'mouse', 'preco': 500, 'qtd':2},
    1 : {'nome': 'monitor', 'preco': 1500, 'qtd':20}}

for     codigo,produto in estoque.items():
    print(f'{codigo} - {produto ['nome']} R$ {produto['preco']}')

#{dicionario}

