from random import randint

class Agencia:
    
    def __init__(self, telefone, cnpj, numero):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self.caixa = 0
        self.emprestimos = []
    
    def verificar_caixa(self):
        if self.caixa < 1000000:
            print('Caixa abaixo do nível recomendado. Caixa atual: {}'.format(self.caixa))
        else:
            print('O valor de Caixa está ok. Caixa atual: {}'.format(self.caixa))
    
    def emprestar_dinherio(self, valor, cpf, juros):
        if self.caixa > valor:
            self.emprestimos.append((valor, cpf, juros))
        else:
            print('Emprestimo não é possível. Dinheiro não disponível em caixa.')
        
    def adicionar_cliente(self, nome, cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))
 

class AgenciaVirtual(Agencia):
    
    def __init__(self, site, telefone, cnpj):
        super().__init__(telefone, cnpj, 1000)
        self.site = site
        self.caixa = 1000000
        self.caixa_paypal = 0
    
    def depositar_paypal(self, valor):
        self.caixa -= valor
        self.caixa_paypal += valor
        #colocar uma condição se não tiver dinheiro disponível
    
    def sacar_paypal(self, valor):
        self.caixa_paypal -= valor
        self.caixa += valor
        #colocar uma condição se não tiver dinheiro disponível
    
    
class AgenciaComum(Agencia):
    
    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=randint(1000, 9999))
        self.caixa = 1000000
        


class AgenciaPremium(Agencia):
    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=randint(1000, 9999))
        self.caixa = 10000000
    
    def adicionar_cliente(self, nome, cpf, patrimonio):
        if patrimonio > 1000000:
            super().adicionar_cliente(nome, cpf, patrimonio)
        else:
            print('O cliente não tem o patrimônio mínimo necessário para entrar na Agencia Premium')



if __name__ == '__main__':
    #se for dentro da classe esse bloco de código teste vai rodar, se for dentro da main ele não vai rodar
    #testes da classe
    
    agencia_premium = AgenciaPremium(2323232, 423423423)
    agencia_premium.adicionar_cliente('juliana', 89248223413, 2000000)
    print(agencia_premium.clientes)

