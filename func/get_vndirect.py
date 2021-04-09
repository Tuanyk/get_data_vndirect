from selenium import webdriver
import requests
import urllib

def get_vndirect_html_data(url, san_chung_khoan):
    Options = webdriver.ChromeOptions()
    Options.add_argument('headless')
    driver = webdriver.Chrome(chrome_options=Options)
    driver.get(url)
    end_of_page = False
    while not end_of_page:
        try:
            if driver.find_element_by_id(get_end_element(san_chung_khoan)):
                end_of_page = True
        except:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    html = driver.page_source
    return html

def get_vndirect_url():
    data = {
        "hose" : "https://banggia-hn.vndirect.com.vn/chung-khoan/hose",
        "vn30" : "https://banggia-hn.vndirect.com.vn/chung-khoan/vn30",
        "thoathuanhose" : "https://banggia-hn.vndirect.com.vn/chung-khoan/thoa-thuan-hose",
        "hnx" : "https://banggia-hn.vndirect.com.vn/chung-khoan/hnx",
        "hnx30" : "https://banggia-hn.vndirect.com.vn/chung-khoan/hnx30",
        "thoathuanhnx" : "https://banggia-hn.vndirect.com.vn/chung-khoan/thoa-thuan-hnx",
        "upcom" : "https://banggia-hn.vndirect.com.vn/chung-khoan/upcom",
        "thoathuanupcom" : "https://banggia-hn.vndirect.com.vn/chung-khoan/thoa-thuan-upcom",
    }
    return data

def get_end_element(san_chung_khoan):
    data = {
        "hose" : "YEG",
        "vn30" : "VRE",
        "thoathuanhose" : "",
        "hnx" : "X20",
        "hnx30" : "VMC",
        "thoathuanhnx" : "",
        "upcom" : "YTC",
        "thoathuanupcom" : "",
    }
    return data[san_chung_khoan]

def notify_if_something_is_wrong():
	#Replace your bot notify link here
    bot_noti_url = "https://api.telegram.org/bot0000000000:XXXXXXXXXXXX/sendMessage?chat_id=-0000000000&text="
    bot_mess = "Oops ! Something went wrong !"
    requests.get(bot_noti_url + urllib.parse.quote(bot_mess))

def ck_bot_notify(mess):
    bot_noti_url = "https://api.telegram.org/bot0000000000:XXXXXXXXXXXX/sendMessage?chat_id=-0000000000&text="
    requests.get(bot_noti_url + urllib.parse.quote(mess))