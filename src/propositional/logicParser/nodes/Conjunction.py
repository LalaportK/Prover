from .PropositionalLogicBase import PropositionalLogicBase


class Conjunction(PropositionalLogicBase):
    def __init__(self, right: PropositionalLogicBase, left: PropositionalLogicBase):
        self.left = left
        self.right = right

    def getFormula(self) -> str:
        return "(" + self.left.getFormula() + "\\land " + self.right.getFormula() + ")"

    def getDeepCopy(self) -> PropositionalLogicBase:
        return Conjunction(self.right.getDeepCopy(), self.left.getDeepCopy())

    def getLeft(self) -> PropositionalLogicBase:
        return self.left

    def getRight(self) -> PropositionalLogicBase:
        return self.right

    def setChildren(self, right: PropositionalLogicBase, left: PropositionalLogicBase):
        self.left = left
        self.right = right