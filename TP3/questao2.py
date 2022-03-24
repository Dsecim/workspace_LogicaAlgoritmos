'''
Desenvolva uma função que recebe a idade de uma pessoa e informe se essa pessoa é:

Eleitor obrigatório (18 anos completos e menos de 70 anos de idade)
Eleitor facultativo (16 anos completos e menos de 18 anos ou 70 anos de idade ou mais).
Não tem direito a voto (menor de 16 anos).
Fluxo de exceção: 

O programa deve verificar se a idade da pessoa é maior do que zero.
Exemplos de saída do programa:

Informe a idade: 25 
Tem obrigação de votar.
Informe a idade: 75
Não tem obrigação de votar.
Informe a idade: 12
Não tem direito a voto.
'''

class PessoaEleitor:
    def __init__(self,nome: str, idade: int):
        self._nome=nome if isinstance(nome, str) and nome!="" else print("Nome invalido")
        self._idade=idade if isinstance(idade,int) and  idade > 0 else print("idade invalida")
        self.imprime_status= print(self.__str__()) if self._nome and self._idade else print("Ocorreu um erro. A entidade nao pode ser processada.")
        
    def valida_status_eleitor(self) -> str:
        if self._idade < 16:
            return 'Eleitor não tem direito a voto'
        elif self._idade<18 or self._idade>70 :
            return 'Eleitor facultativo'
        elif self._idade<=70:
            return 'Eleitor obrigatório'

    def __str__(self):
        return (f'nome:{self._nome}\nidade:{self._idade}\nstatus:{self.valida_status_eleitor()}')
    

try: 
    nome=input("digite o nome:")
    idade=int(input("digite a idade:"))
   
    pessoa = PessoaEleitor(nome,idade)
    pessoa.imprime_status
except(ValueError):
    print("Valor digitado nao pode ser processado")