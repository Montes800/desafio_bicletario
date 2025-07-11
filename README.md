# Projeto Bicicleta - Exemplo de Classe em Python

Este projeto contém uma classe simples em Python que representa uma bicicleta com atributos e métodos básicos.

---

## Conceitos aprendidos

- **Classe e objetos**: A classe `Bicicleta` define a estrutura (atributos) e comportamentos (métodos) de uma bicicleta.
- **Construtor (`__init__`)**: Método especial que inicializa os atributos ao criar um objeto.
- **Atributos**: Informações que cada objeto carrega (cor, modelo, ano, valor).
- **Métodos**: Funções dentro da classe que descrevem comportamentos (buzinar, parar, correr).
- **`self`**: Referência ao próprio objeto, usada para acessar atributos e métodos.
- **Método especial `__str__`**: Define como o objeto será exibido quando usado com `print()`.

---

## Código da classe Bicicleta

```python
class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Plim plim..")

    def parar(self):
        print("Parando bicicleta")
        print("Bicicleta parada!")

    def correr(self):
        print("Vrummm....")

    def __str__(self):
        return f"{self.__class__.__name__}: cor={self.cor}, modelo={self.modelo}, ano={self.ano}, valor={self.valor}"
