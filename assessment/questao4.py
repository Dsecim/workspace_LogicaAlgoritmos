'''Valor inicial: R$ 10000
Rendimento por período (%): 0.54
Aporte a cada período: R$ 1000
Total de períodos: 120 

Após 1 períodos(s), o montante será de R$11054.00.
Após 2 períodos(s), o montante será de R$12113.69.
Após 3 períodos(s), o montante será de R$13179.11.
Após 4 períodos(s), o montante será de R$14250.27.
Após 5 períodos(s), o montante será de R$15327.22.'''

class CalculadoraRendimento:
    plano_investimento={
        "montante": 0.0,
        "periodo": 0
    }
    
    
    def __init__(self, despesas: dict):
        self._montante_inicial= despesas["montante_inicial"] if isinstance(despesas["montante_inicial"],float) and despesas["montante_inicial"]>0.0 else print("Montante inicial invalido")
        self._perc_rendimento=  despesas["perc_rendimento"] if isinstance(despesas["perc_rendimento"],float) and despesas["perc_rendimento"]>0.0 else print("Percentual de rendimento invalido")
        self._aporte_mensal= despesas["aporte_mensal"] if isinstance(despesas["aporte_mensal"],float) and despesas["aporte_mensal"]>0.0 else print("Aporte mensal invalido")
        self._periodo= despesas["periodo"] if isinstance(despesas["periodo"],int) and despesas["periodo"]>0 else print("Periodo invalido")
        self.analise= self.calcula_rendimento()
        
    def calcula_rendimento(self):
        
        periodos=(periodo//30)+1
        self.plano_investimento["montante"]=round(self._montante_inicial+(self._montante_inicial*(self._perc_rendimento/100)) +self._aporte_mensal,2)
        self.plano_investimento["periodo"]=1
        print(f"Após {self.plano_investimento['periodo']} períodos(s), o montante será de R${self.plano_investimento['montante']}.")
        for i in range(1,periodos):
            self.plano_investimento["montante"]=round(self.plano_investimento["montante"]+(self.plano_investimento["montante"]*(self._perc_rendimento/100))+self._aporte_mensal,2)
            self.plano_investimento["periodo"]=self.plano_investimento["periodo"]+1
            print(f"Após {self.plano_investimento['periodo']} períodos(s), o montante será de R${self.plano_investimento['montante']}.")

    
       
try:
    montante_inicial= float(input("Valor inicial:\t"))
    perc_rendimento=float(input("Rendimento por período (%):\t"))
    aporte_mensal=float(input("Aporte a cada período:\t"))
    periodo=int(input("Total de períodos:\t"))
    investimento={
        "montante_inicial": montante_inicial,
        "perc_rendimento": perc_rendimento,
        "aporte_mensal": aporte_mensal,
        "periodo": periodo
    }
    rendimento= CalculadoraRendimento(investimento)
    rendimento.analise
except(ValueError):
    print("Dado de entrada nao pode ser processado")
    