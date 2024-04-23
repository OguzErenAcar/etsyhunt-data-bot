import glob
import os
from time import sleep

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


def isDownload(driver:WebDriver,initial_count:int,time:int)->bool:
    try:
        item = driver.find_element(By.XPATH, "//span[text()='Find 0 products']")
        if item!=None:
            return False
    except:
        print("ürün var ")

    print("bekleniyor..")
    count=1
    while count<16:
        sleep(time)
        print(count,end=" ")
        downloaddir=os.listdir("/Users/oguz/Downloads/")
        current_file_count = len(downloaddir)
        count+=1
        if current_file_count>initial_count:
            print("indiriliyor",end="\n")
            sleep(2)
            return True


    return False


def export(driver:WebDriver, Page):
    try:
        driver.switch_to.frame("zbaseiframe")
    except:
        pass
    try:
        exportButton = driver.find_element(By.XPATH, "//span[text()='Export to CSV']")
        exportButton.click()
        sleep(1)
        button=driver.find_element(By.XPATH,f"//div[text()='{Page}']")
        button.click()
    except Exception as e:
        print("export seçme hatası ")
        export(driver, Page)

def exportDropbox(driver:WebDriver):
    try:
        exportButton = driver.find_element(By.XPATH, "//span[text()='Export to CSV']")
        exportButton.click()
    except Exception as e:
        print("export drowpdown hatası tekrar deneniyor ")
        exportDropbox(driver)

