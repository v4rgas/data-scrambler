import sys

import hashlib
import uuid
import random
import numpy as np
import pandas as pd
from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog, QLabel, QVBoxLayout
from PyQt5 import uic


window_name, base_class = uic.loadUiType("./item.ui")


class Item(window_name, base_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.colnames = self.hbox.itemAt(0).widget()
        self.options = self.hbox.itemAt(1).widget()


window_name, base_class = uic.loadUiType("./main.ui")


class MiVentana(window_name, base_class):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.setWindowTitle('OFG')
        self.filename = ''
        self.items = []
        self.dataframe = pd.DataFrame()

        self.init_gui()

    def init_gui(self):
        self.buttonLayout = QVBoxLayout()
        # buttonLayout.addWidget(Item())
        # buttonLayout.addWidget(Item())
        # buttonLayout.addWidget(Item())
        # buttonLayout.addWidget(Item())
        # buttonLayout.addWidget(Item())
        # buttonLayout.addWidget(Item())
        # buttonLayout.addWidget(Item())
        # buttonLayout.addWidget(Item())

        self.scrollArea.widget().setLayout(self.buttonLayout)

        self.load_button.clicked.connect(self.openFileNameDialog)
        self.anon_button.clicked.connect(self.anonimize)
        self.additem.clicked.connect(self.addItem)

    def addItem(self):
        if len(self.dataframe.columns):
            item = Item()
            item.colnames.addItems(self.dataframe.columns.values)
            self.items.append(item)
            self.buttonLayout.addWidget(item)
            print(item)

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.filename, _ = QFileDialog.getOpenFileName(
            self, "QFileDialog.getOpenFileName()", "", "Excel (*.xlsx)", options=options)

        if self.filename:
            self.dataframe = pd.read_excel(self.filename)

    def anonimize(self):
        if len(self.dataframe.columns):
            for item in self.items:
                current = item.colnames.currentText()
                option = item.options.currentText()
                if current:
                    if option == 'Barajar':
                        self.dataframe[current] = np.random.permutation(self.dataframe[current].values)
                        print(self.dataframe[current])

                    if option == 'Pseudoanonimizacion':
                        def hash_name(string):
                            m = hashlib.md5(string.encode('utf-8'))
                            return str(uuid.UUID(m.hexdigest()))
                        self.dataframe[current] = self.dataframe[current].apply(hash_name)

                    if option == 'Enmascaramiento':
                        self.dataframe[current] = self.dataframe[current].apply(lambda x: ''.join(random.sample(x, len(x))).lower())

                    if option == 'Suprimir':
                        self.dataframe[current] = self.dataframe[current].apply(lambda x: '*')

        self.dataframe.to_excel('modified.xlsx',index=False)


if __name__ == '__main__':
    app = QApplication([])  # Creamos ls base de la app: QApplication
    ventana = MiVentana()  # Construirmos un QWidget que será nuestra ventana
    ventana.show()  # Mostramos la ventna
    sys.exit(app.exec())
