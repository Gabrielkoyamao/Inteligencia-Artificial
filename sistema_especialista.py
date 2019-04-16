from pyknow import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Vocacao(Fact):
    ''' 
        Este é um protótipo de um sistema vocaicional
    '''

    pass

class Dados(Fact):
    pass

class Livros(Fact):
    pass

class vocacaoMachine(KnowledgeEngine):

    # variaveis

    dados = {
        'action': False,
        'x': 0,
        'y': 0 
    }
    
    @DefFacts()
    def _initial_action(self):

        # AQUI COMECA AS REGRAS DE HUMANAS
        # def humanas(self):

        #gosta de ler
        self.dados['action'] = input("Gosta e tem o habito de fazer leitura? (s/n)")
        self.dados['action'] = (False if self.dados['action'] == 'n' else True)

        if(self.dados['action']):
            self.dados['x'] += 2
            self.dados['y'] += 1
            yield Livros(fato=True)

        else:
            self.dados['x'] += 6
            self.dados['y'] += 2
            yield Livros(fato=False)

        
        # Criativo

        self.dados['action'] = input("Voce se considera uma pessoa muito criativa? (s/n)")
        self.dados['action'] = (False if self.dados['action'] == 'n' else True)

        if(self.dados['action']):
            self.dados['x'] += 3
            self.dados['y'] += 2
        else:
            self.dados['x'] += 7
            self.dados['y'] += 3

        
        #Escrever
        self.dados['action'] = input("Voce gosta de escrever? (s/n)")
        self.dados['action'] = (False if self.dados['action'] == 'n' else True)

        if(self.dados['action']):
            self.dados['x'] += 3
            self.dados['y'] += 3
        else:
            self.dados['x'] += 8
            self.dados['y'] += 4

        #questionador

        self.dados['action'] = input("Voce se considera uma pessoa questionadora? (s/n)")
        self.dados['action'] = (False if self.dados['action'] == 'n' else True)

        if(self.dados['action']):
            self.dados['x'] += 3
            self.dados['y'] += 3
        else:
            self.dados['x'] += 7
            self.dados['y'] += 3

        # AQUI COMECA AS REGRAS DE EXATAS

        # def exatas(self):
        
            #calculo(exatas)
            
        self.dados['action'] = input("Gosta de calculos? (s/n)")
        self.dados['action'] = (False if self.dados['action'] == 'n' else True)

        if(self.dados['action']):
            self.dados['x'] += 9
            self.dados['y'] += 1
        else:
            self.dados['x'] += 1
            self.dados['y'] += 1

        #pratica    
        
        self.dados['action'] = input('gosta de fazer coisas na pratica? (s/n)')
        self.dados['action'] = (False if self.dados['action'] =='n' else True)

        if(self.dados['action']):
            self.dados['x'] += 7
            self.dados['y'] += 3
        else:
            self.dados['x'] += 3
            self.dados['y'] += 2

        
        #Tecnologia

        self.dados['action'] = input('Gosta de tecnologias? (s/n)')
        self.dados['action'] = (False if self.dados['action'] =='n' else True)

        if(self.dados['action']):
            self.dados['x'] += 7
            self.dados['y'] += 3
        else:
            self.dados['x'] += 3
            self.dados['y'] += 2

        
        #raciocinio logio

        self.dados['action'] = input('Voce tem um bom raciocinio logico para resolver problemas? (s/n)')
        self.dados['action'] = (False if self.dados['action'] =='n' else True)

        if(self.dados['action']):
            self.dados['x'] += 10
            self.dados['y'] += 0
        else:
            self.dados['x'] += 0
            self.dados['y'] += 2

        # AQUI COMECA AS REGRAS DE BIOLOGICAS

        # def biologicas(self):
            #animal

        self.dados['action'] = input('Você gosta de aniamais? (s/n)')
        self.dados['action'] = (False if self.dados['action'] =='n' else True)

        if(self.dados['action']):
            self.dados['x'] += 3
            self.dados['y'] += 7
        else:
            self.dados['x'] += 3
            self.dados['y'] += 3

        #Medicina/veterinaria

        self.dados['action'] = input('Voce tem interesse pelas areas de medicina e veterinaria? (s/n)')
        self.dados['action'] = (False if self.dados['action'] =='n' else True)

        if(self.dados['action']):
            self.dados['x'] += 3
            self.dados['y'] += 7
        else:
            self.dados['x'] += 3
            self.dados['y'] += 3

        #meio ambiente

        self.dados['action'] = input('Voce tem interesse pelas coisas relacionadas ao meio ambiente? (s/n)')
        self.dados['action'] = (False if self.dados['action'] =='n' else True)

        if(self.dados['action']):
            self.dados['x'] += 2
            self.dados['y'] += 8
        else:
            self.dados['x'] += 3
            self.dados['y'] += 3

        #pessoas

        self.dados['action'] = input('Voce se importa e gosta de cuidar das pessoas nescessitadas? (s/n)')
        self.dados['action'] = (False if self.dados['action'] =='n' else True)

        if(self.dados['action']):
            self.dados['x'] += 3
            self.dados['y'] += 7
        else:
            self.dados['x'] += 3
            self.dados['y'] += 3

        yield Dados(self.dados)



    # tipos de livros 
    @Rule(
        AND (
            Livros(fato=True),
            NOT(Dados(dados=W()))
        )
    )
    def ask_type(self):
        
        self.declare(Livros(fato=False))
        tipos_livros = input( "Que tipo de livro você geralmente leria (1-vida, 2-Cientificos/Tenclogia, 3-Meio Ambiente)" )

        # Humanas
        if(tipos_livros == "1" ):  
            self.dados['x'] += 3
            self.dados['y'] += 1
            self.declare(Dados(self.dados))
        # Exatas
        elif(tipos_livros == "2"):
            self.dados['x'] += 7
            self.dados['y'] += 1
            self.declare(Dados(self.dados))
        # Biologicas
        elif(tipos_livros == "3"):
            self.dados['x'] += 0
            self.dados['y'] += 10
            self.declare(Dados(self.dados))
        else:
            print('invalid answear')


    @Rule(
        AND(
            NOT(Dados(dados=W())),
            Livros(fato=False)
        )
    )
    def main(self):

        print(self.dados)
        plt.xlabel('Lógico')
        plt.ylabel('Emocional')
        plt.title('Sistema Vocacional')
        plt.plot([self.dados['x']], [self.dados['y']], 'ro')
        plt.axis([0,100,0,100])
        plt.show()

