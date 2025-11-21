import os
from time import sleep

a ='\033[92m'
b ='\033[91m'
c ='\033[0m'
os.system('clear')
print(a+'\t  Tombol Tambahan Termux ')
print(a+'\t  Source :  kumpulanremaja.com')
print(b+'\t  By :   breaksek')
print('\t Tiktok : https://tiktok.com/@breaksek')
print('\t Github : https://github.com/breaksek')
print(a+'+'*40)
print('\nProses ...')
sleep(2)
print(b+'\n[!] Mengambil Tombol Default Termux')
sleep(2)
try:
      os.mkdir('/data/data/com.termux/files/home/.termux')
except:
      pass
print(a+'[!]Success !')
sleep(2)
print(b+'\n[!] menambahkan Tombol Tambahan..')
sleep(1)

key = "extra-keys = [['exit','/','-','PGUP','UP','PGDN',''],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','ENTER']]"
kontol = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
kontol.write(key)
kontol.close()
sleep(2)
print(a+'[!] Memproses  !')
sleep(2)
print(b+'\n[!] Tunggu Sebentar')
sleep(2)
os.system('termux-reload-settings')
print(a+'[!] Proses Selesai !! ^^'+c+'\n\nhubungi : saya lewat Mimpi*\n\n')
