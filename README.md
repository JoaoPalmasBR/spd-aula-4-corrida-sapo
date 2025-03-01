# Corrida de Sapos

Este projeto simula uma corrida de sapos utilizando threads em Python. Cada sapo tem uma velocidade e cor únicas, e a corrida é exibida no terminal.

## Como executar

1. Certifique-se de ter o Python instalado em sua máquina.
2. Instale a biblioteca `termcolor` se ainda não a tiver:
   ```sh
   pip install termcolor
   ```
3. Execute o script `corrida.py`:
   ```sh
   python corrida.py
   ```

## Funcionamento

- Cada sapo é representado por uma instância da classe `Sapo`, que herda de `threading.Thread`.
- A corrida tem uma distância de 50 metros.
- Cada sapo pula uma distância aleatória entre 1 e 5 metros em intervalos de tempo aleatórios entre 0.1 e 0.5 segundos.
- A cor de cada sapo é escolhida aleatoriamente de uma lista de cores permitidas.
- O primeiro sapo a alcançar ou ultrapassar a distância de 50 metros é declarado vencedor.

## Exemplo de Saída

```sh
Sapo 0 pulou 3 metros e percorreu 3 metros
Sapo 1 pulou 2 metros e percorreu 2 metros
Sapo 2 pulou 4 metros e percorreu 4 metros
Sapo 3 pulou 1 metros e percorreu 1 metros
Sapo 4 pulou 5 metros e percorreu 5 metros
...
Sapo 4 é o vencedor!

Este `README.md` fornece uma visão geral do projeto, instruções sobre como executá-lo, uma explicação do funcionamento e um exemplo de saída.
Este `README.md` fornece uma visão geral do projeto, instruções sobre como executá-lo, uma explicação do funcionamento e um exemplo de saída.
```
