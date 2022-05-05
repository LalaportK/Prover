# Generated from grammar\Logic.g4 by ANTLR 4.10.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,9,72,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,
        2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,4,
        4,46,8,4,11,4,12,4,47,1,4,1,4,1,4,1,4,4,4,54,8,4,11,4,12,4,55,3,
        4,58,8,4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,4,8,67,8,8,11,8,12,8,68,1,8,
        1,8,0,0,9,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,1,0,3,2,0,65,90,
        97,122,1,0,48,57,3,0,9,10,13,13,32,32,76,0,1,1,0,0,0,0,3,1,0,0,0,
        0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,
        15,1,0,0,0,0,17,1,0,0,0,1,19,1,0,0,0,3,23,1,0,0,0,5,29,1,0,0,0,7,
        34,1,0,0,0,9,57,1,0,0,0,11,59,1,0,0,0,13,61,1,0,0,0,15,63,1,0,0,
        0,17,66,1,0,0,0,19,20,5,92,0,0,20,21,5,116,0,0,21,22,5,111,0,0,22,
        2,1,0,0,0,23,24,5,92,0,0,24,25,5,108,0,0,25,26,5,97,0,0,26,27,5,
        110,0,0,27,28,5,100,0,0,28,4,1,0,0,0,29,30,5,92,0,0,30,31,5,108,
        0,0,31,32,5,111,0,0,32,33,5,114,0,0,33,6,1,0,0,0,34,35,5,92,0,0,
        35,36,5,110,0,0,36,37,5,101,0,0,37,38,5,103,0,0,38,8,1,0,0,0,39,
        58,7,0,0,0,40,41,7,0,0,0,41,42,5,95,0,0,42,43,5,123,0,0,43,45,1,
        0,0,0,44,46,7,1,0,0,45,44,1,0,0,0,46,47,1,0,0,0,47,45,1,0,0,0,47,
        48,1,0,0,0,48,49,1,0,0,0,49,58,5,125,0,0,50,51,7,0,0,0,51,53,5,95,
        0,0,52,54,7,1,0,0,53,52,1,0,0,0,54,55,1,0,0,0,55,53,1,0,0,0,55,56,
        1,0,0,0,56,58,1,0,0,0,57,39,1,0,0,0,57,40,1,0,0,0,57,50,1,0,0,0,
        58,10,1,0,0,0,59,60,5,44,0,0,60,12,1,0,0,0,61,62,5,40,0,0,62,14,
        1,0,0,0,63,64,5,41,0,0,64,16,1,0,0,0,65,67,7,2,0,0,66,65,1,0,0,0,
        67,68,1,0,0,0,68,66,1,0,0,0,68,69,1,0,0,0,69,70,1,0,0,0,70,71,6,
        8,0,0,71,18,1,0,0,0,5,0,47,55,57,68,1,6,0,0
    ]

class LogicLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ImplicationSymbol = 1
    AndSymbol = 2
    OrSymbol = 3
    NegSymbol = 4
    Identifier = 5
    Delimiter = 6
    LeftParenthesis = 7
    RightParenthesis = 8
    WS = 9

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'\\to'", "'\\land'", "'\\lor'", "'\\neg'", "','", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "ImplicationSymbol", "AndSymbol", "OrSymbol", "NegSymbol", "Identifier", 
            "Delimiter", "LeftParenthesis", "RightParenthesis", "WS" ]

    ruleNames = [ "ImplicationSymbol", "AndSymbol", "OrSymbol", "NegSymbol", 
                  "Identifier", "Delimiter", "LeftParenthesis", "RightParenthesis", 
                  "WS" ]

    grammarFileName = "Logic.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


