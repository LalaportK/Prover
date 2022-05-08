from antlr4 import *
import sys
import os

from logicParser.nodes.ExtendedConjunction import ExtendedConjunction
from logicParser.nodes.ExtendedDisjunction import ExtendedDisjunction
print(sys.path)
from logicParser.LogicLexer import LogicLexer
from logicParser.LogicParser import LogicParser
from logicParser.LogicListener import LogicListener
from logicParser.nodes.Formula import Formula
from formulaHandler.CanonicalFormFactory import *

def main():
    input = InputStream("A \\to (B\\land C\\lor(D \\land E)) \\to E\\lor F")
    lexer = LogicLexer(input)
    stream = CommonTokenStream(lexer)
    parser = LogicParser(stream)
    tree = parser.logicalFormula()
    walker = ParseTreeWalker()
    listener = LogicListener()
    walker.walk(listener, tree)
    formula = Formula(listener.stack.pop())
    print(formula.getFormula())
    # この formula に対していろいろな操作をする
    formulaHandler = CanonicalFormFactory()
    #cnf = formulaHandler.getCNF(formula.getDeepCopy())
    #dnf = formulaHandler.getDNF(formula.getDeepCopy())
    #print("CNF: " + cnf.getFormula())
    eCNF = formulaHandler.getExtendedCNF(formula.getDeepCopy())
    print("ExtendedConjunction: " + eCNF.getFormula())
    #print("DNF: " + dnf.getFormula())
    eDNF = formulaHandler.getExtendedDNF(formula.getDeepCopy())
    print("ExtendedDisjunction: " + eDNF.getFormula())

if __name__ == "__main__":
    main()