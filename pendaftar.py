class Pendaftar:
    _nik = ""  #protected
    _nama = "" #protected
    _jenisKelamin = "" #protected
    _alamat = "" #protected
    __status = 2 # 0=Tidak Lulus, 1=Lulus, 2=Lulus harus Toefl #private

    def __init__(self, nama, nik, jenis_kelamin, alamat):
        self._nama = nama
        self._nik = nik
        self._jenisKelamin = jenis_kelamin
        self._alamat = alamat

    '''def _setStatus(self, status): #method protected
        self.__status = status'''
    
    def _getStatus(self):
        return self.__status