from pyknow import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Vocacao(Fact):
    pass

#classes de humanas
class GostaDeLer(Fact):
    pass

class Criativo(Fact):
    pass

class Escrever(Fact):
    pass

class Questionador(Fact):
    pass


#classes de calculos

class Calculos(Fact):
    pass

class Praticar(Fact):
    pass

class Tecnologia(Fact):
    pass

class RacLogico(Fact):
    pass


#classes de biologicas

class Animal(Fact):
    pass

class Med_vec(Fact):
    pass

class Meio_ambiente(Fact):
    pass

class Pessoas (Fact):
    pass

class Dados(Fact):
    pass


#classe machine
class vocacaoMachine(KnowledgeEngine):

    # variaveis

    # Emoção ( Humanas, Biológicas )

    dados = {
        'action': False,
        'x': 0,
        'y': 0 
    }
    
    @DefFacts()
    def _initial_action(self):

        #AQUI COMECA AS REGRAS DE HUMANAS

        #humanas

        #gosta de ler
        self.dados['action'] = input("Gosta e tem o habito de fazer leitura? (s/n)")
        self.dados['action'] = (False if self.dados['action'] == 'n' else True)

        if(self.dados['action']):
            self.dados['x'] += 8
            self.dados['y'] += 2

        #Criativo

        self.dados['action'] = input("Voce se considera uma pessoa muito criativa? (s/n)")
        self.dados['action'] = (False if self.dados['action'] == 'n' else True)

        if(self.dados['action']):
            self.dados['x'] += 9
            self.dados['y'] += 1

        
        #Escrever
        self.dados['action'] = input("Voce gosta de escrever? (s/n)")
        self.dados['action'] = (False if self.dados['action'] == 'n' else True)

        if(self.dados['action']):
            self.dados['x'] += 6
            self.dados['y'] += 4

        #questionador

        self.dados['action'] = input("Voce se considera uma pessoa questionadora? (s/n)")
        self.dados['action'] = (False if self.dados['action'] == 'n' else True)

        if(self.dados['action']):
            self.dados['x'] += 4
            self.dados['y'] += 6


        #AQUI COMECA AS REGRAS DE EXATAS

        #calculo(exatas)
        
        self.dados['action'] = input("Gosta de calculos? (s/n)")
        self.dados['action'] = (False if self.dados['action'] == 'n' else True)

        if(self.dados['action']):
            self.dados['x'] += 1
            self.dados['y'] += 9

        #pratica    
        
        self.dados['action'] = input('gosta de fazer coisas na pratica? (s/n)')
        self.dados['action'] = (False if self.dados['action'] =='n' else True)

        if(self.dados['action']):
            self.dados['x'] += 3
            self.dados['y'] += 7

        
        #Tecnologia

        self.dados['action'] = input('Gosta de tecnologias? (s/n)')
        self.dados['action'] = (False if self.dados['action'] =='n' else True)

        if(self.dados['action']):
            self.dados['x'] += 3
            self.dados['y'] += 7

        
        #raciocinio logio

        self.dados['action'] = input('Voce tem um bom raciocinio logico para resolver problemas? (s/n)')
        self.dados['action'] = (False if self.dados['action'] =='n' else True)

        if(self.dados['action']):
            self.dados['x'] += 0
            self.dados['y'] += 10

        
        #AQUI COMECA AS REGRAS DE BIOLOGICAS

        #animal

        self.dados['action'] = input('Voce gosta de aniamis? (s/n)')
        self.dados['action'] = (False if self.dados['action'] =='n' else True)

        if(self.dados['action']):
            self.dados['x'] += 7
            self.dados['y'] += 3

        #Medicina/veterinaria

        self.dados['action'] = input('Voce tem interesse pelas areas de medicina e veterinaria? (s/n)')
        self.dados['action'] = (False if self.dados['action'] =='n' else True)

        if(self.dados['action']):
            self.dados['x'] += 6
            self.dados['y'] += 4

        #meio ambiente

        self.dados['action'] = input('Voce tem interesse pelas coisas relacionadas ao meio ambiente? (s/n)')
        self.dados['action'] = (False if self.dados['action'] =='n' else True)

        if(self.dados['action']):
            self.dados['x'] += 8
            self.dados['y'] += 2

        #pessoas

        self.dados['action'] = input('Voce se importa e gosta de cuidar das pessoas nescessitadas? (s/n)')
        self.dados['action'] = (False if self.dados['action'] =='n' else True)

        if(self.dados['action']):
            self.dados['x'] += 7
            self.dados['y'] += 3

        #chamadas das classes de humanas
        yield Dados(self.dados)


    # Regras encadeadas para exatas
    @Rule(
        AND(
            NOT(Dados(calculos=W()))
        )
    )
    def main(self):
                
        print(self.dados)

        plt.xlabel('Lógico')
        plt.ylabel('Emocional')
        plt.title('Sistema Vocacional')
        # inverti x e y
        plt.plot([self.dados['y']], [self.dados['x']], 'ro')
        plt.axis([0,100,0,100])
        plt.show()

        
engine = vocacaoMachine()
engine.reset() 
engine.run() 