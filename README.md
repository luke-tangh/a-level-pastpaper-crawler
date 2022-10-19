# a-level-pastpaper-crawler
crawl cambridge a level papers from papers.gceguide.com

- Change the variables `years` to suit your needs

- Amend `subject.json` to add additional subjects

- `years` must be `list[str]` data type that supports batch download mutiple years. 

    > e.g. `['2018', '2019']` is accepted while `[2018, 2019]` / `2019` / `2018` is not.

- Crawl delay are set to minimum value of 30 seconds according to the robots from the website.

- Papers are saved in current working folder by default, if needed, `save_path` variable may be modified. 

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