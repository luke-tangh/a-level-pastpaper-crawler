# a-level-pastpaper-crawler
Crawl cambridge a level papers from _papers.gceguide.com_

- Choose from combo boxs to suit your needs

- Amend `subject.json` or `subject_dict` to add additional subjects

- Crawl delay are set to minimum value of 30 seconds according to the robots from the website.

- Papers are saved in current working folder by default, if needed, `save_path` variable may be modified. 

# libs

- `requests`
- `pyqt5` _optional_

# run command line version

1. git clone `https://github.com/luke-tangh/a-level-paper-downloader.git` 
2. open `lite_downloader.py` with editor
3. modify `subject_code` and `year` below _line 32_
4. run `lite_downloader.py`
5. wait for download to complete


# run gui version
1. git clone `https://github.com/luke-tangh/a-level-paper-downloader.git`
2. run `main.pyw`
3. modify `Subject`, `Year` and `Type` and click download
4. wait for download to complete


> qp - question paper\
> ms - mark scheme\
> gt - grade threshold\
> ci - confidential information


# supported subjects

- 9231 Mathematics Further
- 9489 History
- 9608 Computer Science (old)
- 9618 Computer Science (new)
- 9696 Geography
- 9700 Biology
- 9701 Chemistry
- 9702 Physics
- 9709 Mathematics
- 9990 Psychology

# robots

Retrive from _https://www.gceguide.com/robots.txt_

```
User-agent: *
Crawl-delay: 30
Disallow: 
Disallow: /wp-includes/*
Disallow: /Books/*
Disallow: /assets/*
Disallow: /files/*
Disallow: /draft/*
Disallow: /wp-content/*
```