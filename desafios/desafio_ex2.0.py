#desafio 06
#Exiba a seguinte mensagem: "O aluno xxx foi yyy no curso www com média zzz". Onde:
# xxx: nome do aluno; yyy: aprovado/reprovado; www: nome do curso; zzz: média
# A média deve ser calculada da seguinte forma:
# = ((nota da primeira prova 7 + nota do primeiro trabalho 3) + (nota da segunda prova 6 + nota do segundo trabalho 4))2
# Se a média do aluno for maior ou igual a 70, considere-o aprovado; caso contrário, reprovado.

class Aluno:
    def __init__(self, nome: str, curso: str, p1: int, t1:int , p2: int, t2: int):
        self.nome = nome
        self.curso = curso 
        self.media = (((p1*7)+(t1*3)) + ((p2*6) +(t2*4)))/2
        self.resultado = self.check_result()
        self.mensagem = self.__str__()
        
    def check_result(self):
        if self.media >= 70:
            return f"aprovado"
        return f"reprovado"
        
    def __str__(self):
       return f"O aluno {self.nome} foi {self.resultado} no curso {self.curso} com média {self.media}"