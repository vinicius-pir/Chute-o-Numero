import random

class ChuteONumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.tentativas = 0
        self.tentar_novamente = True

    def Iniciar(self):       
        self.GerarNumeroAleatorio()
        self.PedirValorAleatorio()
       
        while self.tentar_novamente == True:
            if (self.valor_do_chute > self.valor_aleatorio):
                print('Chute mais Baixo!!')
                self.PedirValorAleatorio()
            elif (self.valor_do_chute < self.valor_aleatorio):
                print('Chute mais Alto!!')
                self.PedirValorAleatorio()
            elif (self.valor_do_chute == self.valor_aleatorio):
                print(f'PARABÉNS!!! Você acertou em {self.tentativas} !!!',
                f'\nO Valor correto era = {self.valor_aleatorio}')
                self.PedirParaJogarNovamente()

    def PedirParaJogarNovamente(self):
        resposta = input('Deseja Jogar Novamente? ')
        try:
            if resposta == 'sim' or resposta == 's':
                self.tentativas = 0
                chute.Iniciar()
            elif resposta == 'nao' or resposta == 'n' or resposta == 'não':
                print('Obrigado Pela Participação!')
                self.tentar_novamente = False
            else:
                print('Responda sim ou não')
        except:
            print('Resposta Inválida!!')

    def PedirValorAleatorio(self):
        self.valor_do_chute = input("Chute um Número: ")
        self.tentativas = self.tentativas + 1
        try:
            self.valor_do_chute = int(self.valor_do_chute)
        except:
            print('Digite Somente Números')
            self.tentativas = self.tentativas - 1
            self.PedirValorAleatorio()

    def GerarNumeroAleatorio(self):
        self.valor_aleatorio = random.randint(self.valor_minimo,self.valor_maximo)

chute = ChuteONumero()
chute.Iniciar()