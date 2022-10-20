"""
main.pyw
coding:utf-8

Developed by @Luke.Tang 2022
This program crawl cambridge a level papers from papers.gceguide.com.
For more information, please visit github.com/luke-tangh/a-level-paper-downloader
"""

import sys
import time
import main_window
from files import Data
from downloader import Crawler, create_save_dir
from PyQt5.QtCore import QStringListModel
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox


class MainWindowSetup(QMainWindow, main_window.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Pastpaper downloader")

    def button_setup(self):
        self.SubmitButton.clicked.connect(self.submit)

    def submit(self):
        year = self.YearComboBox.currentText()
        subject = self.SubjectComboBox.currentText()
        download(year, subject[:4])

    def display_info(self, log: list):
        model = QStringListModel()
        model.setStringList(log)
        self.ProgressList.setModel(model)

    def http_error(self, url):
        text = "Site can be reached! url:{}, retry?".format(url)
        reply = QMessageBox.information(self, "Warning", text, QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            return True
        else:
            return False

    def download_error(self, pdf):
        text = "Failed to download! pdf:{}, retry?".format(pdf)
        reply = QMessageBox.information(self, "Warning", text, QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            return True
        else:
            return False

    def closeEvent(self, event):
        text = 'Exit? Downloads will not continue.'
        reply = QMessageBox.question(self, 'Warning', text, QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


def download(year, subject_code):
    log = ["Read from json..."]
    MainWindow.display_info(log)

    # fetch info from json
    D = Data()
    D.read_json()

    # parameter starts here
    DELAY = 30
    subject_name = D.sub_name(subject_code)
    save_dir = './{}/{}/'.format(subject_code, year)

    log.append("Subject:{}".format(subject_name))
    log.append("Attempting to connect...".format(subject_name))
    MainWindow.display_info(log)

    C = Crawler(subject_code, subject_name, year)
    pdfs = C.find_pdfs()
    while not pdfs:
        if MainWindow.http_error(C.url):
            pdfs = C.find_pdfs()
        else:
            break

    for pdf in pdfs:
        MainWindow.display_info(log)
        if not create_save_dir(save_dir, pdf):
            log.append("File exist:{}".format(pdf))
            MainWindow.display_info(log)
            continue
        while True:
            if C.save_pdfs(pdf, save_dir):
                log.append("Saved: {}".format(pdf))
                MainWindow.display_info(log)
                break
            else:
                if not MainWindow.download_error(pdf):
                    break
        time.sleep(DELAY)
    log.append("Download complete")
    MainWindow.display_info(log)


if __name__ == '__main__':
    # UI initial - Main window
    app = QApplication(sys.argv)
    MainWindow = MainWindowSetup()
    MainWindowSetup.button_setup(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
