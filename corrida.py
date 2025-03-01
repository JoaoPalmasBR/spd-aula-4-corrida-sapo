import threading 
import time
import random
from termcolor import colored
from tqdm import tqdm

#define uma classe Sapo
class Sapo(threading.Thread):
    vencedor = None  # Variável compartilhada para armazenar o vencedor
    cores_permitidas = ['blue', 'yellow', 'cyan', 'magenta', 'white']  # Lista de cores permitidas

    def __init__(self, ident, progress_bar):
        threading.Thread.__init__(self)
        self._ident = ident  # Use um atributo privado para armazenar o valor
        self.pulos = 0
        self.posicao = 0
        self.pulo = 0
        self.velocidade = random.uniform(0.1, 0.5)  # Define a velocidade como um número aleatório entre 0.1 e 0.5 segundos
        self.cor = Sapo.escolher_cor()  # Escolhe uma cor única da lista de cores permitidas
        self.progress_bar = progress_bar  # Referência à barra de progresso do tqdm

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
            self.progress_bar.update(self.pulo)  # Atualiza a barra de progresso
            print(colored("Sapo %d pulou %d metros e percorreu %d metros" % (self.ident, self.pulo, self.posicao), self.cor))
            time.sleep(self.velocidade)  # Dorme um tempo aleatório entre 0.1s e 0.5s para simular diferenças de velocidade
            if self.posicao >= 50 and Sapo.vencedor is None:
                Sapo.vencedor = self.ident
                print(colored("Sapo %d é o vencedor!" % self.ident, 'green'))

def corrida():
    sapos = []
    progress_bars = []
    for i in range(5):
        progress_bar = tqdm(total=50, desc=f'Sapo {i}', position=i, leave=True, bar_format='{desc}: {bar} {n_fmt}/{total_fmt}')
        sapo = Sapo(i, progress_bar)
        sapos.append(sapo)
        progress_bars.append(progress_bar)

    for sapo in sapos:
        sapo.start()
    for sapo in sapos:
        sapo.join()

    for progress_bar in progress_bars:
        progress_bar.close()

if __name__ == "__main__":
    corrida()