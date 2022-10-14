# a-level-pastpaper-crawler
crawl cambridge a level papers from papers.gceguide.com

- Change the variables `year` and `subject_code` to suit your needs

- Crawl delay are set to minimum value of 30 seconds according to the robots from the website.

- Papers are defaultly saved in current working folder, `save_path` variable may be modified to suit your need. 

# supported subjects

* 9709 mathematics
* 9702 physics
* 9701 chemistry
* 9700 biology
* 9708 economics
* 9093 english
* 9696 geography
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