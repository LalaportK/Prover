from abc import ABCMeta, abstractclassmethod, abstractmethod

class PropositionalLogicBase(metaclass=ABCMeta):

    @abstractmethod
    def getFormula(self) -> str:
        pass

    @abstractmethod
    def getDeepCopy(self):
        pass