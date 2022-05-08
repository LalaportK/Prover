from logicParser.nodes.PropositionalLogicBase import *
from logicParser.nodes.Atom import *
from logicParser.nodes.Conjunction import *
from logicParser.nodes.Disjunction import *
from logicParser.nodes.Negation import *
from logicParser.nodes.To import *
from logicParser.nodes.ExtendedBinOpBase import ExtendedBinOpBase
from logicParser.nodes.ExtendedConjunction import ExtendedConjunction
from logicParser.nodes.ExtendedDisjunction import ExtendedDisjunction

class CanonicalFormFactory:
    def __init__(self):
        pass

    def getExtendedCNF(self, formula: PropositionalLogicBase) -> ExtendedBinOpBase:
        return ExtendedConjunction(self.getCNF(formula))

    def getExtendedDNF(self, formula: PropositionalLogicBase) -> ExtendedBinOpBase:
        return ExtendedDisjunction(self.getDNF(formula))


    def getCNF(self, formula: PropositionalLogicBase) -> PropositionalLogicBase:
        """
        Calculates CNF of this formula.
        Returns
        ------
        expanded : PropositionalLogicBase
            CNF of this formula.
        """
        preProcessed = self.__canonicalPreProcess(formula.getDeepCopy())
        expanded = self.__expandOr(preProcessed)
        return expanded

    def __expandOr(self, formula: PropositionalLogicBase) -> PropositionalLogicBase:
        """
        Expands \"or\" operators which are the parents of \"and\" operator.

        Parameters
        ------
        formula : PropositionalLogicBase
            The target to expand.
        """
        print("__expandOr " + formula.getFormula())
        expanded = formula
        if type(formula) is Disjunction:
            right = self.__expandOr(formula.getRight())
            left = self.__expandOr(formula.getLeft())
            if type(right) is Conjunction:
                rightOfRight = right.getRight()
                leftOfRight = right.getLeft()
                expanded =  Conjunction(self.__expandOr(Disjunction(rightOfRight, left)), self.__expandOr(Disjunction(leftOfRight, left)))
            elif type(left) is Conjunction:
                rightOfLeft = left.getRight()
                leftOfLeft = left.getLeft()
                expanded =  Conjunction(self.__expandOr(Disjunction(right, rightOfLeft)), self.__expandOr(Disjunction(right, leftOfLeft)))
        elif type(formula) is Negation:
            expanded =  Negation(self.__expandOr(formula.getChild()))
        elif type(formula) is Conjunction:
            expanded = Conjunction(self.__expandOr(formula.getRight()), self.__expandOr(formula.getLeft()))
        else:
            expanded =  formula
        print("expanded : " + expanded.getFormula())
        return expanded

    def getDNF(self, formula: PropositionalLogicBase) -> PropositionalLogicBase:
        """
        Calculates DNF of this formula.

        Returns
        ------
        expanded : PropositionalLogicBase
            DNF of this formula.
        """
        preProcessed = self.__canonicalPreProcess(formula.getDeepCopy())
        expanded = self.__expandAnd(preProcessed)
        return expanded

    # Almost the same as __expandOr (a kind of duality)
    def __expandAnd(self, formula: PropositionalLogicBase) -> PropositionalLogicBase:
        """
        Expands \"and\" operators which are the parents of \"or\" operator.

        Parameters
        ------
        formula : PropositionalLogicBase
            The target to expand.
        
        Returns
        ------
        expanded : PropositionalLogicBase
            DNF of this formula.
        """
        print("__expandAnd " + formula.getFormula())
        expanded = formula
        if type(formula) is Conjunction:
            right = self.__expandAnd(formula.getRight())
            left = self.__expandAnd(formula.getLeft())
            if type(right) is Disjunction:
                rightOfRight = right.getRight()
                leftOfRight = right.getLeft()
                expanded =  Disjunction(self.__expandAnd(Conjunction(rightOfRight, left)), self.__expandAnd(Conjunction(leftOfRight, left)))
            elif type(left) is Disjunction:
                rightOfLeft = left.getRight()
                leftOfLeft = left.getLeft()
                expanded = Disjunction(self.__expandAnd(Conjunction(right, rightOfLeft)), self.__expandAnd(Conjunction(right, leftOfLeft)))
        elif type(formula) is Negation:
            expanded =  Negation(self.__expandAnd(formula.getChild()))
        elif type(formula) is Disjunction:
            expanded = Disjunction(self.__expandAnd(formula.getRight()), self.__expandAnd(formula.getLeft()))
        else:
            expanded =  formula
        print("expanded : " + expanded.getFormula())
        return expanded
    
    def __canonicalPreProcess(self, formula: PropositionalLogicBase) -> PropositionalLogicBase:
        """
        Common procedure for obtaining CNF and DNF.

        Parameters
        ------
        formula : PropositionalLogicBase
        
        Returns
        ------
        processed : PropositionalLogicBase
            Pre-processed formula.
        """
        print("__canonicalPreProcess :" + formula.getFormula())
        eliminated = self.__eliminateTo(formula)
        print("eliminated = " + eliminated.getFormula())
        return self.__distributeNegation(eliminated)

    def __eliminateTo(self, formula: PropositionalLogicBase) -> PropositionalLogicBase:
        """
        Eliminates implications in the formula.

        Parameters
        ------
        formula : PropositionalLogicBase
            The target to eliminate implications.
        
        Returns
        ------
        eliminated : PropositionalLogicBase
            The formula in which implications are eliminated.
        """
        print("__eliminateTo :" + formula.getFormula())
        if type(formula) is Conjunction or type(formula) is Disjunction:
            formula.setChildren(self.__eliminateTo(formula.getRight()), self.__eliminateTo(formula.getLeft()))
        elif type(formula) is Negation:
            formula.setChildren(self.__eliminateTo(formula))
        elif type(formula) is To:
            return Disjunction(self.__eliminateTo(formula.getRight()), Negation(self.__eliminateTo(formula.getLeft())))
        return formula

    def __distributeNegation(self, formula: PropositionalLogicBase) -> PropositionalLogicBase:
        """
        Distributes the negation in the formula.

        Parameters
        ------
        formula : PropositionalLogicBase
            The target to distribute negations.
        
        Returns
        ------
        distributed : PropositionalLogicBase
            The formula in which negations are distributed.
        """
        print("__distributeNegation :" + formula.getFormula())
        distributed = formula
        if type(formula) is Negation:
            child = formula.getChild()
            if type(child) is Disjunction:
                distributed = Conjunction(self.__distributeNegation(Negation(child.getRight())), self.__distributeNegation(Negation(child.getLeft())))
            elif type(child) is Conjunction:
                distributed = Disjunction(self.__distributeNegation(Negation(child.getRight())), self.__distributeNegation(Negation(child.getLeft())))
            elif type(child) is Negation:
                # eliminate duplicated negation
                distributed = child.getChild()
        elif type(formula) is Conjunction or type(formula) is Disjunction:
            formula.setChildren(self.__distributeNegation(formula.getRight()), self.__distributeNegation(formula.getLeft()))
            distributed = formula
        print("distributed = " + distributed.getFormula())
        return distributed