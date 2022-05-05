from .PropositionalLogicBase import PropositionalLogicBase


class Disjunction(PropositionalLogicBase):
    def __init__(self, right: PropositionalLogicBase, left: PropositionalLogicBase):
        self.left = left
        self.right = right

    def getFormula(self) -> str:
        return "(" + self.left.getFormula() + "\\lor " + self.right.getFormula() + ")"

    def getDeepCopy(self) -> PropositionalLogicBase:
        return Disjunction(self.right.getDeepCopy(), self.left.getDeepCopy())

    def getLeft(self) -> PropositionalLogicBase:
        return self.left

    def getRight(self) -> PropositionalLogicBase:
        return self.right

    def setChildren(self, right: PropositionalLogicBase, left: PropositionalLogicBase):
        self.left = left
        self.right = right