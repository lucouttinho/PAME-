

class Faixas:
    def __init__(self, cor):
        self.cor = cor

class Arte:
    def __init__(self, marcial):
        self.marcial = marcial

class Lutador:
    def __init__(self, nome, idade, peso, força, faixa, arteMarcial):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.força = força
    def __str__(self):
        return f'Nome: {self.nome}, idade: {self.idade}, peso: {self.peso}, força: {self.força}, faixa: {self.faixa}, Arte Marcial: {self.arteMarcial}'
        
class Torneio:
    def __init__(self, nome, arteMarcial, faixa, peso):
        self.nome = nome
        self.arteMarcial = arteMarcial
        self.faixa = faixa
        self.peso = peso
      
        
        
    
def linha (tam=80):
    return '-' * tam

def Texto (txt):
    print(linha())
    print(txt.center(80))
    print(linha())


def menu (lista):
    Texto(' Escolha uma das opções abaixo e pressione a tecla ENTER')
    c=1
    for item in lista:
            print (f'{c} - {item}')
            c+=1
    print (linha())
    

def menuTorneio ():
    Texto(' Escolha uma das opções abaixo e pressione a tecla ENTER')
    print ("""
    1 - Criar Torneio
    2 - Inscrever Lutador
    3 - Ver torneiros existentes
    4 - Ver Ranking de Torneios
    5 - Ver Lutadores inscritos em torneios
    6 - Realizar Luta
    7 - voltar
    """)
    print (linha())
    

def menuLutador ():
    Texto(' Escolha uma das opções abaixo e pressione a tecla ENTER')
    print ("""
    1 - Cadastrar Lutador
    2 - Ver Lutadores
    3 - Ver Detalhes do Lutador
    4 - voltar
    """)
    print (linha())
    
    

    print (linha())


Texto ('STREET FIGHTER II')
menu (['Torneio', 'Lutador', 'Torneio Aleatório'])
Z=[]
Y=[]
x = int(input('Opção desejada: '))

if x==1:
    while x==1:
     menuTorneio()
     x=int(input('Opção desejada: '))
     if x==1:
        A = Torneio(nome = input('nome:'), arteMarcial = input('Arte Marcial: '), faixa =input('faixa:'), peso =input('peso: '))
        Y.append(A)
     
elif x==2:
    while x==2:
     menuLutador()
     b = int(input('Opção desejada:'))
     a=Lutador(nome = input('nome:'), idade = input('idade:'), peso =input('peso: ') , força =input('força: ') , faixa =input('faixa:') , arteMarcial = input('Arte Marcial: ')) 
     Z.append(a)
     
          
elif x==3:
     for n in Z:
         print (n)
elif x==4:
    menu (['Torneio', 'Lutador', 'Torneio Aleatório'])
    
else:
     print ('digite uma opção válida')


     
#def Poder_de_luta (força, idade, faixa):
  #  return força * 1.3 + idade/1.3 + faixa *1.5




























#def Valid(msg):
#    while True:
#        try:
#            n = int(input(msg))
#        except (ValueError, TypeError):
 #           print('ERRO.. Insira uma opção válida')
 #           continue
    














#while True:
 #   resposta = menu (['Torneio', 'Lutador', 'Criar torneio aleatório'])
  #  if resposta ==1:
   #     print('opção 1')
    #elif resposta ==2:
     #   print('opção 2')
    #elif resposta ==3:
     #   print('opção 3')
    #else:
     #   print ('ERRO.. insira uma opção válida)
        
    
    

#Valid ('Digite uma opção:') 

