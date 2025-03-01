import threading 
import time
import random

#define uma classe Sapo
class Sapo(threading.Thread):
    vencedor = None  # Variável compartilhada para armazenar o vencedor

    def __init__(self, ident):
        threading.Thread.__init__(self)
        self.ident = ident
        self.pulos = 0
        self.posicao = 0
        self.pulo = 0

    def run(self):
        while self.posicao < 50:  # Altera a distância da corrida para 50 metros
            self.pulo = random.randint(1, 5)
            self.posicao += self.pulo
            self.pulos += 1
            print("Sapo %d pulou %d metros e percorreu %d metros" % (self.ident, self.pulo, self.posicao))
            time.sleep(random.uniform(0.1, 0.5))  # Dorme um tempo aleatório entre 0.1s e 0.5s para simular diferenças de velocidade
            if self.posicao >= 50 and Sapo.vencedor is None:
                Sapo.vencedor = self.ident
                print("Sapo %d é o vencedor!" % self.ident)

def corrida():
    sapos = [Sapo(i) for i in range(10)]
    for sapo in sapos:
        sapo.start()
    for sapo in sapos:
        sapo.join()

if __name__ == "__main__":
    corrida()