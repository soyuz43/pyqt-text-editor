# editor.py
from PyQt5.QtWidgets import QFileDialog, QTextEdit

class Editor:
    def __init__(self, parent):
        self.parent = parent
        self.textEdit = QTextEdit()

    def openFile(self):
        filename, _ = QFileDialog.getOpenFileName(self.parent, 'Open File', '', 'Text Files (*.txt);;All Files (*)')
        if filename:
            with open(filename, 'r') as file:
                self.textEdit.setText(file.read())
        # Implement saveFile, newFile, etc.
