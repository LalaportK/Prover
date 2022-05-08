from .PropositionalLogicBase import PropositionalLogicBase
from .Conjunction import Conjunction
from .Disjunction import Disjunction
from .ExtendedBinOpBase import ExtendedBinOpBase

class ExtendedConjunction(ExtendedBinOpBase):
    __children = list[list[PropositionalLogicBase]]
    __original = PropositionalLogicBase

    def __init__(self, cnf: PropositionalLogicBase) -> None:
        self.__children = self.__collectChildren(cnf)
        self.__original = cnf.getDeepCopy()


    def getDeepCopy(self):
        return ExtendedConjunction(self.__original.getDeepCopy())
        
    def getFormula(self) -> str:
        stringifiedList = map(lambda l: self.getFormulaOfChild(l), self.__children)
        return "\\land ".join(stringifiedList)

    def getFormulaOfChild(self, childList: list[PropositionalLogicBase]) -> str:
        if len(childList) == 1:
            return childList[0].getFormula()
        l = list(map(lambda p: p.getFormula(), childList))
        return "(" + "\\lor ".join(l) + ")"

    def getChildrenList(self) -> list[PropositionalLogicBase]:
        return self.__children

    def __collectChildren(self, cnf: PropositionalLogicBase) -> list[list[PropositionalLogicBase]]:
        ret: list[list[PropositionalLogicBase]] = []
        
        if type(cnf) is Conjunction:
            childrenOfConj: list[PropositionalLogicBase] = []
            childrenOfConj = super().unifyAdjacentConjunctions(cnf)
            # childrenOfConj has children of type of Atom, Negation, or Disjunction.
            for child in childrenOfConj:
                ret.append(self.__getChildList(child))
        else:
            ret.append(self.__getChildList(cnf))
        return ret

    def __getChildList(self, p: PropositionalLogicBase) -> list[PropositionalLogicBase]:
        if type(p) is Disjunction:
            return super().unifyAdjacentDisjunctions(p)
        else:
            return [p]