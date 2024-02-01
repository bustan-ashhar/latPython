from pendaftar import Pendaftar
from khs import Khs

class Mahasiswa(Pendaftar, Khs):
    __nim = ""
    __ipk = ""
    __prodi = ""
    __krs = []
    

    def Mahasiswa():
        print("Data Mahasiswa")

    def __init__(self, nama, nik, jenis_kelamin, alamat):
        Pendaftar.__init__(self, nama, nik, jenis_kelamin, alamat)
        #super().__init__(nama, nik, jenis_kelamin, alamat)

    def _setNim(self, nim):
        self.__nim = nim
    
    def _setProdi(self, nim):
        self.__nim = nim
    
    def _setKRS(self, matkul, kelas):
        mk = {'id': matkul, 'kelas':kelas}
        self.__krs.append(mk)
    
    def getKRS(self):
        print('\n')
        print('Kartu Rencana Studi')
        return self.__krs
    
    def _setKHS(self, matkul, nilai):
        return super()._setKHS(matkul, nilai)
    
    def showKHS(self):
        print('\n')
        print('Kartu Hasil Studi')
        return super().showKHS()
        
    def getDataMahasiswa(self):
        status  = Pendaftar._getStatus(self)
        ketStatus = "Tidak Lulus"
        if status > 0:
            if status == 1:
                ketStatus = "Lulus"
            elif status == 2:
                ketStatus = "Lulus Harus Tes Toefl"
            else:
                ketStatus = "Status Tidak Diketahui"
                
        print('Status Mahasiswa')
        return f"{self._nama} {self.__nim} {ketStatus}"
