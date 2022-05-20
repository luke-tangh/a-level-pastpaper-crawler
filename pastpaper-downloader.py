"""
pastpaper-downloader.py
coding:utf-8

Developed by @Luke.Tang 2022
This program crawl cambridge a level papers from papers.gceguide.com
For more information, please visit github.com/Clob4k/a-level-pastpaper-crawler
"""

import requests
import time
import os
import re


def crawl_delay():
    delay = 10
    print('pause for crawl delay...({}s)'.format(delay))
    time.sleep(delay)


def get_html(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r
    except requests.HTTPError:
        return "HTTPError"


def get_pdf_name(url, subject_code):
    web = get_html(url)
    web_text = web.text
    pdf_list = re.findall(r'('+str(subject_code)+'.*?.pdf)', web_text)
    pdf_set = set()
    print("list of download:")
    for i in range(len(pdf_list)):
        if len(pdf_list[i]) < 20:
            pdf_set.add(pdf_list[i])
            
            print(pdf_list[i])
    return pdf_set


year = '2011'
subject_code = '9702'
trial_max = 5
save_path = './{}/{}/'.format(subject_code, year)

subject_dict = {"9702" : "Physics", "9703" : "Chemistry", "9704" : "Biology", \
                "9705" : "Geography", "9706" : "History", "9708" : "Economics",\
                "9709" : "English", "9710" : "Chinese", "9711" : "Mathematics",\
                "9608" : "Computer%20Science%20(for%20final%20examination%20in%202021)",\
                "9618" : "Computer%20Science%20(for%20first%20examination%20in%202021)"}

subject_name = subject_dict[subject_code]
subject = '{}%20({})'.format(subject_name,subject_code)
url = "https://papers.gceguide.com/A%20Levels/{}/{}/".format(subject,year)
print("target url: {}".format(url))

r = requests.get(url, timeout=30)
if r.status_code != 200:
    print('connection failed, double check the parameters')
else:
    print('successfully connected')


pdf_set = get_pdf_name(url, subject_code)
count = 1
trial_max = 5
for pdf in pdf_set:
    trial = 1
    print("=====================")
    print(pdf)
    print(count, "/", len(pdf_set))
    print("=====================")
    pdf_url = url + pdf
    pdf_name = save_path + pdf
    if os.path.exists(save_path) == False:
        os.makedirs(save_path)
    if os.path.exists(pdf_name):
        print("The file has already existed")
    else:
        print("Downloading...")
        pdf_content = get_html(pdf_url)
        while pdf_content == "HTTPError":
            crawl_delay()
            print("Download failed. Retrying...{}/{}".format(trial, trial_max))
            pdf_content = get_html(pdf_url)
            if trial == trial_max:
                print("Download failed. Automatically switch to next item.")
                continue
            trial += 1
        pdf_content = pdf_content.content
        with open(pdf_name, "wb") as f:
            f.write(pdf_content)
        print("successfully downloaded")
        crawl_delay()
    count += 1
print("Download completed {}/{}".format(count-1, len(pdf_set)))

os.system('pause')
