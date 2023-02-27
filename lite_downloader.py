import requests
import time
import os
import re


# set crawl delay
def crawl_delay():
    delay = 30  # default 30s due to robots
    for i in range(delay):
        print('\rpause for crawl delay...({}s)'.format(str(delay-i).rjust(2, '0')), end="")
        time.sleep(1)
    print('\rpause for crawl delay...(00s)')


def get_html(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r
    except requests.HTTPError:
        return None


def get_pdf_name(url, subject_code):
    web = get_html(url)
    web_text = web.text
    pdf_list = re.findall(r'(' + subject_code + '.*?.pdf)', web_text)
    pdf_set = set(pdf_list)
    return pdf_set


# parameters
subject_code = input("enter the subject code(eg. 9702):")
while len(subject_code) != 4 and not subject_code.isdigit():
    print("invalid subject code, please retry")
    subject_code = input("enter the subject code(eg. 9702):")

year = input("enter the year to download(eg. 2015):")
while len(year) != 4 and not year.isdigit():
    print("invalid year, please retry")
    year = input("enter the year to download(eg. 2015):")


trial_max = 5
save_path = './{}/{}/'.format(subject_code, year)


subject_dict = {
    "9231": "Mathematics%20-%20Further%20(9231)",
    "9489": "History%20(9489)",
    "9608": "Computer%20Science%20(for%20final%20examination%20in%202021)%20(9608)",
    "9618": "Computer%20Science%20(for%20first%20examination%20in%202021)%20(9618)",
    "9696": "Geography%20(9696)",
    "9700": "Biology%20(9700)",
    "9701": "Chemistry%20(9701)",
    "9702": "Physics%20(9702)",
    "9708": "Economics(9708)",
    "9709": "Mathematics%20(9709)",
    "9990": "Psychology%20(9990)"
    }


subject = subject_dict[subject_code]
url = "https://papers.gceguide.com/A%20Levels/{}/{}/".format(subject, year)
print("target url: {}".format(url))

r = requests.get(url, timeout=30)
if r.status_code != 200:
    print('connection failed, double check the parameters')
else:
    print('successfully connected')


pdf_set = get_pdf_name(url, subject_code)

print("list of downloading:")
for pdf in pdf_set:
    print(pdf)

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
