from abc import ABC, abstractmethod
from matakuliah import list as matkul

class Khs:
    __list = []
    __bobotNilai = {'A' : 4, 'A-':3.75, 'B+':3.5, 'B':3, 'C':2.5, 'D':2, 'E':0}
    
    @abstractmethod
    def _setKHS(self, matkul, nilai):
        data = {'id':matkul, 'nilai':nilai}
        self.__list.append(data)

    @abstractmethod
    def getKHS(self):
        return self.__list
    
    @abstractmethod
    def showKHS(self):
        tNilai = 0
        tSks = 0
        tBobot = 0
        for k in self.__list:
            tNilai += k['nilai']
            tSks += matkul[k['id']]['sks']
            tBobot += matkul[k['id']]['sks'] * self.__bobotNilai[self.__nilaiHuruf(k['nilai'])]
            print(matkul[k['id']]['nama'], matkul[k['id']]['sks'], k['nilai'], self.__nilaiHuruf(k['nilai']))

        print(tSks)
        print(tBobot)
        print('IPK : ', self._kalkulasiIPK(tSks, tBobot))

    def _kalkulasiIPK(self, totalSKS, totalBobot):
        ipk = round(totalBobot/totalSKS, 2)
        return ipk

    def __nilaiHuruf(self, nilai):
        huruf = 'E'
        if nilai > 90:
            huruf = 'A'
        elif nilai > 85 and nilai <= 90:
            huruf = 'A-'
        elif nilai > 75 and nilai <= 85:
            huruf = 'B+'
        elif nilai > 65 and nilai <= 75:
            huruf = 'C'
        elif nilai > 0 and nilai <= 65:
            huruf = 'D'

        return huruf

