# a-level-pastpaper-crawler
crawl cambridge a level papers from papers.gceguide.com

- Choose from combo boxs to suit your needs

- Amend `subject.json` to add additional subjects

- Crawl delay are set to minimum value of 30 seconds according to the robots from the website.

- Papers are saved in current working folder by default, if needed, `save_path` variable may be modified. 

# libs

- `requests`
- `pyqt5`

# supported subjects

* 9709 mathematics
* 9702 physics
* 9701 chemistry
* 9700 biology
* 9618 computer science
* ...

You can add more subjects by adding subjects in the `subject_dict`.

# robots
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