engine = vocacaoMachine()
engine.reset() 
engine.run() 




# SE gosta de ler
# ENTÃO x = 2 e y = 1
# SENÃO x = 6 e y = 2

# SE sou criativo
# ENTÃO x = 3 e y = 2
# SENÃO x = 7 e y = 3


# SE gosto de escrever
# ENTÃO x = 3 e y = 3
# SENÃO x = 8 e y = 4


# SE sou questionador
# ENTÃO x = 3 e y = 3
# SENÃO x = 7 e y = 3


# SE gosto de cálculo
# ENTÃO x = 9 e y = 1
# SENÃO x = 1 e y = 1

# SE sou prático
# ENTÃO x = 7 e y = 3
# SENÃO x = 3 e y = 2

# SE gosto de Tecnologia
# ENTÃO x = 7 e y = 3
# SENÃO x = 3 e y = 2

# SE tenho raciocineo logico
# ENTÃO x = 10 e y = 0
# SENÃO x = 0 e y = 2

# SE gosto de animais
# ENTÃO x = 3 e y = 7
# SENÃO x = 3 e y = 3

# SE gosto de veterinario ou medicina
# ENTÃO x = 3 e y = 7
# SENÃO x = 3 e y = 3

# SE gosto do meio ambiente
# ENTÃO x = 2 e y = 8
# SENÃO x = 3 e y = 3

# SE me preocupo com as pessoas
# ENTÃO x = 3 e y = 7
# SENÃO x = 3 e y = 3