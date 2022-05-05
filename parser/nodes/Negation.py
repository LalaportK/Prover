from .PropositionalLogicBase import PropositionalLogicBase


class Negation(PropositionalLogicBase):
    def __init__(self, formula: PropositionalLogicBase):
        self.formula = formula

    def getFormula(self) -> str:
        return "\\neg " + self.formula.getFormula()

    def getDeepCopy(self) -> PropositionalLogicBase:
        return Negation(self.formula.getDeepCopy())

    def getChild(self) -> PropositionalLogicBase:
        return self.formula

    def setChildren(self, formula: PropositionalLogicBase):
        self.formula = formula