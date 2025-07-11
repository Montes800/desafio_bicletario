class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):#construtor ou metodo
        self.cor = cor
        self.modelo = modelo #atributos da class
        self.ano = ano 
        self.valor = valor 
#self referencia para o obejto. convenção do python e usar self ppara  ainstancia do obejeto 

    def buzinar(self): #metdos da class 
        print("Plim plim..")

    def parar(self):
        print("Parando bicileta")
        print("Bicleta parada!")
    
    def correr(self):
        print("Vrummm....")

    #def get_cor(self):
        #return self.cor
    
    #def __str__(self):
        #return f"Bicicleta: cor={self.cor}, modelo={self.modelo}, ano={self.ano}, valor={self.valor}"


    def __str__(self):
        return f"{self.__class__.__name__}: {[{chave}={valor} for chave, valor in self._dict_]}"



b1 = Bicicleta("vermelha", "caloi", 2023, 600)
b1.buzinar()
b1.correr()
b1.parar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta("verde", "monark", 2000, 189)
Bicicleta.buzinar(b2)
