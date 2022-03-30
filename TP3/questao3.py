

class Participante:
    def __init__(self,nome: str, nota: int):
        self._nome = nome if isinstance(nome, str) and nome!="" else print("Nome invalido")
        self._nota =  nota if isinstance(nota,float) and  nota > -1 and nota<11 else print("idade invalida")
        self.participante = {"nome": self._nome, "nota": self._nota}
        
    def get_nome(self):
        return self._nome
    
    def get_nota(self):
        return self._nota
    
    def get_participante(self):
        return self.participante

class Concurso:
    
    lista=[]
    
    def __init__(self, participante: Participante):
        self.adciona_participante=self.lista.append(participante.participante) 
        self.resultado= self.ordena_participantes()
        
    def ordena_participantes(self):
        for final in range(len(self.lista), 0, -1):
            for current in range(0, final - 1):
                if self.lista[current]['nota'] < self.lista[current + 1]['nota']:
                    self.lista[current + 1], self.lista[current] = self.lista[current], self.lista[current + 1]
        return self.lista        

    
    
            
try:
    num_participantes = int(input("digite o numero de participantes:"))
    participantes=[]
    for i in range(num_participantes):
        nome=input("digite o nome:")
        nota=float(input("digite a nota:"))
        concurso = Concurso(Participante(nome, nota))
    concurso.resultado
    for current in range(len(concurso.lista)):
        print(f"Informe nome do {current+1} participante: {concurso.lista[current]['nome']}\nnforme nota do {current+1} participante: {concurso.lista[current]['nota']}")
except(ValueError):
    print("Valor digitado nao pode ser processado")

