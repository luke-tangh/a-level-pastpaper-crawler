# a-level-pastpaper-crawler
crawl cambridge a level papers from papers.gceguide.com

* change the variables `year` and `subject_code` to suit your needs

* crawl delay are set to minimum value of 30 seconds according to the robots from the website.

# supported subjects

* 9709 mathematics
* 9702 physics
* 9701 chemistry
* 9700 biology
* 9708 economics
* 9093 english
* 9696 geography
* 9489 history
* 9715 chinese
* 9618 computer science

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