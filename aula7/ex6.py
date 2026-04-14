from conta import ContaBancaria

conta1 = ContaBancaria('Bryca0', 300000)
conta2 = ContaBancaria('Joana', 1621.61)

conta1.exibir_saldo()
conta1.depositar(100000)
conta1.exibir_saldo()
conta1.sacar(1000000)
conta1.sacar(15000)
conta1.exibir_saldo()

contas = []
for i in range (5):
    nome = input('Nome ')
    saldo = float(input('Saldo'))
    contas.append(ContaBancaria(nome, saldo))

for conta in contas:
    print(f'{conta.titular} R$ {conta.saldo}')