import subprocess
import sys
# converts the ui file for mainwindow to a python File (PySide6)
result = subprocess.run(["C://Python_Projects//FileConverter//venv//Scripts//pyside2-uic.exe", "C:/Python_Projects/FileConverter/resources/GUI/FileConverter/mainwindow.ui", "-o", "C:/Python_Projects/FileConverter/resources/GUI/FileConverter/MainWindow.py"])
print('aktuelle GUI erstellt')