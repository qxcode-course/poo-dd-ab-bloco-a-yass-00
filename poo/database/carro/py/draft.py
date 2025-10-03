class Carro:
    def __init__(self, pas: int, km: int, pasMax: int, gas: int, gasMax):
        self.pas = 0
        self.km = 0
        self.pasMax = 2
        self.gas = 0
        self.gasMax = 100

    def show(self) -> None:
        print(self)

    def __str__(self):
        return f"pass: {self.pas}, gas: {self.gas}, km: {self.km}"
    
    def enter(self):
        if self.pas < self.pasMax:
            self.pas += 1
        else:
            print("fail: limite de pessoas atingido")

    def leave(self):
        if self.pas == 0:
            print("fail: nao ha ninguem no carro")
        else:
            self.pas -= 1

    def fuel(self, increment: int):
        self.gas += increment
        if self.gas > self.gasMax:
            b = self.gas - self.gasMax
            self.gas -=  b

    def drive(self, distance: int):
        if self.gas == 0:
            print("fail: tanque vazio")
        elif self.pas == 0:
            print("fail: nao ha ninguem no carro")
        else:
            if self.gas >= distance:
                self.gas -= distance
                self.km += distance
            else:
                print(f"fail: tanque vazio apos andar {self.gas} km")
                self.km += self.gas
                self.gas = 0


def main():
    carro = Carro(0, 0, 2, 0, 100)
    while True:
        linha: str = input()
        print("$" + linha)
        arg: list[str] = linha.split(" ")

        if arg[0] == "end":
            break
        elif arg[0] == "show":
            print(carro)
        elif arg[0] == "enter":
            carro.enter()
        elif arg[0] == "leave":
            carro.leave()
        elif arg[0] == "fuel":
            increment = int(arg[1])
            carro.fuel(increment)
        elif arg[0] == "drive":
            distance = int(arg[1])
            carro.drive(distance)


main()

