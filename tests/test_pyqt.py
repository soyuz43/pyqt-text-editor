# test_pyqt.py
from PyQt5 import QtWidgets

app = QtWidgets.QApplication([])
window = QtWidgets.QMainWindow()
window.show()
app.exec_()
