# a-level-pastpaper-crawler
Crawl cambridge a level papers from _papers.gceguide.com_

- Amend `subject.json` or `subject_dict` to add additional subjects

- Crawl delay is set to minimum value of 30 seconds according to [_robots.txt_](#robots) from the website.

- Papers are saved in current working folder by default. If needed, `save_path` may be modified. 

# libs
- `requests`
- `pyqt5` _(essential for gui version)_

# run command line version
1. git clone `https://github.com/luke-tangh/a-level-paper-downloader.git` or download ``lite_downloader.py``
2. run `lite_downloader.py`
3. input `subject` and `year`
4. wait for download to complete


# run gui version (not recommended)
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
- 9708 Economics
- 9709 Mathematics
- 9990 Psychology

# robots
Retrieved from _https://www.gceguide.com/robots.txt_

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