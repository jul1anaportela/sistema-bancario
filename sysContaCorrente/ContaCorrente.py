from datetime import datetime
import pytz
from random import randint


class ContaCorrente:
    """
    
    Cria um objeto ContaCorrente para gerenciar as contas dos clientes
    
    Atributos:
        nome (str): Nome do Cliente
        cpf (str): cpf do cliente, colocar pontos e traço
        agencia (int): agencia responsável pela conta do Cliente
        num_conta (int): Número da Conta Corrente do cliente
        saldo (float): Saldo disponível na conta do cliente
        limite (float): limite de cheque especial daquele cliente
        transacoes (list): Histórico de Transações do Cliente

    """
    
    #método estático: não usa nenhuma informação da classe ou da instância
    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S')
        
    def __init__(self, nome, cpf, agencia, num_conta):
        self.nome = nome #atributo com _ na frete só pode ser editado por meio de métodos, ou seja, não pode ser editado diretamente
        self.cpf = cpf
        self._saldo = 0
        self._limite = None
        self.agencia = agencia
        self.num_conta = num_conta
        self._transacoes = []
        self.cartoes = [] #atributo que é acessado por outra classe então não vai ter o underline
    
    def consultar_saldo(self):
        print(f'Seu saldo atual é de R${self._saldo:,.2f}')
    
    def depositar(self, valor):
        self._saldo += valor
        self._transacoes.append((valor, self._saldo, ContaCorrente._data_hora()))   
    
    def _limite_conta(self):
        self._limite = -1000
        return self._limite
    
    def sacar(self, valor):
        if self._saldo - valor < self._limite_conta():
            print('você não tem saldo suficiente para realizar esse saque. PARA DE SER DOIDA (Márcia sensitiva voices')
            self.consultar_saldo() #chamando um método dentro de outro método
        else:
            self._saldo -= valor
            self._transacoes.append((-valor, self._saldo, ContaCorrente._data_hora()))
    
    def consultar_limite_chequeespecial(self):
        print(f'Seu limite de Cheque Especial é de R${self._limite_conta():,.2f}')
        
    def consultar_historico_transacoes(self):
        print('Histórico de Transações: ')
        print('Valor, Saldo, Data e Hora')
        for transacao in self._transacoes:
            print(transacao)
            
    def transferir(self, valor, conta_destino):
        self._saldo -= valor
        self._transacoes.append((-valor, self._saldo, ContaCorrente._data_hora()))
        conta_destino.saldo += valor
        conta_destino._transacoes.append((valor, conta_destino.saldo, ContaCorrente._data_hora()))


class CartaoCredito:
    
    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR
    
    def __init__ (self, titular, conta_corrente):
        self.numero = randint(1000000000000000, 9999999999999999)
        self.titular = titular
        self.validade = '{}/{}'.format(CartaoCredito._data_hora().month, CartaoCredito._data_hora().year + 4)
        self.cod_seguranca = '{}{}{}'.format(randint(0,9),randint(0,9), randint(0,9))
        self.limite = 1000
        self._senha = '1234'
        self.conta_corrente = conta_corrente
        conta_corrente.cartoes.append(self)
    
    #metodos getter e setter -> usado quando um atributo for privado mas mesmo assim eu quero deixar o usuário alterar ele, porém com algumas restrinções
    @property
    def senha(self):
        #logica (getter)
        return self._senha

    @senha.setter
    def senha(self, valor):
        if len(valor) == 4 and valor.isnumeric():
            self._senha = valor
        else:
            print('nova senha inválida')