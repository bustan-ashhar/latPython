from mahasiswa import Mahasiswa

m = Mahasiswa("Ashhar", "3242342465467546", "L", "Palopo")
m._setNim("D082231024")
print(m.getDataMahasiswa())
#print(list)
m._setKRS(1, 'A')
m._setKRS(3, 'B')
print(m.getKRS())

m._setKHS(1, 85)
m._setKHS(3, 90)
m.showKHS()