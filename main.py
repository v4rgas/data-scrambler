import sys
import pandas as pd
from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog
from PyQt5 import uic

window_name, base_class = uic.loadUiType("./main.ui")
class MiVentana(window_name, base_class):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.setWindowTitle('OFG')
        self.filename=''

        self.init_gui()

    
    def init_gui(self):
        self.load_button.clicked.connect(self.openFileNameDialog)
        self.anon_button.clicked.connect(self.anonimize)

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filename, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","Excel (*.xlsx)", options=options)
        self.filename = filename

    def anonimize(self):
        if self.filename:
            pass

if __name__ == '__main__':
    app = QApplication([])    ## Creamos ls base de la app: QApplication
    ventana = MiVentana()     ## Construirmos un QWidget que será nuestra ventana
    ventana.show()            ## Mostramos la ventna
    sys.exit(app.exec())
