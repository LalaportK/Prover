from antlr4 import *
from LogicLexer import LogicLexer
from LogicParser import LogicParser
from LogicListener import LogicListener
from nodes.Formula import Formula

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
    formula = formula.getDNF()
    print("DNF: " + formula.getFormula())
    

if __name__ == "__main__":
    main()