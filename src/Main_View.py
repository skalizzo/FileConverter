from PySide2.QtCore import Slot, QThreadPool
from PySide2.QtWidgets import QMainWindow, QFileDialog
from resources.GUI.FileConverter.MainWindow import Ui_MainWindow
from src.converters.converters import CSV_Converter, TXT_Converter
from src.thread_worker import Worker


class Main_View(QMainWindow):
    def __init__(self):
        super().__init__()
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        self.setWindowTitle("File Converter")
        self.threadpool = QThreadPool(self)
        self._ui.pushButton_convertFiles.clicked.connect(self.convert_files)
        #self._ui.comboBox_filetype.removeItem(1)
        self.show()

    @Slot(int)
    def set_progress(self, value: int):
        """
        sets the progress on the progress bar
        :param value: Integer between 0 and 100
        :return:
        """
        self._ui.progressBar_mainProgress.setValue(int(value))

    def get_file_path(self, caption='Bitte wähle die Dateien aus, die umgewandelt werden sollen',
                      initial_directory='',
                      filter="CSV-Files (*.csv)"):
        """
        startet einen Dialog in dem man einen Dateipfad angeben muss um zum Beispiel eine Datei zu importieren
        :param caption: Titel des Dialogs
        :param initial_directory: initiales Verzeichnis in dem gesucht werden soll
        :param filter: Dateityp im Format: "BEZEICHNUNG (erlaubte DateiEndungen)" - z.B. "Excel-Files (.xlsx, .xlsm)"
        :return:
        """
        filepaths = QFileDialog.getOpenFileNames(self, caption, initial_directory, filter)
        if filepaths:
            return filepaths[0]

    def get_converter(self, converter_idx: int):
        """
        gets the file converter for the corresponding combobox index
        :param converter_idx:
        :return:
        """
        converters = {
            0: CSV_Converter,
            1: TXT_Converter
        }
        return converters.get(converter_idx, None)

    def get_delimiters(self, delimiter_idx):
        """
        gets the delimiter sign for the corresponding combobox index
        :param delimiter_idx:
        :return:
        """
        delimiters = {
            0: ",",
            1: ";",
            2: str("\t"),
            3: " ",
        }
        return delimiters.get(delimiter_idx, None)

    def convert_files(self):
        """
        opens a file menu where the user can select files that should be converted;
        then picks the appropriate converter to convert the files to xlsx
        :return:
        """
        file_converter = self.get_converter(self._ui.comboBox_filetype.currentIndex())
        delimiter = self.get_delimiters(self._ui.comboBox_delimiter.currentIndex())
        fc = file_converter()
        fc.set_delimiter(delimiter)
        filter = {
            0: "CSV-Files (*.csv)",
            1: "TXT-Files (*.txt)",
        }.get(self._ui.comboBox_filetype.currentIndex())
        filepaths = self.get_file_path(filter=filter)
        self.start_Worker(fc.convert_files_to_xlsx,
                          filepaths)

    def show_result(self, value):
        """
        display results within the 2 labels
        :param value: a list containing of 2 lists (one for results, one for errors)
        :return:
        """
        result = value[0]
        errors = value[1]

        if result:
            self._ui.label_results.setText("converted Files: \n" + "\n".join(result))
        else:
            self._ui.label_results.setText("")
        if errors:
            self._ui.label_errors.setText("Errors: \n" + "\n".join(errors))
        else:
            self._ui.label_errors.setText("")

    def start_Worker(self, func, *args, **kwargs):
        """
        starts a worker with the given function
        :param func:
        :param args:
        :param kwargs:
        :return:
        """
        worker = Worker(func, *args, **kwargs)
        worker.signals.progress.connect(self.set_progress)
        worker.signals.result.connect(self.show_result)
        self.threadpool.start(worker)
