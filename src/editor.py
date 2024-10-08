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
    def saveFile(self):
        filename, _ = QFileDialog.getSaveFileName(self.parent, 'Save File', '', 'Text Files (*.txt);;All Files (*)')
        if filename:
            with open(filename, 'w') as file:
                file.write(self.textEdit.toPlainText())  # Write the plain text from QTextEdit to the file
    def saveFileAs(self):
        self.saveFile()  # Just call the saveFile method

    def newFile(self):
        self.textEdit.clear()
        
