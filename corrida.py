import threading 
import time
import random

#define uma classe Sapo
class Sapo(threading.Thread):
    def __init__(self, ident):
        threading.Thread.__init__(self)
        self.ident = ident
        self.pulos = 0
        self.posicao = 0
        self.pulo = 0
        self.velocidade = random.uniform(0.5, 2.0)  # Define a velocidade como um número aleatório entre 0.5 e 2.0 segundos

    def anda(self):
        while self.posicao < 100:
            self.pulo = random.randint(1, 5)
            self.posicao += self.pulo
            self.pulos += 1
            print("Sapo %d pulou %d cm e percorreu %d cm" % (self.ident, self.pulo, self.posicao))
            time.sleep(self.velocidade)  # Usa a velocidade para determinar o tempo de espera entre os pulos

def corrida():
    for i in range(10):