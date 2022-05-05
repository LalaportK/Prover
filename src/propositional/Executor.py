from antlr4 import *
import sys
import os
print(sys.path)
from logicParser.LogicLexer import LogicLexer
from logicParser.LogicParser import LogicParser
from logicParser.LogicListener import LogicListener
from logicParser.nodes.Formula import Formula
from formulaHandler.CanonicalFormFactory import *

def main():
    input = InputStream("A \\to (B\\land C\\lor(D \\land E)) \\to E")
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
    print("CNF: " + formulaHandler.getCNF(formula.getDeepCopy()).getFormula())
    print("DNF: " + formulaHandler.getDNF(formula.getDeepCopy()).getFormula())

if __name__ == "__main__":
    main()