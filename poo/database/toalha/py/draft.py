class Towel:
    def __init__(self, color: str, size: str):
        self.color: str = color
        self.size: str = size
        self.wetness: int = 0
        print(f"estou criando uma toalha {color}, de tamanhp {size}")
def dry(self, amount: int) -> None:
    self.wetness += amount

def __str__(self) -> str:
    return f"Cor:{self.color}, Tam:[self.size, Umidade:{self.wetness}"

toalha = Towel("red", "M")

print(toalha)
toalha.dry(5)
toalha.dry(15)
print(toalha)