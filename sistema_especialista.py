from pyknow import *

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


#classe machine
class vocacaoMachine(KnowledgeEngine):

    # variaveis

    # Emoção ( Humanas, Biológicas )

    gostaDeLer = {
        'action': False,
        'x': 0,
        'y': 0 
    }

    criativo = {
        'action': False,
        'x': 0,
        'y': 0 
    }

    escrever = {
        'action': False,
        'x': 0,
        'y': 0 
    }

    questionador = {
        'action': False,
        'x': 0,
        'y': 0 
    }

    # Exatas

    calculos = {
        'action': False,
        'x': 0,
        'y': 0 
    }

    praticar = {
        'action': False,
        'x': 0,
        'y': 0 
    }

    tecnologia = {
        'action': False,
        'x': 0,
        'y': 0 
    }

    racLogico = {
        'action': False,
        'x': 0,
        'y': 0 
    }

    #biologicas

    animal = {
        'action': False,
        'x': 0,
        'y': 0 
    }

    med_vec = {
        'action': False,
        'x': 0,
        'y': 0 
    }

    meio_ambiente = {
        'action': False,
        'x': 0,
        'y': 0 
    }

    pessoas = {
        'action': False,
        'x': 0,
        'y': 0 
    }
    
    # x == emoção
    # y == exatas

    @DefFacts()
    def _initial_action(self):

        #AQUI COMECA AS REGRAS DE HUMANAS

        #humanas

        #gosta de ler
        self.gostaDeLer['action'] = input("Gosta e tem o habito de fazer leitura? (s/n)")
        self.gostaDeLer['action'] = (False if self.gostaDeLer['action'] == 'n' else True)

        if(self.gostaDeLer['action']):
            self.gostaDeLer['x'] += 8
            self.gostaDeLer['y'] += 2

        #Criativo

        self.criativo['action'] = input("Voce se considera uma pessoa muito criativa? (s/n)")
        self.criativo['action'] = (False if self.criativo['action'] == 'n' else True)

        if(self.criativo['action']):
            self.criativo['x'] += 9
            self.criativo['y'] += 1

        
        #Escrever
        self.escrever['action'] = input("Voce gosta de escrever? (s/n)")
        self.escrever['action'] = (False if self.escrever['action'] == 'n' else True)

        if(self.escrever['action']):
            self.escrever['x'] += 6
            self.escrever['y'] += 4

        #questionador

        self.questionador['action'] = input("Voce se considera uma pessoa questionadora? (s/n)")
        self.questionador['action'] = (False if self.questionador['action'] == 'n' else True)

        if(self.questionador['action']):
            self.questionador['x'] += 4
            self.questionador['y'] += 6


        #AQUI COMECA AS REGRAS DE EXATAS

        #calculo(exatas)
        
        self.calculos['action'] = input("Gosta de calculos? (s/n)")
        self.calculos['action'] = (False if self.calculos['action'] == 'n' else True)

        if(self.calculos['action']):
            self.calculos['x'] += 1
            self.calculos['y'] += 9

        #pratica    
        
        self.praticar['action'] = input('gosta de fazer coisas na pratica? (s/n)')
        self.praticar['action'] = (False if self.praticar['action'] =='n' else True)

        if(self.praticar['action']):
            self.praticar['x'] += 3
            self.praticar['y'] += 7

        
        #Tecnologia

        self.tecnologia['action'] = input('Gosta de tecnologias? (s/n)')
        self.tecnologia['action'] = (False if self.tecnologia['action'] =='n' else True)

        if(self.tecnologia['action']):
            self.tecnologia['x'] += 3
            self.tecnologia['y'] += 7

        
        #raciocinio logio

        self.racLogico['action'] = input('Voce tem um bom raciocinio logico para resolver problemas? (s/n)')
        self.racLogico['action'] = (False if self.racLogico['action'] =='n' else True)

        if(self.racLogico['action']):
            self.racLogico['x'] += 0
            self.racLogico['y'] += 10

        
        #AQUI COMECA AS REGRAS DE BIOLOGICAS

        #animal

        self.animal['action'] = input('Voce gosta de aniamis? (s/n)')
        self.animal['action'] = (False if self.animal['action'] =='n' else True)

        if(self.animal['action']):
            self.animal['x'] += 7
            self.animal['y'] += 3

        #Medicina/veterinaria

        self.med_vec['action'] = input('Voce tem interesse pelas areas de medicina e veterinaria? (s/n)')
        self.med_vec['action'] = (False if self.med_vec['action'] =='n' else True)

        if(self.med_vec['action']):
            self.med_vec['x'] += 6
            self.med_vec['y'] += 4

        #meio ambiente

        self.meio_ambiente['action'] = input('Voce tem interesse pelas coisas relacionadas ao meio ambiente? (s/n)')
        self.meio_ambiente['action'] = (False if self.meio_ambiente['action'] =='n' else True)

        if(self.meio_ambiente['action']):
            self.meio_ambiente['x'] += 8
            self.meio_ambiente['y'] += 2

        #pessoas

        self.pessoas['action'] = input('Voce se importa e gosta de cuidar das pessoas nescessitadas? (s/n)')
        self.pessoas['action'] = (False if self.pessoas['action'] =='n' else True)

        if(self.pessoas['action']):
            self.pessoas['x'] += 7
            self.pessoas['y'] += 3

        #chamadas das classes de humanas
        yield GostaDeLer(self.gostaDeLer)
        yield Criativo(self.criativo)
        yield Escrever(self.escrever)
        yield Questionador(self.questionador)
    
        #chamadas das classes de exatas
        yield Calculos(self.calculos)
        yield Praticar(self.praticar)
        yield Tecnologia(self.tecnologia)
        yield RacLogico (self.racLogico)

        #chamadas das classes de biologicas
        yield Animal(self.animal)
        yield Med_vec(self.med_vec)
        yield Meio_ambiente(self.meio_ambiente)
        yield Pessoas(self.pessoas)


    # Regras encadeadas para exatas
    @Rule(
        AND(
            NOT(Calculos(calculos=W())),
            NOT(Praticar(praticar=W()))
        )
    )
    def ask_idade(self):
        print(self.calculos, self.praticar)
        
engine = vocacaoMachine()
engine.reset() 
engine.run() 