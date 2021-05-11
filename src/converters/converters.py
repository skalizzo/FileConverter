import os
import glob
import csv
import traceback
from builtins import callable

from xlsxwriter.workbook import Workbook


class WrongFileTypeException(Exception):
    pass


class Base_Converter:
    delimiter = ","

    def set_delimiter(self, delimiter: str = ","):
        self.delimiter = delimiter

    def convert_files_to_xlsx(self, files: [str], progress_callback: callable) -> [str]:
        """
        converts a list of files to xlsx
        :param files: list of filepaths
        :param callback_func: a callback function that excepts Integers between 0 and 100 as an argument
        used to return progress information
        :return: a list of export paths (file paths for the xlsx files)
        """
        converted_files = []
        errors = []
        nr_of_files = len(files)
        for i, file in enumerate(files):
            progress_callback.emit(int((i / nr_of_files) * 100))
            try:
                converted_file = self.convert_file(file)
                converted_files.append(converted_file)
            except:
                errors.append((str(file) + "\n" + str(traceback.format_exc())))
        progress_callback.emit(100)
        return converted_files, errors

    def convert_file(self, file) -> str:
        """
        converts a file to xlsx
        :param file: filepath as a string
        :return: String - filepath of the exported xlsx file
        """
        pass


class CSV_Converter(Base_Converter):
    def convert_file(self, file) -> str:
        """
        converts a csv file to xlsx
        :param file: filepath as a string
        :return: String - filepath of the exported xlsx file
        """
        if "csv" in str(os.path.splitext(file)[1]).lower():
            workbook = Workbook(os.path.splitext(file)[0] + '.xlsx')
            worksheet = workbook.add_worksheet()
            with open(file, 'rt', encoding='utf8') as f:
                reader = csv.reader(f, delimiter=self.delimiter)
                for r, row in enumerate(reader):
                    for c, col in enumerate(row):
                        worksheet.write(r, c, col)
            workbook.close()
            return str(file)[:-4] + '.xlsx'
        else:
            raise WrongFileTypeException


class TXT_Converter(Base_Converter):
    def convert_file(self, file) -> str:
        if "txt" in str(os.path.splitext(file)[1]).lower():
            workbook = Workbook(os.path.splitext(file)[0] + '.xlsx')
            worksheet = workbook.add_worksheet()
            with open(file, 'rt', encoding='utf8') as f:
                reader = csv.reader(f, delimiter=self.delimiter)
                for r, row in enumerate(reader):
                    for c, col in enumerate(row):
                        worksheet.write(r, c, col)
            workbook.close()
            return str(file)[:-4] + '.xlsx'
        else:
            raise WrongFileTypeException