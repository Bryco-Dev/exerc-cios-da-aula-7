class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    def depositar (self, valor):
        self.saldo += valor
        print(f'deposito de R$ {valor} realizado')

    def sacar (self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print (f'Saque de R$ {valor} realizado') 
        else:
            print('Tá duro, dorme')
    def exibir_saldo  (self):
            print(f'salfo atual Titular {self.titular} R$ {self.saldo}')