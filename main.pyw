"""
main.pyw
coding:utf-8

Developed by @Luke.Tang 2022
This program crawl cambridge a level papers from papers.gceguide.com.
For more information, please visit github.com/luke-tangh/a-level-paper-downloader
"""


import sys
import time
import threading
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
        self.Label.setText("Progress:")
        self.progressBar.setRange(0, 1)

    def submit(self):
        year = self.YearComboBox.currentText()
        subject = self.SubjectComboBox.currentText()
        self.setWindowTitle("Connecting...")
        # disable button
        MainWindow.SubmitButton.setEnabled(False)
        # download thread initial
        thread.down_info(subject[:4], year)
        thread.start()

    def init_progress_bar(self, total_pdfs):
        self.progressBar.setRange(0, total_pdfs)

    def update_progress_bar(self, cur):
        self.progressBar.setValue(cur)

    def http_error(self, url):
        text = "Site can be reached! url:{}, retry?".format(url)
        QMessageBox.information(self, "Warning", text, QMessageBox.Yes, QMessageBox.No)

    def download_error(self, pdf):
        text = "Failed to download! pdf:{}, retry?".format(pdf)
        QMessageBox.information(self, "Warning", text, QMessageBox.Yes, QMessageBox.No)

    def closeEvent(self, event):
        text = 'Exit? Downloads will not continue.'
        reply = QMessageBox.question(self, 'Warning', text, QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            thread.terminate()
            event.accept()
        else:
            event.ignore()


'''
class ProgressBar(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.stop_flag = False
'''


class Download(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.stop_flag = False
        self.counter = 0
        self.DELAY = 10
        self.subject_code = ""
        self.year = ""

    def down_info(self, subject_code, year):
        self.subject_code = subject_code
        self.year = year

    def terminate(self):
        self.stop_flag = True

    def run(self):
        subject_name = D.sub_name(self.subject_code)
        save_dir = './{}/{}/'.format(self.subject_code, self.year)

        # request from web page
        C = Crawler(self.subject_code, subject_name, self.year)
        pdfs = C.find_pdfs()

        # retry when connection failed
        if not pdfs:
            MainWindow.http_error(C.url)

        # initial progress_bar
        # MainWindow.init_progress_bar(len(pdfs))

        # download all papers
        for pdf in pdfs:
            # terminate if set
            if self.stop_flag:
                return
            # show current pdf in title
            MainWindow.setWindowTitle(pdf)
            if create_save_dir(save_dir, pdf):
                if not C.save_pdfs(pdf, save_dir):
                    MainWindow.download_error(pdf)

                # pause for delay
                for i in range(self.DELAY):
                    time.sleep(1)
                    MainWindow.setWindowTitle("Pause for {}s".format(self.DELAY - i))

            # self.counter += 1
            # MainWindow.update_progress_bar(self.counter)

        MainWindow.setWindowTitle("Download complete")
        # resume button
        # MainWindow.SubmitButton.setEnabled(True)


if __name__ == '__main__':
    # initial thread
    thread = Download()

    # fetch info from json
    D = Data()
    D.read_json()

    # UI initial - Main window
    app = QApplication(sys.argv)
    MainWindow = MainWindowSetup()
    MainWindowSetup.button_setup(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
