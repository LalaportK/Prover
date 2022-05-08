from .PropositionalLogicBase import PropositionalLogicBase
from .Conjunction import Conjunction
from .Disjunction import Disjunction

class ExtendedBinOpBase(PropositionalLogicBase):

    def __init__(self, p:PropositionalLogicBase) -> None:
        pass

    def getDeepCopy(self):
        pass

    def getFormula(self) -> str:
        pass

    def unifyAdjacentConjunctions(self, c: Conjunction) -> list[PropositionalLogicBase]:
        """
        Contruct edges adjacent to c recursively and return the children of c.

        ------
        Parameters
        c: Conjunction
            Original AST.
        
        ------
        Returns
        children: list[PropositionalLogicBase]
            Children of the contructed AST.
        """
        ret: list[PropositionalLogicBase] = []
        left = c.getLeft()
        right = c.getRight()
        ret.extend(self.getChildOfConjunctions(left))
        ret.extend(self.getChildOfConjunctions(right))
        return ret

    def getChildOfConjunctions(self, p: PropositionalLogicBase) -> list[PropositionalLogicBase]:
        ret: list[PropositionalLogicBase] = []
        if type(p) is Conjunction:
            ret.extend(self.unifyAdjacentConjunctions(p))
        else:
            ret.append(p)
        return ret

    def unifyAdjacentDisjunctions(self, d: Disjunction) -> list[PropositionalLogicBase]:
        ret: list[PropositionalLogicBase] = []
        left = d.getLeft()
        right = d.getRight()
        ret.extend(self.getChildOfDisjunctions(left))
        ret.extend(self.getChildOfDisjunctions(right))
        return ret

    def getChildOfDisjunctions(self, p: PropositionalLogicBase) -> list[PropositionalLogicBase]:
        ret: list[PropositionalLogicBase] = []
        if type(p) is Disjunction:
            ret.extend(self.unifyAdjacentDisjunctions(p))
        else:
            ret.append(p)
        return ret