class Towel:
    def __init__(self, cor: str, tamanho: str, moiado: int):
        self.cor = cor
        self.tamanho = tamanho
        self.moiado = 0

    def show(self) -> None:
        print(self)
    
    def __str__(self):
        return f"Cor: {self.cor}, Tamanho: {self.tamanho}, Umidade: {self.moiado}"
    
    def dry(self, amount: int):
        self.moiado += amount
        if self.moiado >= self.getMaxWetness():
            print("toalha encharcada")
            self.moiado = self.getMaxWetness()

    def getMaxWetness(self):
        if self.tamanho == "P":
            return 10
        if self.tamanho == "M":
            return 20
        if self.tamanho == "G":
            return 30
        
    def wringOut(self):
        self.moiado = 0

    def isDry(self):
        if self.moiado == 0:
            return True
        else:
            return False

    

def main():
    toalha = Towel("", "", 0)
     
    while True: 
        linha: str = input()
        print("$" + linha)
        arg: list[str] = linha.split(" ")

        if arg[0] == "end":
            break
        elif arg[0] == "criar":
            cor = arg[1]
            tamanho = arg[2]
            toalha = Towel(cor, tamanho, 0)
        elif arg[0] ==  "mostrar":
            print(toalha)
        elif arg[0] == "enxugar":
            amount = int(arg[1])
            toalha.dry(amount)
        elif arg[0] == "torcer":
            toalha.wringOut()
        elif arg[0] == "seca":
            if toalha.isDry():
                print("sim")
            else:
                print("nao")
    




main()

