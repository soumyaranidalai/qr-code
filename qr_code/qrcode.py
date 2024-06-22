import pyqrcode

x = pyqrcode.create("i am a developer: ")
x.svg('orgen.svg',scale=10)