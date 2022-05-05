# Generated from grammar\Logic.g4 by ANTLR 4.10.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,9,32,2,0,7,0,2,1,7,1,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,3,1,16,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,27,8,1,10,
        1,12,1,30,9,1,1,1,0,1,2,2,0,2,0,0,34,0,4,1,0,0,0,2,15,1,0,0,0,4,
        5,3,2,1,0,5,6,5,0,0,1,6,1,1,0,0,0,7,8,6,1,-1,0,8,16,5,5,0,0,9,10,
        5,7,0,0,10,11,3,2,1,0,11,12,5,8,0,0,12,16,1,0,0,0,13,14,5,4,0,0,
        14,16,3,2,1,4,15,7,1,0,0,0,15,9,1,0,0,0,15,13,1,0,0,0,16,28,1,0,
        0,0,17,18,10,3,0,0,18,19,5,3,0,0,19,27,3,2,1,4,20,21,10,2,0,0,21,
        22,5,2,0,0,22,27,3,2,1,3,23,24,10,1,0,0,24,25,5,1,0,0,25,27,3,2,
        1,2,26,17,1,0,0,0,26,20,1,0,0,0,26,23,1,0,0,0,27,30,1,0,0,0,28,26,
        1,0,0,0,28,29,1,0,0,0,29,3,1,0,0,0,30,28,1,0,0,0,3,15,26,28
    ]

class LogicParser ( Parser ):

    grammarFileName = "Logic.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\\to'", "'\\land'", "'\\lor'", "'\\neg'", 
                     "<INVALID>", "','", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "ImplicationSymbol", "AndSymbol", "OrSymbol", 
                      "NegSymbol", "Identifier", "Delimiter", "LeftParenthesis", 
                      "RightParenthesis", "WS" ]

    RULE_top = 0
    RULE_logicalFormula = 1

    ruleNames =  [ "top", "logicalFormula" ]

    EOF = Token.EOF
    ImplicationSymbol=1
    AndSymbol=2
    OrSymbol=3
    NegSymbol=4
    Identifier=5
    Delimiter=6
    LeftParenthesis=7
    RightParenthesis=8
    WS=9

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class TopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalFormula(self):
            return self.getTypedRuleContext(LogicParser.LogicalFormulaContext,0)


        def EOF(self):
            return self.getToken(LogicParser.EOF, 0)

        def getRuleIndex(self):
            return LogicParser.RULE_top

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTop" ):
                listener.enterTop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTop" ):
                listener.exitTop(self)




    def top(self):

        localctx = LogicParser.TopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_top)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.logicalFormula(0)
            self.state = 5
            self.match(LogicParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalFormulaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LogicParser.RULE_logicalFormula

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class DisjunctionContext(LogicalFormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LogicParser.LogicalFormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def logicalFormula(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LogicParser.LogicalFormulaContext)
            else:
                return self.getTypedRuleContext(LogicParser.LogicalFormulaContext,i)

        def OrSymbol(self):
            return self.getToken(LogicParser.OrSymbol, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDisjunction" ):
                listener.enterDisjunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDisjunction" ):
                listener.exitDisjunction(self)


    class NegationContext(LogicalFormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LogicParser.LogicalFormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NegSymbol(self):
            return self.getToken(LogicParser.NegSymbol, 0)
        def logicalFormula(self):
            return self.getTypedRuleContext(LogicParser.LogicalFormulaContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNegation" ):
                listener.enterNegation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNegation" ):
                listener.exitNegation(self)


    class ConjunctionContext(LogicalFormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LogicParser.LogicalFormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def logicalFormula(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LogicParser.LogicalFormulaContext)
            else:
                return self.getTypedRuleContext(LogicParser.LogicalFormulaContext,i)

        def AndSymbol(self):
            return self.getToken(LogicParser.AndSymbol, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConjunction" ):
                listener.enterConjunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConjunction" ):
                listener.exitConjunction(self)


    class AtomicFormulaContext(LogicalFormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LogicParser.LogicalFormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Identifier(self):
            return self.getToken(LogicParser.Identifier, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtomicFormula" ):
                listener.enterAtomicFormula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtomicFormula" ):
                listener.exitAtomicFormula(self)


    class QuotedFormulaContext(LogicalFormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LogicParser.LogicalFormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LeftParenthesis(self):
            return self.getToken(LogicParser.LeftParenthesis, 0)
        def logicalFormula(self):
            return self.getTypedRuleContext(LogicParser.LogicalFormulaContext,0)

        def RightParenthesis(self):
            return self.getToken(LogicParser.RightParenthesis, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuotedFormula" ):
                listener.enterQuotedFormula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuotedFormula" ):
                listener.exitQuotedFormula(self)


    class ImplicationContext(LogicalFormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LogicParser.LogicalFormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def logicalFormula(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LogicParser.LogicalFormulaContext)
            else:
                return self.getTypedRuleContext(LogicParser.LogicalFormulaContext,i)

        def ImplicationSymbol(self):
            return self.getToken(LogicParser.ImplicationSymbol, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImplication" ):
                listener.enterImplication(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImplication" ):
                listener.exitImplication(self)



    def logicalFormula(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LogicParser.LogicalFormulaContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_logicalFormula, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LogicParser.Identifier]:
                localctx = LogicParser.AtomicFormulaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 8
                self.match(LogicParser.Identifier)
                pass
            elif token in [LogicParser.LeftParenthesis]:
                localctx = LogicParser.QuotedFormulaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 9
                self.match(LogicParser.LeftParenthesis)
                self.state = 10
                self.logicalFormula(0)
                self.state = 11
                self.match(LogicParser.RightParenthesis)
                pass
            elif token in [LogicParser.NegSymbol]:
                localctx = LogicParser.NegationContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 13
                self.match(LogicParser.NegSymbol)
                self.state = 14
                self.logicalFormula(4)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 28
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 26
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = LogicParser.DisjunctionContext(self, LogicParser.LogicalFormulaContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalFormula)
                        self.state = 17
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 18
                        self.match(LogicParser.OrSymbol)
                        self.state = 19
                        self.logicalFormula(4)
                        pass

                    elif la_ == 2:
                        localctx = LogicParser.ConjunctionContext(self, LogicParser.LogicalFormulaContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalFormula)
                        self.state = 20
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 21
                        self.match(LogicParser.AndSymbol)
                        self.state = 22
                        self.logicalFormula(3)
                        pass

                    elif la_ == 3:
                        localctx = LogicParser.ImplicationContext(self, LogicParser.LogicalFormulaContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalFormula)
                        self.state = 23
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 24
                        self.match(LogicParser.ImplicationSymbol)
                        self.state = 25
                        self.logicalFormula(2)
                        pass

             
                self.state = 30
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.logicalFormula_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def logicalFormula_sempred(self, localctx:LogicalFormulaContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 1)
         




