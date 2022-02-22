#desafio 07
# Exiba a seguinte mensagem:
# "O funcionário aaa da empresa bbb terá o valor de R$ccc a deduzir do salário" (quando a alíquota for superior a zero)
# ou
# "O funcionário aaa da empresa bbb está isento de qualquer dedução" (quando a alíquota for igual a zero)
# Onde:
# aaa: nome do funcionário; bbb: nome da empresa; ccc: parcela a deduzir
# Utilize a seguinte tabela como base para calcular o valor da alíquota:
# Base de cálculo;Alíquota
# Até 1.903,98 = 0; De 1.903,99 até 2.826,65 = 7,50%; De 2.826,66 até 3.751,05 = 15%; De 3.751,06 até 4.664,68 = 22,50%; Acima de 4.664,68 = 27,50%

class Funcionario:
    
    def __init__(self, nome: str, empresa: str, salario: float):
        self.nome = nome
        self.empresa = empresa
        self.salario = salario


class ImpostoRenda:
    def __init__(self, funcionario: Funcionario):
        self.funcionario = funcionario()
        self.dedução = self.calc_aliquota()
        
    def calc_aliquota(self):
        if self.funcionario.salario > 4664.68:
            return self.funcionario.salario*0.275
        
        elif self.funcionario.salario > 3.751.05:
            return self.funcionario.salario*0.2250
        
        elif self.funcionario.salario > 2826.65:
            return self.funcionario.salario*0.15
        
        elif self.funcionario.salario > 1.903,98:
            return self.funcionario.salario*0.075
        
        else: 
            retun 0.00
            
    def __str__(self):
        
        if self.dedução > 0:
            return f"O funcionário {self.funciona.nome} da empresa {self.funciona.empresa} terá o valor de R${self.deducao} a deduzir do salário"
        else:
            return f"O funcionário {self.funciona.nome} da empresa {self.funciona.empresa} está isento de qualquer deduçã"