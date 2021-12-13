#Programm funktioniert nur, wenn die Zip-Datei in einem Ordner ist, in dem sich sonst nichts befindet.
import os
import zipfile

def entpacken(pfad):
    for i in range(2021):
        namensliste = os.listdir(pfad)
        name = namensliste.pop()

        ziel = pfad  + '\\' + name
        verarbeite = zipfile.ZipFile(ziel)
        verarbeite.extractall(pfad)
        verarbeite.close()

        os.remove(ziel)

entpacken('C:\\Users\%username%\pfad\zum\ziel')

