#Escreva um algoritmo que armazene o valor 10 em uma variável A e o valor 20
# em uma variável B.
from __future__ import annotations
from datetime import datetime


varA = 10
varB = 20


#A seguir troque os seus 
#conteúdos fazendo com que o valor que está em A passe para B e vice-versa.
aux = varB
varB = varA
varA = aux

# Ao final, escrever 
# os valores que ficaram armazenados nas variáveis.

print(f'valores de A: {varA} e valores de B: {varB}')


# Escreva um algoritmo para ler as dimensões de um triângulo 
# (base e altura), calcular e escrever a área do triângulo.

b = input("inserir base: ") 
a = input("inserir altura: ") 

# Sabendo que para calcular a área devemos usar 
# a fórmula a seguir: =(base * altura) / 2

area = round((b*a)/2,2)

print(f'area: {area}')

# Faça um algoritmo que leia a idade de uma pessoa expressa em anos,
# meses e dias e escreva a idade dessa pessoa expressa apenas em dias.


idade = input("idade:")
idade_dias= idade*(365*30)

print(f'idade em dias: {idade_dias}')

# eceba o nome, o sobrenome, a idade, o salário e o desconto do funcionário.
# Exiba a seguinte frase: "O funcionário aaa bbb nasceu em ccc e ganha R$ddd". Onde:
# aaa é o nome do funcionário e bbb é o sobrenome;
# ccc é o ano de nascimento do funcionário;
# ddd é o salário líquido = salário - desconto.


class Funcionario:
    # nome = 'daniela secim'
    # nome = nome.split(" ") -> ["daniela","secim"]
    def __init__(self, nome: list[str], ano: int, salario: int, desconto: int ):
        self.aaa= nome[0]  
        self.bbb= nome[1]
        self.ccc = ano
        self.sss = salario
        self.kkk = desconto
        self.ddd = self.desconto()
        
        return self.sss - self.kkk
    
    def __str__(self):
        return f'O funcionário {self.aaa} {self.bbb} nasceu em {self.ccc} e ganha R${self.ddd}'
    
    
# Receba o nome do time, a quantidade de vitórias, a quantidade de empates.
# Exiba o seguinte relatório:
# "O time xxx está com yyy pontos". Onde:
# xxx é o nome do time;
# yyy é a quantidade de pontos;
# A pontuação deve ser calculada da seguinte maneira: quantidade de vitórias * 3 pontos + quantidade de empates


class Time:
    
    def __init__(self, nome: str, vitorias: int, empates: int, desconto: int ):
        self.xxx= nome  
        self.vvv = vitorias
        self.eee = empates
        self.yyy = self.pontuacao()
        
    def pontuacao(self) -> int :
        return  (self.vvv * 3) + self.eee
        
    def escreve_ex1(self) -> str:
        return f'O time {self.xxx} está com {self.yyy} pontos'
    
        