import pickle

from selenium.webdriver.chrome.webdriver import WebDriver


def save_cookies(driver: WebDriver):
    cookies = driver.get_cookies()
    pickle.dump(cookies, open("cookies.pkl", "wb"))
    print("cookies kaydedildi")


def load_cookies(driver: WebDriver):
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        try:
            driver.add_cookie(cookie)
        except:
            pass
    print("google cookie yüklendi ")