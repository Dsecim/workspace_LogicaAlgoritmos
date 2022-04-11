'''Crie um programa contendo uma função que, dados um valor de renda mensal total, gastos totais com moradia, gastos totais com educação e gastos totais com transporte, faça um diagnóstico da saúde financeira do usuário, com base nos valores percentuais acima expostos, informando qual é o percentual da renda mensal total comprometido por cada custo. '''

class ControleFinanceiro:
    moradia_max= 30
    educacao_max= 20
    transporte_max = 15
    lista_percentual_gastos={
        "moradia": 0.0,
        "educacao":0.0,
        "transporte":0.0
    }
    
    def __init__(self, salario_mensal: float, despesas: dict):
        self._salario_mensal= salario_mensal if isinstance(salario_mensal,float) and salario_mensal>0.0 else print("Salario informado invalido")
        self._moradia=  despesas["moradia"] 
        self._educacao= despesas["educacao"]
        self._transporte= despesas["transporte"]
        self.analise= self.analise()
        
    def calcula_percentual_gastos(self):
        self.lista_percentual_gastos["moradia"]=round((self._moradia/self._salario_mensal)*100,2)
        self.lista_percentual_gastos["educacao"]=round((self._educacao/self._salario_mensal)*100,2)
        self.lista_percentual_gastos["transporte"]=round((self._transporte/self._salario_mensal)*100,2)
        return self.lista_percentual_gastos
    
    def analise(self):
        self.calcula_percentual_gastos()
        if self.lista_percentual_gastos["moradia"] > self.moradia_max:
            print(f"Seus gastos totais com moradia comprometem {self.lista_percentual_gastos['moradia']}% de sua renda total. O máximo recomendado é de {self.moradia_max}%.\n Portanto, idealmente, o máximo de sua renda comprometida com moradia deveria ser de R$ {round((self._salario_mensal*(self.moradia_max/100)),2)}.")
        else:    
            print(f"Seus gastos totais com educação comprometem {self.lista_percentual_gastos['moradia']}% de sua renda total. O máximo recomendado é de {self.moradia_max}%. Seus gastos estão dentro da margem recomendada.")
        if self.lista_percentual_gastos["educacao"] > self.educacao_max:
            print(f"Seus gastos totais com educação comprometem {self.lista_percentual_gastos['educacao']}% de sua renda total. O máximo recomendado é de {self.educacao_max}%.\n Portanto, idealmente, o máximo de sua renda comprometida com moradia deveria ser de R$ {round(self._salario_mensal*(self.educacao_max/100),2)}.")
        else:
            print(f"Seus gastos totais com educação comprometem {self.lista_percentual_gastos['educacao']}% de sua renda total. O máximo recomendado é de {self.educacao_max}%. Seus gastos estão dentro da margem recomendada.")
        if self.lista_percentual_gastos["transporte"] > self.transporte_max:
            print(f"Seus gastos totais com educação comprometem {self.lista_percentual_gastos['transporte']}% de sua renda total. O máximo recomendado é de {self.transporte_max}%.\n Portanto, idealmente, o máximo de sua renda comprometida com moradia deveria ser de R$ {round(self._salario_mensal*(self.transporte_max/100),2)}.")
        else:
            print(f"Seus gastos totais com educação comprometem {self.lista_percentual_gastos['transporte']}% de sua renda total. O máximo recomendado é de {self.transporte_max}%. Seus gastos estão dentro da margem recomendada.")
           
        
try:
    sal_mensal= float(input("Digite sua renda liquida mensal:\t"))
    desp_moradia=float(input("Digite seu gasto mensal com moradia:\t"))
    desp_educacao=float(input("Digite seu gasto mensal com educação:\t"))
    desp_transporte=float(input("Digite seu gasto mensal com transporte:\t"))
    despesas={
        "moradia": desp_moradia,
        "educacao": desp_educacao,
        "transporte": desp_transporte
    }
    controle_financeiro= ControleFinanceiro(sal_mensal, despesas)
    controle_financeiro.analise
except(ValueError):
    print("Dado de entrada nao pode ser processado")
    