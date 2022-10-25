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

        tags = []
        if self.MS_Box.isChecked():
            tags.append('ms')
        if self.QP_Box.isChecked():
            tags.append('qp')
        if self.CI_Box.isChecked():
            tags.append('ci')
        if self.GT_Box.isChecked():
            tags.append('gt')

        if not tags:
            self.tag_error()
        else:
            self.setWindowTitle("Connecting...")
            # disable button
            MainWindow.SubmitButton.setEnabled(False)
            # download initial
            download(subject[:4], year, tags)

    def tag_error(self):
        text = "no paper selected"
        QMessageBox.information(self, "Warning", text, QMessageBox.Yes)

    def http_error(self, url):
        text = "Site can be reached! url:{}.".format(url)
        QMessageBox.information(self, "Warning", text, QMessageBox.Yes)

    def closeEvent(self, event):
        text = 'Exit? Downloads will not continue.'
        reply = QMessageBox.question(self, 'Warning', text, QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


def download(subject_code, year, tags):
    DELAY = 30
    counter = 0
    subject_name = D.sub_name(subject_code)
    save_dir = './{}/{}/'.format(subject_code, year)

    # request from web page
    C = Crawler(subject_code, subject_name, year)
    pdfs = C.find_pdfs(tags)

    # retry when connection failed
    if not pdfs:
        MainWindow.http_error(C.url)

    total = len(pdfs)

    # download all papers
    for pdf in pdfs:
        # show current pdf in title
        MainWindow.setWindowTitle("{}/{}: {}".format(counter, total, pdf))
        if create_save_dir(save_dir, pdf):
            if not C.save_pdfs(pdf, save_dir):
                MainWindow.download_error(pdf)

            # pause for delay
            for i in range(DELAY):
                time.sleep(1)
                MainWindow.setWindowTitle("Pause for {}s".format(DELAY - i))

        counter += 1

    if pdfs:
        MainWindow.setWindowTitle("Download complete")
    # resume button
    MainWindow.SubmitButton.setEnabled(True)


if __name__ == '__main__':
    # fetch info from json
    D = Data()
    D.read_json()

    # UI initial - Main window
    app = QApplication(sys.argv)
    MainWindow = MainWindowSetup()
    MainWindowSetup.button_setup(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
