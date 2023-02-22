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
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox


class MainWindowSetup(QMainWindow, main_window.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Pastpaper downloader")
        self.Thread = Downloader()
        self.Thread.progress_bar_val.connect(self.update_progress_bar)

    def button_setup(self):
        self.SubmitButton.clicked.connect(self.submit)
        self.ProgressBar.setRange(0, 1)

    def submit(self):
        year = self.YearComboBox.currentText()
        subject = self.SubjectComboBox.currentText()

        # reading tags
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
            # disable push button
            MainWindow.SubmitButton.setEnabled(False)
            # download initial
            self.Thread.update_info(subject[:4], year, tags)
            self.Thread.get_pdfs()
            # progress bar initial
            self.ProgressBar.setRange(0, len(self.Thread.pdfs))
            self.setWindowTitle("Downloading...")
            # connect progress bar
            self.Thread.start()

    def update_progress_bar(self, i):
        # receive emitted value from download thread
        self.ProgressBar.setValue(i)

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
            self.Thread.terminate()
            event.accept()
        else:
            event.ignore()


class Downloader(QThread):
    progress_bar_val = pyqtSignal(int)

    def __init__(self):
        super(Downloader, self).__init__()
        self.C = None
        self.stop_flag = False
        self.subject_code = ""
        self.save_dir = ""
        self.year = ""
        self.pdfs = []
        self.tags = []
        self.DELAY = 30

    def update_info(self, code, year, tags):
        self.subject_code = code
        self.year = year
        self.tags = tags

    def get_pdfs(self):
        subject_name = D.sub_name(self.subject_code)
        self.save_dir = './{}/{}/'.format(self.subject_code, self.year)

        # request from web page
        self.C = Crawler(self.subject_code, subject_name, self.year)
        self.pdfs = self.C.find_pdfs(self.tags)

        # retry when connection failed
        if not self.pdfs:
            MainWindow.http_error(self.C.url)

    def run(self):
        counter = 0

        # download all papers
        for pdf in self.pdfs:
            # terminate if closed
            if self.stop_flag:
                break

            # show current pdf in title
            MainWindow.BarLabel.setText(pdf)
            if create_save_dir(self.save_dir, pdf):
                if not self.C.save_pdfs(pdf, self.save_dir):
                    MainWindow.download_error(pdf)

                # update progress bar
                self.progress_bar_val.emit(counter)

                # pause for delay
                for i in range(self.DELAY):
                    time.sleep(1)
                    MainWindow.BarLabel.setText("Pause for {}s".format(self.DELAY - i))

            counter += 1

        if self.pdfs:
            MainWindow.setWindowTitle("Download complete")
            MainWindow.BarLabel.setText("Pending")

        # resume button
        MainWindow.SubmitButton.setEnabled(True)

    def terminate(self):
        self.stop_flag = True


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
