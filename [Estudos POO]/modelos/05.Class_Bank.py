class Bank_account():
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    def __str__(self):
        return f'{self._titular}\n' \
               f'         | Saldo: {self._saldo}\n'\
               f'         | Ativo: {self._ativo}'

    @property
    def titular(self):
        return self._titular
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def ativo(self):
        return self._ativo

    

    def ativar_conta(self):
        self._ativo = not self._ativo
        return f'self._ativo'

class BankClient():
    clients = []

    def __init__(self, cpf, nome, endereco, telefone, profissao ):
        self._cpf = cpf
        self._nome = nome
        self._endereco = endereco
        self._telefone = telefone
        self._profissao = profissao

        BankClient.clients.append(self)

    @classmethod
    def consultor(cls):
        for client in cls.clients:
            print(vars(client))


client1 = BankClient('44415126863', 'Kendrick', 'Cabeça do Drake', '19983484407', 'Rapper')
client2 = BankClient('23217892848', 'Djonga', 'Belo Horizonte',    '19998623541', 'Rapper')
client3 = BankClient('22268945207', 'Mano Brown', 'Capão', '19932665489', 'Rapper')
BankClient.consultor()

cliente1 = Bank_account('Kendrick','R$ 9500')
Bank_account.ativar_conta(cliente1)
print(cliente1)
cliente1 = Bank_account('Djonga','R$ 9900')
print(cliente1)
        