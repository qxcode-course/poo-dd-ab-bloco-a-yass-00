class Calculadora:
    def __init__(self, display: int, bateria: int, batteryMax: int):
        self.display = 0
        self.bateria = 0
        self.batteryMax = batteryMax

    def show(self) -> None:
        print(self)

    def __str__(self):
        return f"display = {self.display:.2f}, battery = {self.bateria}"

    def charge(self, increment: int):
        self.bateria += increment
        if self.bateria >= self.batteryMax:
            self.bateria = self.batteryMax

    def sum(self, a: int, b: int):
        if self.bateria == 0:
            print("fail: bateria insuficiente")
        else:
            self.display = a + b
            self.bateria -= 1

    def div(self, a:int, b: int):
        if self.bateria > 0:
            if b == 0:
                print("fail: divisao por zero")
            else:
                self.display = a/b
            self.bateria -= 1
        else:
            print("fail: bateria insuficiente")


def main():
    calculadora = Calculadora(0,0,"")
    while True:
        linha: str = input()
        print("$" + linha)
        arg: list[str] = linha.split(" ")
        
        if arg[0] == "end":
            break
        elif arg[0] == "init":
            batteryMax = int(arg[1])
            calculadora = Calculadora(0,0, batteryMax)
        elif arg[0] == "show":
            print(calculadora)
        elif arg[0] == "sum":
            a = int(arg[1])
            b = int(arg[2])
            calculadora.sum(a, b)
        elif arg[0] == "div":
            a = int(arg[1])
            b = int(arg[2])
            calculadora.div(a, b)
        elif arg[0] == "charge":
            increment = int(arg[1])
            calculadora.charge(increment)


main()
            