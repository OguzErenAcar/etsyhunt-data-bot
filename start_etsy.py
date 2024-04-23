from selenium.webdriver.support import expected_conditions as EC
import pickle
import set_cookies
from time import sleep
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
from selenium.webdriver.support.wait import WebDriverWait

import os

def sayac(sure):
    while(sure>0):
        print(sure)
        sleep(1)
        sure-=1

def login():
    path= os.getenv('BROWSER_EXECUTABLE_PATH')
    driver = uc.Chrome(browser_executable_path=path)
    driver.get("https://etsyhunt.com/user/login")
    sure = 200

    main_window = driver.window_handles[0]

    wait = WebDriverWait(driver, sure)
    wait.until(EC.number_of_windows_to_be(2))

    new_window = [window for window in driver.window_handles if window != main_window][0]
    driver.switch_to.window(new_window)
    wait = WebDriverWait(driver, sure)
    try:
        wait.until(EC.invisibility_of_element_located((By.XPATH, "//body")))
    except Exception as e:
        pass

    driver.switch_to.window(main_window)

    expected_url = "https://etsyhunt.com/etsy-product-research"
    wait.until(EC.url_to_be(expected_url))

    print(driver.current_url)
    sleep(2)
    return driver


def open_etsy(giris:bool,url):
    driver=None

    if(not giris):
        driver =login()
        cookies = driver.get_cookies()
        pickle.dump(cookies, open("cookies.pkl", "wb"))
        print("cookies saved")
    else:
        path = os.getenv('BROWSER_EXECUTABLE_PATH')
        driver = uc.Chrome(browser_executable_path=path)
        driver.get("https://etsyhunt.com/user/login")
        set_cookies.load_cookies(driver)
        driver.get(url)
    print("its is opened ")

    return driver

