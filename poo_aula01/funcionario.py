class Funcionario:
    def __init__(self, nome, valor_hora, horas_trabalhadas):
        self.nome = nome
        self.valor_hora = valor_hora
        self.horas_trabalhadas = horas_trabalhadas

   
    def calcular_salario(self):
        return self.valor_hora * self.horas_trabalhadas
        
    def calcular_inss(self):
      
        salario = self.calcular_salario()

      
        if salario <= 2500:
            return salario * 0.09                
        return salario * 0.125
            
    def salario_liquido(self):
        salario = self.calcular_salario()
        inss = self.calcular_inss()
        return salario - inss
            
    def mostrar_holerite(self):
        salario = self.calcular_salario()
        inss = self.calcular_inss()
        liquido = self.salario_liquido()

        print("=" * 30)
        print(f"Funcionário: {self.nome}")
        print(f"Salário Bruto: R$ {salario:.2f}")
        print(f"INSS: R$ {inss:.2f}")
        print(f"Salário Líquido: R$ {liquido:.2f}")
        print("-" * 30)