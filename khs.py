from abc import ABC, abstractmethod

class Khs:
    __list = []
    
    @abstractmethod
    def _setKHS(self, matkul, nilai):
        pass

    def getKHS(self):
        return self.__list
    
    def _kalkulasiIPK():
        pass