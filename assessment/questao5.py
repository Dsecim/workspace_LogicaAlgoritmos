
class ClassificaçãoPIB:
    
    path_arquivo="/Users/danielasecim/Documents/workspace_LogicaAlgoritmos/assessment/Assessment_PIBs.csv"
    xseries=None
    yseries=[]
    raw_data = []
    
    def __init__(self):
        self.le_arquivo = self.le_arquivo()
        self.valida_dados =  self.valida_dados()
        
    def le_arquivo(self):
        arquivo = open(self.path_arquivo, 'r')
        return arquivo.readlines()
        
    
    def transforma_dados(self):
        conteudo_arquivo=self.le_arquivo
        for item in conteudo_arquivo:
            item = item.replace("\n","")
            self.raw_data.append(item.split(","))
       
        self.xseries=self.raw_data[0]
        for item in self.raw_data:
            self.yseries.append(item.pop(0))
        self.yseries.pop(0)
        self.raw_data.pop(0)
        self.raw_data.pop()
    
    def find_x_pos_data(self,ano):
        i=0
        while ano!=self.xseries[i]:
            i+=1
        return i
    
    def find_y_pos_data(self, pais):
        i=0
        while pais!=self.yseries[i]:
            i+=1
        return i
    
    def valida_dados(self):
        #O programa solicita ao usuário o nome do país e o ano desejado.
        #Caso o país solicitado ou o ano não sejam válidos, o programa deve informar, na saída, a mensagem:
        self.transforma_dados()
        pais=input("Digite o país desejado:\t") 
        ano=input("Digite o ano desejado:\t")
        if pais in self.yseries and ano in self.xseries:
            print(f"PIB {pais} em {ano}: {self.raw_data[self.find_x_pos_data(ano)][self.find_y_pos_data(pais)]} trilhões.")
        else: 
            if pais  not in self.yseries:
                print(f"{pais} nao encontrado")
            else :
                print(f"{ano} nao encontrado")
        
    def analise_dados(path_arquivo):
        pass
    def monta_grafico(path_arquivo):
        pass


teste=ClassificaçãoPIB()
teste.valida_dados







