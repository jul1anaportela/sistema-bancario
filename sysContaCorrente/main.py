from ContaCorrente import ContaCorrente, CartaoCredito
from Agencia import AgenciaPremium, AgenciaComum, AgenciaVirtual


#programa
# conta_juliana = ContaCorrente('juliana', '111.222.333-45', 1234, 34062 )
# cartao_juliana = CartaoCredito('juliana', conta_juliana)    

# print(cartao_juliana.conta_corrente.num_conta)

# #print(conta_juliana.cartoes[0].numero)

# print(cartao_juliana.validade)

# print(cartao_juliana.numero)
# print(cartao_juliana.cod_seguranca)

# cartao_juliana.senha = '2345' #chama sem o underline mesmo
# # help(ContaCorrente)

#lista todos os atributos atributos da classe criada (consulta todos os valores que estão naquela instância)
# print(conta_juliana.__dict__)
# print(cartao_juliana.__dict__)

agencia_premium_especial = AgenciaPremium(2222222, 3232323)
