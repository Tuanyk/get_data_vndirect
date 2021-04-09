from func.save_get_file import *
from func.get_vndirect import *
from bs4 import BeautifulSoup
from datetime import datetime
import time
import requests
import urllib
import os
import pathlib

current_path = str(pathlib.Path(__file__).parent.absolute())

start_time = time.time()


def save_vndirect_data():
    folder_save = current_path + "/data/vndirect/" + str(datetime.now())
    os.mkdir(folder_save)
    for item, value in get_vndirect_url().items():
        file_name = item + ".html"
        if get_end_element(item) == "":
            continue
        print(get_end_element(item))
        print(folder_save + "/" + file_name)
        save_string_to_file(folder_save + "/" + file_name, get_vndirect_html_data(value, item))
    return folder_save
        

current_data_saved_folder = save_vndirect_data()
all_vndirect_current_file = get_all_file_in_folder(current_data_saved_folder)

datacount = ""
for item in all_vndirect_current_file:
    html = get_file_contents(item)
    soup = BeautifulSoup(html, "html.parser")
    filename = get_filename(item).replace(".html", "")
    current_folder = get_folder_of_file(item)

    data = ""
    lines = soup.find_all("tr")
    for line in lines:
        span = line.find_all("span", id)
        for ispan in span:
            data += ispan.text.strip() + "~"
        data += "\n"
    data = data.strip()
    save_string_to_file(current_folder + "/" + filename + ".txt", data)
    datacount += filename + "=" + str(len(lines)) + "\n"
    delete_file(item)    

save_string_to_file(current_path + "/timedone", str(time.time()))
save_string_to_file(current_path + "/datacount", datacount.strip())

ck_bot_notify("Get Data Done!")

print("Time excute: ", time.time() - start_time)

