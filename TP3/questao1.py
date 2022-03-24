'''
{Desenvolva uma função que calcule a divisão de uma conta de consumo (conta de restaurante ou bar), em reais, considerando o número de pessoas que estavam consumindo e a taxa de serviço que será paga ao garçom.

Ao usuário do programa serão solicitados o valor total do consumo, em reais, o número total de pessoas e o percentual do serviço prestado, entre 0 e 100.

Fluxo de exceção: 

O programa deve verificar se o número total de pessoas é maior do que zero.
O programa deve verificar se o percentual do serviço está dentro do intervalo válido, de 0 a 100. 
Caso valores inválidos sejam digitados, deve ser exibida a mensagem de erro “Valor inválido” e o programa deve ser interrompido.
 Dica: Em Python, o valor monetário calculado ao final pode ser informado, na função print(), usando vírgula como separador de casa decimal, em vez de pontos.

Para isso, converta o valor final da conta em uma string, usando a função str() e, em seguida, substitua os pontos por vírgulas com replace('.',',')
'''

class Conta:
    def __init__(self,val_total: float, num_pessoas: int, tx_servico: int):
        self.valTotal=val_total if val_total > 0 else print("valor total inválido")
        self.numPessoas=num_pessoas if num_pessoas > 0 else print("numero de pessoas invalido")
        self.txServico=tx_servico if tx_servico>-1 and tx_servico<101 else print("taxa de serviço invalida")
        self.valTotalTxServico= self.calcula_total_com_taxa_servico()
        self.imprime_conta= print(self.__str__()) if self.valTotal and self.numPessoas and self.txServico else print("Ocorreu um erro. A entidade nao pode ser processada.")
        
    def calcula_total_com_taxa_servico(self) -> float:
        return round(valTotal*(float(f'1.{txServico}')), 2)

    def __str__(self):
        return (f'valor total:{str(self.valTotal).replace(".", ",")}\nvalor total com taxa de serviço: R${str(self.valTotalTxServico).replace(".", ",")}: divisão sugerida por pessoa:{str(round(self.valTotalTxServico/self.numPessoas,2)).replace(".", ",")}')
    

try: 
    valTotal=float(input("digite o valor total da conta:"))
    numPessoas=int(input("digite o numero total de pessoas:"))
    txServico=int(input("escolha uma taxa de servico de 0 até 100:"))
    conta = Conta(valTotal,numPessoas,txServico)
    conta.imprime_conta
except(ValueError):
    print("Valor digitado nao pode ser processado")