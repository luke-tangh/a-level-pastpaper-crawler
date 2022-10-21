"""
downloader.py
coding:utf-8

Developed by @Luke.Tang 2022
This program crawl cambridge a level papers from papers.gceguide.com.
For more information, please visit github.com/luke-tangh/a-level-paper-downloader
"""

import requests
import re
import os

HTTP_ERROR = "HTTPError"
FILE_EXIST = "FileExist"


class Crawler:
    def __init__(self, code: str, name: str, year: str) -> None:
        self.url = "https://papers.gceguide.com/A%20Levels/{}/{}/".format(name, year)
        self.subject_code = code
        self.subject_name = name
        self.save_dir = './{}/{}/'.format(code, year)
        self.year = year

    def find_pdfs(self) -> list:
        web = get_html(self.url)
        if web == HTTP_ERROR:
            return [] 
        web = web.text
        pdf_list = re.findall(r'('+str(self.subject_code)+'.*?.pdf)', web)
        pdf_set = set()
        # handling abnormal results
        for i in range(len(pdf_list)):
            if len(pdf_list[i]) < 20:
                pdf_set.add(pdf_list[i])
        return list(pdf_list)

    def save_pdfs(self, pdf: str, save_dir: str) -> bool:
        pdf_url = self.url + pdf
        pdf_dir = save_dir + pdf
        pdf_cont = get_html(pdf_url)
        if pdf_cont == HTTP_ERROR:
            return False
        pdf_cont = pdf_cont.content
        with open(pdf_dir, "wb") as f:
            f.write(pdf_cont)
        return True


def get_html(url: str):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r
    except requests.HTTPError:
        return HTTP_ERROR


def create_save_dir(path: str, pdf: str) -> bool:
    if not os.path.exists(path):
        os.makedirs(path)
    if os.path.exists(os.path.normpath(path + '/' + pdf)):
        return False
    else:
        return True
