from .PropositionalLogicBase import PropositionalLogicBase
from .Conjunction import Conjunction
from .Disjunction import Disjunction
from .ExtendedBinOpBase import ExtendedBinOpBase

class ExtendedDisjunction(ExtendedBinOpBase):
    __children = list[list[PropositionalLogicBase]]
    __original = PropositionalLogicBase

    def __init__(self, cnf: PropositionalLogicBase) -> None:
        self.__children = self.__collectChildren(cnf)
        self.__original = cnf.getDeepCopy()


    def getDeepCopy(self):
        return ExtendedDisjunction(self.__original.getDeepCopy())
        
    def getFormula(self) -> str:
        stringifiedList = map(lambda l: self.getFormulaOfChild(l), self.__children)
        return "\\lor ".join(stringifiedList)

    def getFormulaOfChild(self, childList: list[PropositionalLogicBase]) -> str:
        if len(childList) == 1:
            return childList[0].getFormula()
        l = list(map(lambda p: p.getFormula(), childList))
        return "(" + "\\land ".join(l) + ")"

    def getChildrenList(self) -> list[PropositionalLogicBase]:
        return self.__children

    def __collectChildren(self, dnf: PropositionalLogicBase) -> list[list[PropositionalLogicBase]]:
        ret: list[list[PropositionalLogicBase]] = []
        
        if type(dnf) is Disjunction:
            childrenOfDisj: list[PropositionalLogicBase] = []
            childrenOfDisj = super().unifyAdjacentDisjunctions(dnf)
            # childrenOfDisj has children of type of Atom, Negation, or Conjunction.
            for child in childrenOfDisj:
                ret.append(self.__getChildList(child))
        else:
            ret.append(self.__getChildList(dnf))
        return ret

    def __getChildList(self, p: PropositionalLogicBase) -> list[PropositionalLogicBase]:
        if type(p) is Conjunction:
            return super().unifyAdjacentConjunctions(p)
        else:
            return [p]