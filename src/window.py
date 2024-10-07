# window.py
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QMenuBar, QAction, QFileDialog, QMessageBox
from editor import Editor

class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.editor = Editor(self)  # Create an instance of the Editor class
        self.initUI()

    def initUI(self):
        # Initialize the UI components
        self.setWindowTitle('Simple Text Editor')
        self.setGeometry(100, 100, 640, 480)
        self.setCentralWidget(self.editor.textEdit)
        self.createMenus()

    def createMenus(self):
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('File')
        fileMenu.addAction(QAction('Open', self, triggered=self.editor.openFile))
        # Add other file menu actions...

        editMenu = menuBar.addMenu('Edit')
        editMenu.addAction(QAction('Cut', self, triggered=self.editor.textEdit.cut))
        # Add copy, paste actions...

        helpMenu = menuBar.addMenu('Help')
        helpMenu.addAction(QAction('About', self, triggered=self.showAbout))

    def showAbout(self):
        QMessageBox.about(self, "About Simple Text Editor", "This is a simple text editor built using PyQt5.")
