
class Calculadora:
    def __init__(self, valor_1, valor_2):
        self.valor_1 = valor_1
        self.valor_2 = valor_2

    def somar(self):
        return self.valor_1 + self.valor_2
    
    def subtrair(self):
        return self.valor_1 - self.valor_2
    
    def multiplicar(self):
        return self.valor_1 * self.valor_2

    def dividir(self):
        if self.valor_2 == 0:
            raise ValueError("Não é possível dividir por zero.")
        return self.valor_1 / self.valor_2