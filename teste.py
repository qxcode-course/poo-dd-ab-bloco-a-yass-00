class Towel:
    def __init__(self, cor: str, tamanho: str, moiado: 0): #esqueci o o pq do __init__ = constructor
        self.cor = cor
        self.tamanho = tamanho
        self.moiado = 0

    def show(self) -> None:    # -> None = nada
        print(self)

    def __str__(self):
        return f"Cor: {self.cor}, Tamnho: {self.tamanho}, Umidade: {self.moiado}"
    
    def dry(self, amount: int): 
        self.moiado += amount  #amount é uma variavel de valor e o += significa q ele cresce
        if self.moiado >= self.getMaxWetness(): #sempre me esqueço o (): no final pra definir uma função
            print("toalha encharcada") #o self faz com q uma função seja singular, ou seja, ela é algo proprio n um nome qualquer
            self.moiado = self.getMaxWetness():

    def getMaxWetness(self):
        if self.tamanho == "P":
            return 10
        if self.tamanho == "M":
            return 20
        if self.tamanho == "G":
            return 30
        
    def wringOut(self): #n me lembro o pq no wringOut o self vim dentro dos ()
        self.moiado = 0 #faz secar a toalha, se alguem "expremer = wringOut" a toalha vai estar seca, ou seja, sem moiado

    def isDry(self): #sempre usa self dentro do () da funcao
        if self.moiado == 0: #indica se a toalha esta seca ou n, se sim true, se n false
            return True
        else:                #os : abrem a sentença n posso esquecer eles
            return False
        

def main():
    toalha = Towel("","", 0)
    while True:               #eu me lembro q esse while true faz com q o comando fique organizado em uma linha, lembro do ph falando de vetor mas eu n lembro como funciona
        linha: str = input()
        print ("$" + linha)
        arg: list[str] =linha.split("")

    if arg[0] == "end":  # n me recordo oq significa o agr 
        break
    elif arg[0] == "criar": #
        cor = arg[1]
        tamanho = arg[2]
        toalha = Towel(cor, tamanho, 0)
    elif arg[0] == "mostrar":
        print(toalha)
    elif arg[0] == "enxugar":   #eu acho q lembro da maioria, mas agr eu to tonta ent eu n vou conseguir pensar
        amount = int(arg[1])
        toalha.dry(amount)
    elif agr[0] == "torcer":
        toalha.wringOut()
    elif arg[0] == "seca":
        if toalha.isDry():
            print("sim")
        else:
            print("nao")



main()





