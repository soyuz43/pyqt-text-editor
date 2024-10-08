# window.py
from PyQt5.QtWidgets import QMainWindow, QAction, QMenuBar, QMessageBox
from editor import Editor

class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.editor = Editor(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Simple Text Editor')
        self.setGeometry(100, 100, 640, 480)
        self.setCentralWidget(self.editor.textEdit)
        self.createMenus()

    def createMenus(self):
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('File')

        # New File action
        newAction = QAction('New', self)
        newAction.triggered.connect(self.editor.newFile)
        fileMenu.addAction(newAction)

        # Open File action
        openAction = QAction('Open', self)
        openAction.triggered.connect(self.editor.openFile)
        fileMenu.addAction(openAction)

        # Save File action
        saveAction = QAction('Save', self)
        saveAction.triggered.connect(self.editor.saveFile)
        fileMenu.addAction(saveAction)

        # Save File As action
        saveAsAction = QAction('Save As...', self)
        saveAsAction.triggered.connect(self.editor.saveFileAs)
        fileMenu.addAction(saveAsAction)

        # Exit action
        exitAction = QAction('Exit', self)
        exitAction.triggered.connect(self.close)
        fileMenu.addAction(exitAction)
        # ! Edit Menu
        editMenu = self.menuBar().addMenu('Edit')
        editMenu.addAction(QAction('Cut', self, triggered=self.editor.textEdit.cut))
        editMenu = menuBar.addMenu('Edit')
        editMenu.addAction(QAction('Cut', self, triggered=self.editor.textEdit.cut))
        editMenu.addAction(QAction('Copy', self, triggered=self.editor.textEdit.copy))
        editMenu.addAction(QAction('Paste', self, triggered=self.editor.textEdit.paste))

        helpMenu = menuBar.addMenu('Help')
        aboutAction = QAction('About', self)
        aboutAction.triggered.connect(self.showAbout)
        helpMenu.addAction(aboutAction)

    def showAbout(self):
        QMessageBox.about(self, "About Simple Text Editor", "This is a simple text editor built using PyQt5.")
