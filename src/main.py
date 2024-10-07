# main.py
import sys
from PyQt5.QtWidgets import QApplication
from window import TextEditor  # Make sure this import matches your project's file and class names.

def main():
    app = QApplication(sys.argv)  # Create an instance of QApplication
    editor = TextEditor()         # Create an instance of your main window class
    editor.show()                 # Show the main window
    sys.exit(app.exec_())         # Start the application's event loop

if __name__ == '__main__':
    main()
