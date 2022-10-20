"""
files.py
coding:utf-8

Developed by @Luke.Tang 2022
This program crawl cambridge a level papers from papers.gceguide.com.
For more information, please visit github.com/luke-tangh/a-level-paper-downloader
"""

import json

SUBJECT_NOT_FOUND = "SubjectNotFound"


class Data:
    def __init__(self) -> None:
        self.subject_dict = {}
        self.sub_json_dir = "subject.json"
    
    def read_json(self) -> None:
        # read json to dict
        with open(self.sub_json_dir, 'r') as f:
            self.subject_dict = json.load(f)

    def sub_name(self, code : str) -> str:
        if code in self.subject_dict:
            return self.subject_dict[code]
        else:
            return SUBJECT_NOT_FOUND
