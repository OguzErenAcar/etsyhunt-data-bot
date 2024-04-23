from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


def select_Category(driver:WebDriver, category):
    try:
        driver.switch_to.frame("zbaseiframe")
    except:
        pass
    try:
        category_element = driver.find_element(By.XPATH, "//span[text()='Category']")
        category_element.click()
        sleep(1)
        CategoryDropBox = driver.find_element(By.XPATH, "//*[@id='category_add']")
        categoryelement = CategoryDropBox.find_element(By.XPATH, f"//span[text()='{category}']")
        action = ActionChains(driver)
        action.move_to_element(categoryelement).click().perform()
    except Exception as e:
        print("Category seçme hatası: ", e)


def select_Country(driver:WebDriver, Country):
    try:
        driver.switch_to.frame("zbaseiframe")
    except:
        pass
    try:

        select_item_list= driver.find_elements(By.XPATH, "//div[@class='zf-select-content']")
        select_item_list[0].click()
        ullist=driver.find_element(By.XPATH,"//ul[@class='el-select-group']")
        sleep(1)
        countryelements = ullist.find_elements(By.XPATH, f"//span[text()='{Country}']")
        countryelements[len(countryelements)-1].click()

    except Exception as e:
        print("Country seçme hatası: ", e)


def select_ProductType(driver:WebDriver, ProductType):
    if ProductType!="Select All":
        try:
            driver.switch_to.frame("zbaseiframe")
        except:
            pass
        try:
            select_item_list= driver.find_elements(By.XPATH, "//div[@class='zf-select-content']")
            select_item_list[1].click()
            sleep(1)
            ProductTypeelement = driver.find_element(By.XPATH, f"//span[text()='{ProductType}']")
            ProductTypeelement.click()
            select_item_list[1].click()


        except Exception as e:
            print("ProductType seçme hatası: ", e)


def unselect_ProductType(driver:WebDriver, ProductType):
    try:
        print("secim bırakılıyor ")
        select_item_list= driver.find_elements(By.XPATH, "//div[@class='zf-select-content']")
        i_element = select_item_list[1].find_element(By.CLASS_NAME, "el-tag__close")
        # Öğeyi tıklayın
        i_element.click()

    except Exception as e:
        print("unProductType seçme hatası: ", e)

def select_label(driver:WebDriver, label:str):
    try:
        driver.switch_to.frame("zbaseiframe")
    except:
        pass
    try:
        select_label = driver.find_element(By.XPATH, f"//span[text()='{label}']")
       # i_element = select_item_list[1].find_element(By.CLASS_NAME, "el-tag__close")
        select_label.click()

    except Exception as e:
        print("label seçme hatası: ", e)


def select_time(driver:WebDriver, time:str):
    try:
        driver.switch_to.frame("zbaseiframe")
    except:
        pass
    try:
        select_label = driver.find_element(By.XPATH, f"//span[text()='{time}']")
       # i_element = select_item_list[1].find_element(By.CLASS_NAME, "el-tag__close")
        select_label.click()

    except Exception as e:
        print("time seçme hatası: ", e)
