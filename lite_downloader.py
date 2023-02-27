import requests
import time
import os
import re


# set crawl delay
def crawl_delay():
    delay = 30  # default 30s due to robots
    print('pause for crawl delay...({}s)'.format(delay))
    time.sleep(delay)


def get_html(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r
    except requests.HTTPError:
        return None


def get_pdf_name(url):
    web = get_html(url)
    web_text = web.text
    pdf_list = re.findall(r'(9702.*?.pdf)', web_text)
    pdf_set = set(pdf_list)
    return pdf_set


# parameters
year = '2014'
subject_code = '9702'
trial_max = 5
save_path = './{}/{}/'.format(subject_code, year)


subject_dict = {
    "9702": "Physics",
    "9701": "Chemistry",
    "9700": "Biology",
    "9696": "Geography",
    "9706": "History",
    "9489": "Economics",
    "9093": "English",
    "9710": "Chinese",
    "9709": "Mathematics",
    "9231": "Mathematics%20-%20Further%20",
    "9608": "Computer%20Science%20(for%20final%20examination%20in%202021)",
    "9618": "Computer%20Science%20(for%20first%20examination%20in%202021)"
}


subject_name = subject_dict[subject_code]
subject = '{}%20({})'.format(subject_name,subject_code)
url = "https://papers.gceguide.com/A%20Levels/{}/{}/".format(subject,year)
print("target url: {}".format(url))

r = requests.get(url, timeout=30)
if r.status_code != 200:
    print('connection failed, double check the parameters')
else:
    print('successfully connected')


pdf_set = get_pdf_name(url)
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
        while pdf_content is None:
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
