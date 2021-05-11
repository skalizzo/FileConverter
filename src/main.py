import sys
from PySide2.QtWidgets import QApplication
from src.Main_View import Main_View

try:
    # Include in try/except block if you're also targeting Mac/Linux
    from PySide2.QtWinExtras import QtWin
    myappid = 'leonine.digitalsales.fileconverter.0.1'
    QtWin.setCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass

class App(QApplication):
    """
    The application
    """
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.view = Main_View()



if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec_())
