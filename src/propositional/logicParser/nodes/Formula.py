from .PropositionalLogicBase import PropositionalLogicBase


class Formula(PropositionalLogicBase):
    def __init__(self, formula: PropositionalLogicBase):
        self.formula = formula
    
    def getFormula(self) -> PropositionalLogicBase:
        return self.formula.getFormula()

    def getDeepCopy(self) -> PropositionalLogicBase:
        """
        Returns
        ------
        deepCopy : PropositionalLogicBase
            A deepCopy of this formula.
        """
        return self.formula.getDeepCopy()

