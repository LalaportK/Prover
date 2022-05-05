# Generated from grammar\Logic.g4 by ANTLR 4.10.1
from antlr4 import *

from .nodes.Atom import Atom
from .nodes.Negation import Negation
from .nodes.Conjunction import Conjunction
from .nodes.To import To
from .nodes.Stack import Stack
from .nodes.Disjunction import Disjunction
if __name__ is not None and "." in __name__:
    from .LogicParser import LogicParser
else:
    from LogicParser import LogicParser

# This class defines a complete listener for a parse tree produced by LogicParser.
class LogicListener(ParseTreeListener):

    stack = Stack()

    # Exit a parse tree produced by LogicParser#Disjunction.
    def exitDisjunction(self, ctx:LogicParser.DisjunctionContext):
        self.stack.push(Disjunction(self.stack.pop(), self.stack.pop()))

    # Exit a parse tree produced by LogicParser#Negation.
    def exitNegation(self, ctx:LogicParser.NegationContext):
        self.stack.push(Negation(self.stack.pop()))

    # Exit a parse tree produced by LogicParser#Conjunction.
    def exitConjunction(self, ctx:LogicParser.ConjunctionContext):
        self.stack.push(Conjunction(self.stack.pop(), self.stack.pop()))

    # Exit a parse tree produced by LogicParser#AtomicFormula.
    def exitAtomicFormula(self, ctx:LogicParser.AtomicFormulaContext):
        self.stack.push(Atom(ctx.getText()))

    # Exit a parse tree produced by LogicParser#Implication.
    def exitImplication(self, ctx:LogicParser.ImplicationContext):
        self.stack.push(To(self.stack.pop(), self.stack.pop()))

del LogicParser