import threading 
import time
import random
from termcolor import colored

#define uma classe Sapo
class Sapo(threading.Thread):
    vencedor = None  # Variável compartilhada para armazenar o vencedor
    cores_permitidas = ['blue', 'yellow', 'cyan', 'magenta', 'white']  # Lista de cores permitidas

    def __init__(self, ident):
        threading.Thread.__init__(self)
        self._ident = ident  # Use um atributo privado para armazenar o valor
        self.pulos = 0
        self.posicao = 0
        self.pulo = 0
        self.velocidade = random.uniform(0.1, 0.5)  # Define a velocidade como um número aleatório entre 0.1 e 0.5 segundos
        self.cor = Sapo.escolher_cor()  # Escolhe uma cor única da lista de cores permitidas

    @property
    def ident(self):
        return self._ident

    @ident.setter
    def ident(self, value):
        self._ident = value

    @staticmethod
    def escolher_cor():
        if Sapo.cores_permitidas:
            return Sapo.cores_permitidas.pop(random.randint(0, len(Sapo.cores_permitidas) - 1))
        else:
            return 'white'  # Cor padrão caso todas as cores tenham sido usadas

    def run(self):
        while self.posicao < 50:  # Altera a distância da corrida para 50 metros
            self.pulo = random.randint(1, 5)
            self.posicao += self.pulo
            self.pulos += 1
            print(colored("Sapo %d pulou %d metros e percorreu %d metros" % (self.ident, self.pulo, self.posicao), self.cor))
            time.sleep(self.velocidade)  # Dorme um tempo aleatório entre 0.1s e 0.5s para simular diferenças de velocidade
            if self.posicao >= 50 and Sapo.vencedor is None:
                Sapo.vencedor = self.ident
                print(colored("Sapo %d é o vencedor!" % self.ident, 'green'))

def corrida():
    sapos = [Sapo(i) for i in range(5)]
    for sapo in sapos:
        sapo.start()
    for sapo in sapos:
        sapo.join()

if __name__ == "__main__":
    corrida()


#link https://github.com/JoaoPalmasBR/spd-aula-4-corrida-sapo