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


def get_html(url: str):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r
    except requests.HTTPError:
        return None


def get_pdf_name(web_text: str, code: str) -> set[str]:
    # example: 9702_s20_qp_12.pdf
    pdf_list = re.findall('(' + code + r"_\w\d{2}_\w{2}_\d{2}.pdf)", web_text)
    return set(pdf_list)


def input_sub_code():
    ipt_code = input("enter the subject code(eg. 9702):")
    while len(ipt_code) != 4 and not ipt_code.isdigit():
        print("invalid subject code, please retry")
        ipt_code = input("enter the subject code(eg. 9702):")
    return ipt_code


def input_year():
    ipt_year = input("enter the year to download(eg. 2021):")
    while len(ipt_year) != 4 and not ipt_year.isdigit():
        print("invalid year, please retry")
        ipt_year = input("enter the year to download(eg. 2021):")
    return ipt_year


subject_dict = {
    "9231": "Mathematics%20-%20Further%20(9231)",
    "9489": "History%20(9489)",
    "9608": "Computer%20Science%20(for%20final%20examination%20in%202021)%20(9608)",
    "9618": "Computer%20Science%20(for%20first%20examination%20in%202021)%20(9618)",
    "9696": "Geography%20(9696)",
    "9700": "Biology%20(9700)",
    "9701": "Chemistry%20(9701)",
    "9702": "Physics%20(9702)",
    "9708": "Economics%20(9708)",
    "9709": "Mathematics%20(9709)",
    "9990": "Psychology%20(9990)"
    }


# parameters
count = 1
trial_max = 5

subject_code = input_sub_code()
while subject_code not in subject_dict:
    print("subject code {} is not supported".format(subject_code))
    subject_code = input_sub_code()


year = input_year()


subject = subject_dict[subject_code]
target_url = "https://papers.gceguide.com/A%20Levels/{}/{}/".format(subject, year)
print("target url: {}".format(target_url))


r = get_html(target_url)
if r.status_code != 200:
    print('connection failed, double check the parameters')
else:
    print('successfully connected')


save_path = './{}/{}/'.format(subject_code, year)
if not os.path.exists(save_path):
    os.makedirs(save_path)


pdf_set = get_pdf_name(r.text, subject_code)
print("list of downloading:")
for pdf in pdf_set:
    print(pdf)


for pdf in pdf_set:
    print("---------------------")
    print(pdf)
    print(count, "/", len(pdf_set))
    print("---------------------")

    trial = 1
    pdf_url = target_url + pdf
    pdf_name = save_path + pdf

    if os.path.exists(pdf_name):
        print("File exists")
        count += 1
        continue

    print("Downloading...")
    pdf_download = get_html(pdf_url)
    while pdf_download is None:
        crawl_delay()
        print("Download failed. Retrying...{}/{}".format(trial, trial_max))
        pdf_download = get_html(pdf_url)
        if trial == trial_max:
            print("Download failed. Automatically switch to next item.")
            break
        trial += 1

    if pdf_download is None:
        continue

    pdf_download = pdf_download.content
    with open(pdf_name, "wb") as f:
        f.write(pdf_download)
    print("Successfully downloaded")
    crawl_delay()
    count += 1

print("Download completed {}/{}".format(count-1, len(pdf_set)))
input("Press enter to exit...")
