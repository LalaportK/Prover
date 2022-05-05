from .PropositionalLogicBase import PropositionalLogicBase


class Atom(PropositionalLogicBase):
    def __init__(self, name: str):
        self.name = name

    def getFormula(self) -> str:
        return self.name

    def getDeepCopy(self) -> PropositionalLogicBase:
        return Atom(self.name)