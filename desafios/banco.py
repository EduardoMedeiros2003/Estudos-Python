class ContaBancaria:
    contas = []
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self._ativo = False
        ContaBancaria.contas.append(self)

    def __str__(self):
        return f'{self.titular} | {self.saldo}'

    @classmethod
    def listar_conta(cls):
        for conta in cls.contas:
            print(f'O Titular da conta é: {conta.titular} e seu saldo é R$ {conta.saldo}! E esta com a conta {conta.ativo}')
    
    @property
    def ativo(self):
        return '-> Ativada' if self._ativo else '-> Desativada'
    
    def ativar_conta(self):
        self._ativo = not self._ativo # O not inverte o valor
        print('Conta Ativada com sucesso!')


pessoa1 = ContaBancaria('Eduardo', 20000000)
pessoa2 = ContaBancaria('Maria', 2140239)
pessoa1.ativar_conta()
ContaBancaria.listar_conta()
