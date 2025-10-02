class Animal:
    def __init__(self, especie: str,idade: int, som: str):
        self.especie = especie
        self.idade: int = 0  #inicia com 0 mas eu n lembro como faz isso
        self.som = som

    def show(self) -> None:
        print(self)
    
    def __str__(self):
        return f"{self.especie}:{self.idade}:{self.som}"
    
    def ageBy(self, increment: int):
        self.idade += increment
        if self.idade >= 4:
            print(f"warning: {self.especie} morreu")
            self.idade = 4

    def makeSound(self):
        if self.idade == 0:
            return "---"
        elif self.idade == 4:
            return "RIP"
        else:
            return self.som
        


def main():
    animal = Animal("",0,"")
    while True:
        linha: str = input()
        print("$" + linha)
        arg: list[str] = linha.split(" ")
        if arg[0] == "end":
            break
        elif arg[0] == "init":
            especie = arg[1]
            som = arg[2]
            animal = Animal(especie, 0, som)
        elif arg[0] == "show":
            print(animal)
        elif arg[0] == "grow":
            increment = int(arg[1])
            animal.ageBy(increment)
        elif arg[0] == "noise":
            print(animal.makeSound())
            


main()



        